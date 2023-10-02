import smtplib
import json
import mysql.connector
from email.message import EmailMessage

connection_params = {
    'host': "mysql",
    'user': "root",
    'password': "super-secret-password",
    'database': "my-wonderful-website"
}

request = "Select * from USERS"
emails_list=[]

with mysql.connector.connect(**connection_params) as db:
    with db.cursor() as c:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS USERS (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(255) NOT NULL,
            LastName VARCHAR(255) NOT NULL,
            Email VARCHAR(255) UNIQUE NOT NULL
        )
        """
        c.execute(create_table_query)
        db.commit()

        insert_users = [
            ("Souhail", "Hmahma", "souhailhmahma@gmail.com"),
            ("Souh", "hm", "souhail3032@gmail.com")
        ]
        insert_query = "INSERT INTO USERS (FirstName, LastName, Email) VALUES (%s, %s, %s)"
        c.executemany(insert_query, insert_users)
        db.commit()

        c.execute(request)
        resultats = c.fetchall()
        for utilisateur in resultats:
            emails_list.append(utilisateur[3])
 
json_file = open("config.json")
gmail_cfg = json.load(json_file)
print(gmail_cfg)
print(emails_list)
 
with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
    smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
    for email in emails_list:
        msg = EmailMessage()
        msg["from"] = gmail_cfg["email"]
        msg["Subject"] = "Test"
        msg.add_alternative(f"""\
            <!DOCTYPE html>
            <html>
                <body>
                    <h1>Bojour {email}!</h1>
                    <h3>Vu les nouvelles compliances de sécurité du 1/10/2023 vous devez changer votre mot de passe izly</h3>
                    <h4>Le nouveau mot de passe doit contenir au mois deux caractéres spéciaux, au moins 4 nombres , au moins 5 alphabets</h4>
                    <h5>Visitez ce lien pour le changer</h5>
                    <a href="http://localhost">Lien vers le site</a>
                </body>
            </html>
        """, subtype='html')
        msg["to"] = email
        smtp.send_message(msg)
    print("emails sent!")

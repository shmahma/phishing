from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="super-secret-password",
    database="my-wonderful-website"
)

cursor = db.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS Persons (
    PersonId INT AUTO_INCREMENT PRIMARY KEY,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    Password1 VARCHAR(255) NOT NULL,
    Password2 VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        password1 = request.form['password1']
        password2 = request.form['password2']

        cursor.execute("INSERT INTO Persons (PersonId, LastName, FirstName, Password1, Password2) VALUES (%s, %s, %s, %s, %s)",
                       ('1', last_name, first_name, password1, password2))

        db.commit()

        return redirect('/done')
    else:
        return render_template('index.html')

@app.route('/done')
def done():
    return render_template('done.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

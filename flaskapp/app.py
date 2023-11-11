from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mariadb",
    user="root",
    password="super-secret-password",
    database="my-wonderful-website",
    port="3306"
)

cursor = db.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS Persons (
    PersonId INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']

    cursor.execute("INSERT INTO Persons (username, password) VALUES (%s, %s)", (username, password))
    db.commit()

    return render_template('done.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

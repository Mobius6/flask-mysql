# app.py
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def create_database():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='your_password'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database")
    cursor.close()
    connection.close()

def create_table():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='your_password',
        database='your_database'
    )
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        )
    """)
    cursor.close()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        insert_message(message)
    messages = get_messages()
    return render_template('index.html', messages=messages)

def insert_message(message):
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='your_password',
        database='your_database'
    )
    cursor = connection.cursor()
    query = "INSERT INTO messages (message) VALUES (%s)"
    cursor.execute(query, (message,))
    connection.commit()
    cursor.close()
    connection.close()

def get_messages():
    connection = mysql.connector.connect(
        host='mysql',
        user='root',
        password='your_password',
        database='your_database'
    )
    cursor = connection.cursor()
    query = "SELECT message FROM messages"
    cursor.execute(query)
    messages = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return messages

if __name__ == '__main__':
    create_database()
    create_table()
    app.run(host='0.0.0.0', port=8080)

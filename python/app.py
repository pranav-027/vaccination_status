from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    user='root', password='root', host='db', port="3306", database='db')
print("DB connected")




cursor = connection.cursor()

@app.route('/')
def registration_number_form():
    return render_template('index.html')

@app.route('/submit_registration_number', methods=['POST'])
def submit_registration_number():
    registration_number = request.form['registration_number']
    cursor.execute(f"SELECT * FROM students WHERE RegNo = '{registration_number}'")
    student = cursor.fetchone()
    if student:
        name = student[1]
        vaccination_status = student[2]
        return f"Name: {name}, Vaccination Status: {vaccination_status}"
    else:
        return "No student found with that registration number."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
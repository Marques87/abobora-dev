from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('politics.html')

@app.route('/menu')
def menupage():
    return render_template('page (1).html')

@app.route('/report1')
def report1_page():
    return render_template('report1.html')

@app.route('/report2')
def report2_page():
    return render_template('report2.html')

@app.route('/report3')
def report3_page():
    return render_template('report3.html')

if __name__ == '__main__':
    app.run(debug=True)
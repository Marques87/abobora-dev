from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('politica.html')

@app.route('/menu')
def menupage():
    return render_template('page (1).html')

@app.route('/noticia1')
def noticia1_page():
    return render_template('noticia1.html')

@app.route('/noticia2')
def noticia2_page():
    return render_template('noticia2.html')

@app.route('/noticia3')
def noticia3_page():
    return render_template('noticia3.html')

if __name__ == '__main__':
    app.run(debug=True)
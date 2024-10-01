from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DB'] = 'meu_banco_de_dados'

mysql = MySQL(app)

# Rota da Home
@app.route('/')
def home():
    return render_template('politica.html')

if __name__ == '__main__':
    app.run(debug=True)

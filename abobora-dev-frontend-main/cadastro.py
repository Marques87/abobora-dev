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
    return render_template('cadastro.html')

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (email, senha))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return redirect(url_for('home'))
        else:
            return "Usuário ou senha inválidos!"
    return render_template('login.html')

# Rota de Cadastro de Usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (name, email, senha) VALUES (%s, %s, %s)", (name, email, senha))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('cadastro.html'))
    return render_template('cadastro.html')

@app.route('/cadastro',methods=['GET', 'POST'])
def cadastro_success():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

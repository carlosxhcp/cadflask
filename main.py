from flask import Flask, render_template, redirect, request, flash
import json

import smtplib
import email.message

cad = Flask(__name__)
cad.config['SECRET_KEY']='C1983RLOS'

# Função de enviar email #
def enviar_email(): 
    corpo_email = """
    <h1> Seu cadastro foi efetuado com sucesso, utilize seu nome de usuário e senha para fazer o login. </h1>

"""
    msg = email.message.Message()
    msg['Subject'] = (f"Sejá bem vindo, {user}!")
    msg['From'] = 'tilfurthernotice22@gmail.com'
    msg['To'] = user_email
    password = 'flfd laei nuzw ayll' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
logged=False

@cad.route('/')
def index():
    global logged
    logged = False
    return render_template('index.html')


# Rota utilizada para login #
@cad.route('/login', methods=['POST'])
def login():
    
    global logged

    user = request.form.get('user')
    password = request.form.get('password')

    with open('users.json') as userstemp:
        users = json.load(userstemp)
        cont=0
        for usuario in users:
            cont+=1
            if usuario['user'] == user and usuario['password'] == password:
                return render_template('users.html')
            if cont >= len(users):
                flash('Usuário ou/e senha inválidos!')
                return redirect("/")

# Rota utilizada para novo cadastro #
@cad.route('/novo_cadastro', methods=['POST'])
def novo_cadastro():
    global user_email
    global user
    usuario = []
    user = request.form.get('user')
    user_email = request.form.get('user_email')
    tel = request.form.get('tel')
    password = request.form.get('password')
    usuario = [
        {
            "user":user,
            "user_email":user_email,
            "tel":tel,
            "password":password
        }
    ]
    with open('users.json') as userstemp:
        users = json.load(userstemp)

    usuario_novo = usuario + users
    with open('users.json','w') as gravartemp:
        json.dump(usuario_novo, gravartemp, indent=4)
    enviar_email()
    flash("Usuario cadastrado com sucesso!")
    return render_template('index.html')   



# Rota utilizada para ir até a pagina de cadastro #
@cad.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


#@cad.route('/admin')
#def admin():










if __name__ in "__main__":
    cad.run(debug=True)
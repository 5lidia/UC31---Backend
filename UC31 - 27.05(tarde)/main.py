from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    estado = request.form['estado']
    formacao =  request.form['formacao']
    modalidade = request.form.getlist('modalidades')

    if senha == 12345:
        return f"Correta"
    else:
        return f"Incorreta"

    return "{} e {} e {} e {} e {}".format(nome, email, senha, estado, formacao, modalidade)

if __name__=='__main__':
    app.run(debug=True)
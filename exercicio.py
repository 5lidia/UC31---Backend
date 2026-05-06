from flask import Flask

app = Flask(__name__)

#Questão 1

@app.route('/ola/<nome>')
def ola(nome):
    return f'Olá, {nome}! Seja bem-vinda ao sistema.'

#Questão 2

@app.route('/calculo/<int:n1>/<int:n2>')
def soma(n1, n2):
    resultado = n1 + n2
    return f'A soma de {n1} + {n2} é {resultado}'

#Questões 3

@app.route('/idade/<nome>/<int:idade>')
def dados(nome, idade):
    if idade >= 18:
        return f'Seu nome é {nome} e a sua idade é {idade} e é maior ou igual a 18'
    else:
        return f'Seu nome é {nome} e a sua idade é {idade} e é menor de 18'

#Questões 4

@app.route('/produto/<nome>/<float:preco>')
def compras(nome, preco):
    return f'O produto é {nome} e custa {preco}'

#Questões 5

@app.route('/repetir/<palavra>/<int:vezes>')
def repertir(palavra, vezes):
    return(palavra + ' ') * vezes

if __name__ == '__main__':
    app.run(debug=True)
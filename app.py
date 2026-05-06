from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome = "Gaby"
    return render_template('index.html', title= 'Página Inicial', usuario=usuario, nome=None)

@app.route()
def usuario():
    nome = {'nome','Gaby','email','cosrtezin@gmail.com'}
    return render_template('index.html', title= 'Página Inicial', nome=nome)

@app.route('/dados', defaults={"nome":"usuário comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá,{nome}!'

@app.route('/semestre/<int: x>')
def semestre(x):
    return 'Estamos no semestre' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return 'Você pagou: '+ str(valor)
   
#Questões 3 e 4

@app.route("/arearestrita/<id>")
def area(id):
    cadeados = {
        "1": "Cadeado Fechado",
        "2": "Cadeado Aberto"
    }

    return cadeados.get(id, "ID inválido")


@app.route("/operacao/<tipo>/<int:op1>/<int:op2>")
def operacao(tipo, op1, op2):
    operacoes = {
        "sum": op1 + op2,
        "sub": op1 - op2,
        "mult": op1 * op2,
        "div": op1 / op2
    }

    return f"Resultado: {operacoes.get(tipo, 'Operação inválida')}"

if __name__ == '__main__':
    app.run()
 

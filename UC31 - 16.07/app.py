from flask import Flask, render template
import json

app = Flask(_name_)

@app.route("/")
def produtos():

    with open("produtos.json", "r", encoding="utf-8")as arquivo:
        lista_produtos = json.load(arquivo)

    return render_template("produtos.html", produtos=lista_produtos)
f
app.run(debug=True)
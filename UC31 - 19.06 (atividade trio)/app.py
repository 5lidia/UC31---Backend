from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash
)

app = Flask(__name__)
app.secret_key = "listatarefassessão"

@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefas = request.form["tarefas"]

    tarefas.append({
        "tarefas": tarefas
    })

    return render_template("formulario.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)
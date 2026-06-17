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
app.secret_key = "minha_chave_secreta"

usuario_correto = "lidia"
senha_correta = "1234"


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip().lower()
        senha = request.form.get("senha")

        if usuario == usuario_correto and senha == senha_correta:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))

        flash("Usuário ou senha inválidos!")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        flash("Faça login para acessar o sistema!")
        return redirect(url_for("login"))

    usuario = session["usuario"]
    return f"Login realizado com sucesso! Bem-vindo, {usuario}!"


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Você saiu do sistema!")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
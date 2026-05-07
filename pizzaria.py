from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def home():
    return 'Olaaaaaaa'


@app.route('/pizzaria/<sabor>')
def sabor(sabor):
    if sabor == "calabresa":
        return render_template('calabresa.html')
    elif sabor == "margherita":
        return render_template('magherita.html')
    elif sabor == "frango":
        return render_template('frango.html')
    else:
        return f'Sabor não disponível!'

if __name__ == '__main__':
    app.run(debug=True)
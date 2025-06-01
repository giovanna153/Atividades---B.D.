from flask import Flask

app = Flask(__name__)

@app.route("/")
def olar():
    return "ciao mundo bello"


@app.route("/nome")
def nome():
    return " gio"

@app.route("/magica/<naosei>")
def magica(naosei):
    return naosei


@app.route("/<int:num1>/<int:num2>")
def somar(num1,num2):
    resultado = num1 + num2
    return f"resposta: {resultado}"
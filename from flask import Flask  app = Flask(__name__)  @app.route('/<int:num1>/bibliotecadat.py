from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)
arquivo = "acessos.txt"

@app.route("/")
def index():
    now = datetime.now()
    data_hora_atual = now.strftime("%d/%m/%Y %H:%M")

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            linhas = f.readlines()
    else:
        linhas = []
    linhas = [linha.strip() for linha in linhas if linha.strip()]

    if len(linhas) == 0:
        resposta = "Primeiro Acesso"
    else:
        resposta = linhas[-1]

    with open(arquivo, "a") as f:
        f.write(data_hora_atual + "\n")
    return f"{resposta}\nData e Hora de acesso: {data_hora_atual}"

if __name__ == "__main__":
    app.run(debug=True)


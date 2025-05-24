from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/dia')
def dia_atual():
    agora = datetime.now()
    dia_formatado = agora.strftime('%d/%m/%Y')
    return dia_formatado

@app.route('/hora')
def hora_atual():
    agora = datetime.now()
    hora_formatada = agora.strftime('%H:%M:%S')
    return hora_formatada

if __name__ == '__main__':
    app.run(debug=True)

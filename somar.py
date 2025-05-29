from flask import Flask

app = Flask(__name__)

@app.route('/<int:num1>/<int:num2>')
def soma(num1, num2):
    resultado = num1 + num2
    return f'Resposta: {resultado}'

if __name__ == '__main__':
    app.run(debug=True)

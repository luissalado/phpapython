from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

colores = {
    "Yellow": "#ffff00",
    "Black": "#000000",
    "Green": "#00ff00",
    "Red": "#ff0000",
    "Cyan": "#00ffff",
    "White": "#ffffff",
    "Purple": "#ff00ff",
    "Blue": "#0000ff"
}

def nuevo_secreto(colores):
    secreto = random.choices(list(colores.values()), k=4)
    return secreto

def calcula_resultado(intento, secreto):
    heridos = 0
    muertos = 0
    for i in range(4):
        if intento[i] == secreto[i]:
            muertos += 1
            continue
        if intento[i] in secreto:
            heridos += 1
    return f"Acertados: {muertos}   Descolocados: {heridos}"

@app.route('/', methods=['GET', 'POST'])
def mastermind():
    if 'secreto' not in session:
        session['secreto'] = nuevo_secreto(colores)
    if request.method == 'POST':
        intento = request.form.getlist('intento')
        resultado = calcula_resultado(intento, session['secreto'])
        return render_template('mastermind.html', colores=colores, intento=intento, resultado=resultado)
    return render_template('mastermind.html', colores=colores)

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    session.pop('secreto', None)
    return '', 204

if __name__ == '__main__':
    app.run()


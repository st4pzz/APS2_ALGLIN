from flask import Flask,request
from funcoes import enigma,de_enigma
import numpy as np

app = Flask(__name__)

alfabeto = 'abcdefghijklmnopqrstuvwxyz ãé,.'
alfabeto_identidade = np.identity(len(alfabeto))
encoder = np.roll(alfabeto_identidade,-2,1)
segundo_encoder = np.roll(alfabeto_identidade,7,1)

#Rota que recebe um json com a mensagem e retorna a mensagem cifrada
@app.route("/post/enigma", methods=["POST"])
def enigma1():
    
    if request.method == "POST":
        msg = request.get_json()
        msg = msg["mensagem"]
        msg_enigma = enigma(msg,encoder,segundo_encoder)
        return f"""<h1>A sua mensagem cifrada é : ( {msg_enigma})  <h1>"""


#Rota que recebe um json com a mensagem cifrada e retorna a mensagem decifrada
@app.route("/post/de-enigma", methods=["POST"])
def de_enigma1():
    if request.method == "POST":
        msg = request.get_json()
        msg = msg["mensagem"]
        msg_de_enigma = de_enigma(msg,encoder,segundo_encoder)
        return f"""A sua mensagem decifrada é : ( {msg_de_enigma}) <h1>"""

if __name__ == "__main__":
    app.run(debug=True)
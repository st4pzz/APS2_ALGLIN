from flask import Flask,request
from funcoes import enigma,de_enigma
import numpy as np

app = Flask(__name__)

@app.route("/post/enigma", methods=["POST"])
def enigma1():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz ãé,.'
    alfabeto_identidade = np.identity(len(alfabeto))
    encoder = np.roll(alfabeto_identidade,-2,1)
    segundo_encoder = np.roll(alfabeto_identidade,7,1)
    if request.method == "POST":
        msg = request.get_json()
        msg = msg["mensagem"]
        msg_enigma = enigma(msg,encoder,segundo_encoder)
        msg_de_enigam = de_enigma(msg_enigma,encoder,segundo_encoder)
        return f"""<h1>A nova mensagem é {msg_enigma} <h1>
                <h2>E sua mensagem decifrada é {msg_de_enigam}<h2>"""

if __name__ == "__main__":
    app.run(debug=True)
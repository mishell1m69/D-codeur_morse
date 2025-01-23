from flask import Flask, render_template, request
from python.D_morseur import decode_message, encode_message, dict_encode_message, dict_decode_message, arbre_alphabet_morse


selected = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/decoder')
def decoder():
    return render_template("decoder.html")

@app.route('/d_arbres')
def d_arbres():
    return render_template("d_arbres.html")

@app.route('/d_dicos')
def d_dicos():
    return render_template("d_dicos.html")

@app.route('/encoder')
def encoder():
    return render_template("encoder.html")

@app.route('/e_arbres')
def e_arbres():
    return render_template("e_arbres.html")

@app.route('/e_dicos')
def e_dicos():
    return render_template("e_dicos.html")

@app.route('/d_arbres_resultat', methods = ['POST'])
def d_arbres_resultat():
    text = request.form.get('texte', '')
    ftext = decode_message(text, arbre_alphabet_morse)
    return render_template("d_arbres_resultat.html", decoded_message = ftext)

@app.route('/d_dicos_resultat', methods = ['POST'])
def d_dicos_resultat():
    text = request.form.get('texte', '')
    ftext = None
    return render_template("d_dicos_resultat.html", decoded_message = ftext)

@app.route('/e_arbres_resultat', methods = ['POST'])
def e_arbres_resultat():
    text = request.form.get('texte', '')
    ftext = encode_message(text, arbre_alphabet_morse)
    print(text)
    print(ftext)
    return render_template("e_arbres_resultat.html", encoded_message = ftext)

@app.route('/e_dicos_resultat', methods = ['POST'])
def e_dicos_resultat():
    text = request.form.get('texte', '')
    ftext = None
    return render_template("e_dicos_resultat.html", encoded_message = ftext)

app.run(debug=True)

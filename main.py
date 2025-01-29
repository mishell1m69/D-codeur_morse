from flask import Flask, render_template, request, send_file
from python.D_morseur import decode_message, encode_message, dict_encode_message, dict_decode_message, arbre_alphabet_morse, arbre_dict

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
    if 'file' not in request.files:
        text = request.form.get('texte', '')
        ftext, time = decode_message(text, arbre_alphabet_morse)
        return render_template("d_arbres_resultat.html", decoded_message = ftext, time = time)
    else:
        file = request.files['file']
        text = file.read().decode('utf-8')
        ftext, time = decode_message(text, arbre_alphabet_morse)
        with open("fichier_decode_arbre.txt", "w", encoding="utf-8") as f:
            f.write(ftext)
        return send_file("fichier_decode_arbre.txt", as_attachment=True)
    

@app.route('/d_dicos_resultat', methods = ['POST'])
def d_dicos_resultat():
    if 'file' not in request.files:
        text = request.form.get('texte', '')
        ftext, time = dict_decode_message(arbre_dict, text)
        return render_template("d_dicos_resultat.html", decoded_message = ftext, time = time)
    else:
        file = request.files['file']
        text = file.read().decode('utf-8')
        ftext, time = dict_decode_message(arbre_dict, text)
        with open("fichier_decode_dicos.txt", "w", encoding="utf-8") as f:
            f.write(ftext)
        return send_file("fichier_decode_dicos.txt", as_attachment=True)

@app.route('/e_arbres_resultat', methods = ['POST'])
def e_arbres_resultat():
    if 'file' not in request.files:
        print("oh")
        text = request.form.get('texte', '')
        ftext, time = encode_message(text, arbre_alphabet_morse)
        return render_template("e_arbres_resultat.html", encoded_message = ftext, time = time)
    else:
        file = request.files['file']
        text = file.read().decode('utf-8')
        ftext, time = encode_message(text, arbre_alphabet_morse)
        with open("fichier_encode_arbre.txt", "w", encoding="utf-8") as f:
            f.write(ftext)
        return send_file("fichier_encode_arbre.txt", as_attachment=True)

@app.route('/e_dicos_resultat', methods = ['POST'])
def e_dicos_resultat():
    if 'file' not in request.files:
        text = request.form.get('texte', '')
        ftext, time = dict_encode_message(arbre_dict, text)
        return render_template("e_dicos_resultat.html", encoded_message = ftext, time = time)
    else:
        file = request.files['file']
        text = file.read().decode('utf-8')
        ftext, time = dict_encode_message(arbre_dict, text)
        with open("fichier_encode_dicos.txt", "w", encoding="utf-8") as f:
            f.write(ftext)
        return send_file("fichier_encode_dicos.txt", as_attachment=True)

@app.route('/comparer')
def comparer():
    return render_template("comparer.html")

@app.route('/e_comparer')
def e_comparer():
    return render_template("e_comparer.html")

@app.route('/d_comparer')
def d_comparer():
    return render_template("d_comparer.html")

@app.route('/d_comparer_resultat', methods = ['POST'])
def d_comparer_results():
    text = request.form.get('texte', '')
    ftext_dict, time_dict = dict_decode_message(arbre_dict, text)
    ftext_arbre, time_arbre = decode_message(text, arbre_alphabet_morse)
    return render_template("d_comparer_resultat.html", decoded_message_dict = ftext_dict, decoded_message_arbre = ftext_arbre, time_arbre = time_arbre, time_dict = time_dict)

@app.route('/e_comparer_resultat', methods = ['POST'])
def e_comparer_results():
    text = request.form.get('texte', '')
    ftext_dict, time_dict = dict_encode_message(arbre_dict, text)
    ftext_arbre, time_arbre = encode_message(text, arbre_alphabet_morse)
    return render_template("e_comparer_resultat.html", encoded_message_dict = ftext_dict, encoded_message_arbre = ftext_arbre, time_arbre = time_arbre, time_dict = time_dict)

app.run(debug=True)

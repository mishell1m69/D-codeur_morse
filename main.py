from flask import Flask, render_template, request

selected = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/d_arbres')
def d_arbres():
    return render_template("d_arbres.html")

@app.route('/d_dicos')
def d_dicos():
    return render_template("d_dicos.html")

@app.route('/decoder')
def decoder():
    return render_template("decoder.html")

@app.route('/e_arbres')
def e_arbres():
    return render_template("e_arbres.html")

@app.route('/e_dicos')
def e_dicos():
    return render_template("e_dicos.html")

@app.route('/encoder')
def encoder():
    return render_template("encoder.html")

@app.route('/d_arbres_resultat')
def d_arbres_resultat():
    return render_template("d_arbres_resultat.html")

@app.route('/d_dicos_resultat')
def d_dicos_resultat():
    return render_template("d_dicos_resultat.html")

@app.route('/e_arbres_resultat')
def e_arbres_resultat():
    return render_template("e_arbres_resultat.html")

@app.route('/e_dicos_resultat')
def e_dicos_resultat():
    return render_template("e_dicos_resultat.html")

app.run(debug=True)

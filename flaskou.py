from flask import Flask, render_template, request

selected = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/decoder')
def decoder():
    return render_template("decoder.html")

@app.route('/encoder')
def encoder():
    return render_template("encoder.html")


app.run(debug=True)
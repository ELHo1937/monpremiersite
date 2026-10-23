from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def accueil():
    return render_template("accueil.html")

@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Hocine", nom="rhm")

@app.get("/loisirs")
def loisirs():
    return "Mes loisirs sont la rando, l'automobile et les voyages !"

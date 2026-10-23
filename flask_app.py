from flask import Flask, render_template, request

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
    
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return f"<h1>Bonjour {prenom} !</h1>"
    
@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{a} + {b} = {a + b}"

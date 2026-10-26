
from flask import Flask, render_template, request, redirect, abort, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

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


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")




@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} ! (reçu en {request.method})"


# 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")


# 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404

@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,)



@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",})



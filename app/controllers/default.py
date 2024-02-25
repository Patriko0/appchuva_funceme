from flask import render_template
from app import app
from app.classes.Posto import Posto

@app.route("/")
def index():
    cords = [ 
             Posto("-6.76","-38.96", 80),
             Posto("-3.67","-38.97", 133),
             Posto("-5.91","-39.26", 349) 
            ]
    return render_template("index.html", cords = cords)
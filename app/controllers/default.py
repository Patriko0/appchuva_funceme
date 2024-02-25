from flask import render_template
from app import app
from classes import Posto

@app.route("/")
def index():
    cords = [ 
             Posto("-6.76","-38.96", 1),
             Posto("-3.67","-38.97", 2),
             Posto("-5.91","-39.26", 3) 
            ]

    return render_template("index.html", cords = cords)
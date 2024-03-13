from flask import Blueprint, render_template
import requests as req

web = Blueprint("web", __name__)

@web.route("/")
def t_home():
    # res = req.get("https://pokeapi.co/api/v2/pokemon/charmander").json()
    # print(res["sprites"]["back_default"])
    data = req.get("http://localhost:3000/tickets").json()
    return render_template("index.html", tickets=data)
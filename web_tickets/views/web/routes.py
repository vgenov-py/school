from flask import Blueprint, render_template, request
import requests as req

web = Blueprint("web", __name__)

@web.route("/")
def t_home():
    # res = req.get("https://pokeapi.co/api/v2/pokemon/charmander").json()
    # print(res["sprites"]["back_default"])
    print(request.args)
    data = req.get("http://localhost:3000/tickets").json()
    return render_template("index.html", tickets=data)
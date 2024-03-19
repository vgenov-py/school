from flask import Blueprint, render_template, request
import requests as req

web = Blueprint("web", __name__)

@web.route("/")
def t_home():
    ticket_id = request.args.get("id")
    if ticket_id:
        req.delete("http://localhost:3000/tickets", params={"id": ticket_id})
    print(request.args)
    data = req.get("http://localhost:3000/tickets").json()
    return render_template("index.html", tickets=data)

@web.route("/test")
def t_base():
    return render_template("test.html")
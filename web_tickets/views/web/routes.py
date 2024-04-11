from flask import Blueprint, render_template, request, flash, redirect, session, current_app
import requests as req
from db import get_db

web = Blueprint("web", __name__)

base_api_url = "http://localhost:3000"

@web.route("/")
def t_home():
    ticket_id = request.args.get("id")
    if ticket_id:
        req.delete("http://localhost:3000/tickets", params={"id": ticket_id})
    print(request.args)
    data = req.get("http://localhost:3000/tickets").json()
    return render_template("index.html", tickets=data)

@web.route("/login", methods=["GET", "POST"])
def t_login():
    print(request.form)
    '''
    Comprobar email y pwd de formulario con email y pwd de DB
    1. Usuario envia user y pwd por form {email: test1@email.com, pwd: 1234}
    2. Filtrar user en DB por email WHERE email = "test1@email.com" {pwd: 1234}
    3. Comprobar que pwd de user en DB sea igual o no a PWD de formulario 
    '''
    con = get_db()
    cur = con.cursor()
    print(tuple(cur.execute("SELECT * FROM users;")))
    return render_template("login.html")

@web.route("/ticket/<ticket_id>")
def t_base(ticket_id):
    ticket = req.get(f"{base_api_url}/tickets", params={"id":ticket_id}).json()
    try:
        ticket = ticket[0]
    except IndexError:
        return render_template("ticket.html", ticket_id=ticket_id)
    return render_template("ticket.html", ticket=ticket)

@web.route("/ticket/update/<ticket_id>", methods=["GET", "POST"])
def t_update(ticket_id):
    session["id"] = "ID DEL USUARIO"
    if request.method == "POST":
        params = dict(request.form)
        params["ticket_id"] = ticket_id # {id:1, description: "nueva descripción"}
        res_api = req.patch(f"{base_api_url}/tickets", params=params)
        if res_api.status_code == 200:
            res_api = res_api.json()
            if res_api.get("success"): # res_api["success"]
                flash("Ticket actualizado correctamente!")
                return redirect("/")
            else:
                flash("Algo ha ido mal!")
            print("Ticket actualizado!")
    return render_template("update.html")
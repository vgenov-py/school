import sqlite3
import datetime as dt
from secrets import token_hex

con = sqlite3.connect("tickets.db")
cur = con.cursor()

user = ""
while user != "q":
    print("1. Crear ticket")

    if user == "1":
        ticket_id = token_hex(6)
        departments = cur.execute("SELECT * FROM departments;")
        for i, department in enumerate(departments):
            department_id, department_name = department
            print(f"{i+1}. {department_name}")

        department_id = input("Indicar departamento: ")
        email = input("Email: ")
        description = input("Descripción: ")
        ticket_date = dt.datetime.now()
        query = f"INSERT INTO tickets VALUES (?,?,?,?,?);"
        print(query)
        cur.execute(query, (ticket_id, email, description, ticket_date, department_id))
        con.commit()


    user = input(": ")
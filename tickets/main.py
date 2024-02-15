import sqlite3
import datetime as dt
from secrets import token_hex
from os import system, get_terminal_size
con = sqlite3.connect("tickets.db")
cur = con.cursor()

def clear():
    system("clear")
width = get_terminal_size().columns

def print_center(word: str, separator:str = " "):
    print(word.center(int(width/1.1), separator))

def print_full(word: str, separator:str = " "):
    print(word.center(width,separator))
def menu():
    print_full("_", "_")
    print_center("1. Crear ticket")
    print_center("2. Eliminar ticket")
    print_center("3. Actualizar ticket")
    print_center("Q. Salir")
    print_full("_", "_")



user = ""
while user.lower() != "q":
    clear()
    menu()
    user = input(": ")
    if user == "1":
        clear()
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
        cur.execute(query, (ticket_id, email, description, ticket_date, department_id))
        con.commit()

    elif user == "2":
        clear()
        print_full("Elige para eliminar", "-")
        print_full("",)
        tickets = tuple(cur.execute("SELECT id, email, description FROM tickets;"))
        for i, ticket in enumerate(tickets):
            id_ticket, email, description = ticket
            description = description[:15] if len(description) > 15 else description
            print_center(f"{i + 1}. {email} | {description[:15]}...")
        print_full("-", "-")
        try:
            user = int(input(": ")) - 1
        except ValueError:
            print(f"Debe indicar un número del 1 al {len(tickets)}")
            input(": ")
            user = ""
            continue
        try:
            ticket_id = tickets[user][0]
        except IndexError:
            print(f"Debe indicar un número del 1 al {len(tickets)}")
            input(": ")
            user = ""
            continue
        ticket_to_delete = list(cur.execute(f"SELECT * FROM tickets WHERE id = '{ticket_id}';"))
        print_center(f"¿Desea eliminar el ticket con identificador: {ticket_id}?(Y/N)")
        user = input(": ")
        if user.upper() == "Y":
            cur.execute(f"DELETE FROM TICKETS WHERE id = ?;", (ticket_id,))
        user = input(": ")
    
    elif user == "3": # Opción UPDATE
        con.close()
        con = sqlite3.connect("tickets.db")
        def make_dicts(cursor, row):
            return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

        con.row_factory = make_dicts
        cur = con.cursor()
        print(next(cur.execute("SELECT * FROM tickets LIMIT 1")))
        con.commit()
        input(": ")

import sqlite3
import datetime as dt
from secrets import token_hex
from os import system, get_terminal_size
import csv
con = sqlite3.connect("tickets.db")
cur = con.cursor()

def clear():
    system("clear")
width = get_terminal_size().columns

def print_center(word: str, separator:str = " "):
    print(word.center(int(width/1), separator))

def print_full(word: str, separator:str = " "):
    print(word.center(width,separator))
def menu():
    print_full("_", "_")
    print_center("1. Crear ticket")
    print_center("2. Eliminar ticket")
    print_center("3. Actualizar ticket")
    print_center("4. Exportar todo")
    print_center("5. Exportar por departamento")
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

    elif user == "4":
        print("Exportar")


    # Opción 1
    # headers = cur.execute("pragma table_info(tickets);")
    # headers_name = []
    # for header in headers:
    #     headers_name.append(header[1])

    # # Opción 2 / 2.1
    # headers = [t[1] for t in cur.execute("pragma table_info(tickets);")] # (t[1] for t in cur.execute("pragma table_info(tickets);"))

    # # Opción 3
    # def extract_name(row):
    #     return row[1]

    # headers = map(extract_name, cur.execute("pragma table_info(tickets);"))

    # Opción 4
        headers = list(map(lambda t: t[1], cur.execute("pragma table_info(tickets);")))

        tickets = cur.execute("SELECT * FROM tickets;")
        today = str(dt.datetime.now().date()).replace("-", "")
        with open(f"{today}.csv", mode="w", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerow(headers)
            csv_writer.writerows(tickets)
        input("Base de datos exportada correctamente: ")

    elif user == "5":
        clear()
        print_center("Exportar por departamento")
        departments = list(cur.execute("SELECT * FROM departments;"))
        for i, department in enumerate(departments):
            department_id, department_name = department
            print(f"{i+1}. {department_name}")
        user = int(input(": ")) - 1
        department_id, department_name = departments[user] # ["1", "RRHH"]

        headers = list(map(lambda t: t[1], cur.execute("pragma table_info(tickets);")))
        tickets = list(cur.execute("SELECT * FROM tickets WHERE department_id = ?",[department_id]))
        today = str(dt.datetime.now().date()).replace("-", "")

        with open(f"{today}_{department_name}.csv", mode="w", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerow(headers)
            csv_writer.writerows(tickets)
        input("Base de datos exportada correctamente: ")

        user = ""    

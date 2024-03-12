from flask import Flask, request
import sqlite3
from secrets import token_hex

app = Flask(__name__)

@app.route("/")
def r_home():
    return "Bienvenido al sistema de tickets"

# @app.route("/tickets")
# def r_table_original():
#     con = sqlite3.connect("tickets.db")
#     cur = con.cursor()
#     data = list(cur.execute(f"SELECT * FROM tickets WHERE id = ?;", ("1",)))
#     if not data:
#         return f"No hay valores"
#     return data

# @app.route("/new_ticket")
# def r_new_ticket():
#     con = sqlite3.connect("tickets.db")
#     def make_dicts(cursor, row):
#         return dict((cursor.description[idx][0], value)
#             for idx, value in enumerate(row))

#     con.row_factory = make_dicts
#     cur = con.cursor()
#     cur.execute("INSERT INTO tickets VALUES ('5', 'desdeweb@email.com', 'HTTP', '2024/3/7', '1')")
#     con.commit()
#     return "Ticket creado!"


'''
Las líneas fueron comentadas en pos de simplificar el código
'''
# @app.route("/<table>")
# def r_table(table):
#     print(request.url)
#     args = request.args
#     '''
#     args.keys() -> Todas las claves del diccionario
#     args.values() -> Todos los valores
#     args.items() -> Ambos
#     '''

#     con = sqlite3.connect("tickets.db")
#     def make_dicts(cursor, row):
#         return dict((cursor.description[idx][0], value)
#             for idx, value in enumerate(row))

#     con.row_factory = make_dicts
#     cur = con.cursor()
#     if table in ("tickets", "departments"):
#         '''
#         table = tickets
#         user_id = 1
#         SELECT * FROM tickets WHERE id = 1;
#         data = list(cur.execute(f"SELECT * FROM {table} WHERE id = '{user_id}';"))
#         data = list(cur.execute(f"SELECT * FROM {table} WHERE id = ?;", [user_id]))
#         '''
#         if args:
#             args_items = args.items()
#             list_items = list(args_items)
#             k, v = list_items[0]
#             print("El usuario ha enviado los siguientes argumentos: ", args)
#             data = list(cur.execute(f"SELECT * FROM {table} WHERE {k} = ?;", [v]))
#         else:
#             data = list(cur.execute(f"SELECT * FROM {table}"))
#     else:
#         return f"Error: La tabla {table} Las tablas disponibles son tickets o departamentos"
#     return data

@app.route("/<table>", methods=["GET", "POST"])
def r_table(table):
    args = request.args
    con = sqlite3.connect("tickets.db")
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
            for idx, value in enumerate(row))

    con.row_factory = make_dicts
    cur = con.cursor()
    if request.method == "GET":

        if table in ("tickets", "departments"):
            if args:
                args_items = args.items()
                list_items = list(args_items)
                k, v = list_items[0]
                data = list(cur.execute(f"SELECT * FROM {table} WHERE {k} = ?;", [v]))
            else:
                data = list(cur.execute(f"SELECT * FROM {table}"))
        else:
            return f"Error: La tabla {table} Las tablas disponibles son tickets o departamentos"
        return data
    elif request.method == "POST":
        new_id = token_hex(6)
        def new_ticket():
            cur.execute(f"INSERT INTO {table} VALUES (?,?,?,?,?)", [new_id, "desde@web.com", "description", "2024/10/10", "1"])
            con.commit()
        new_ticket()
        return f"TICKET ({new_id}) CREADO"

if __name__ == "__main__":
    print(__name__)
    app.run(debug=True, port=3000)

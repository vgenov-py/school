from flask import Flask, request
import sqlite3
from secrets import token_hex

app = Flask(__name__)


@app.route("/<table>")
def r_table(table):
    print(request.url)
    args = dict(request.args)
    print(args)
    con = sqlite3.connect("tickets.db")
    cur = con.cursor()
    if table in ("tickets", "departments"):
        data = list(cur.execute(f"SELECT * FROM {table};"))
    else:
        return "Error: Las tablas disponibles son tickets o departamentos"
    return data

if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)
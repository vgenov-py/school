import sqlite3
from secrets import token_hex
con = sqlite3.connect("tickets.db")
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row))

con.row_factory = make_dicts
cur = con.cursor()
def new_ticket(table):
    new_id = token_hex(6)
    cur.execute(f"INSERT INTO {table} VALUES (?,?,?,?,?)", [new_id, "desde@web.com", "description", "2024/10/10", "1"])
    con.commit() 
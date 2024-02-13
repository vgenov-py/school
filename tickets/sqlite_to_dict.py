import sqlite3

con = sqlite3.connect("tickets.db")
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row))

con.row_factory = make_dicts
cur = con.cursor()
print(list(cur.execute(f"SELECT * FROM tickets;"))[-1]["id"])

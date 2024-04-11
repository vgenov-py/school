from flask import current_app
import sqlite3

def get_db():
    return sqlite3.connect(current_app.config["DB_PATH"])

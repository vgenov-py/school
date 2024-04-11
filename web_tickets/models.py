users = '''CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    pwd TEXT NOT NULL,
    token TEXT
);''' 
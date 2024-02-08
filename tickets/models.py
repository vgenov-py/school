create_table_departments = '''
CREATE TABLE departments (
    id TEXT PRIMARY KEY,
    name TEXT
);
'''

create_table_tickets = '''
CREATE TABLE tickets (
    id TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    description TEXT NOT NULL,
    datetime TEXT NOT NULL,
    department_id TEXT NOT NULL, FOREIGN KEY(department_id) REFERENCES departments(id));
'''

queries = {
    "departments": create_table_departments,
    "tickets": create_table_tickets
}
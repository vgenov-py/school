def route(f):
    def inner():
        print("Hola me llamo Javi")
        return f()
    return inner

@route
def r_home():
    return "Bienvenido al sistema de tickets"
@route
def r_tickets():
    return "Todos los tickets"

print(r_home())
print(r_tickets())

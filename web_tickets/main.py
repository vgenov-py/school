from flask import Flask, g
from views.web.routes import web
import json

def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    app.config.from_file("config.json", load=json.load)
    return app

app = create_app()
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
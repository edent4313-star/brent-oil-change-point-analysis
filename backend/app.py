from flask import Flask
from flask_cors import CORS
# This imports your routes from the other file
from backend.api.routes import api 

def create_app():
    app = Flask(__name__)
    CORS(app)

    # All your routes (kpis, historical, etc.) should be registered here
    app.register_blueprint(api) 

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



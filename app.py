from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.career_routes import career_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config["SECRET_KEY"]

    app.register_blueprint(auth_bp)
    app.register_blueprint(career_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    with app.app_context():
        # Import parts of our application
        from .views import routes_blueprint

        app.register_blueprint(routes_blueprint)

        # Could also import models, services etc. here

    return app

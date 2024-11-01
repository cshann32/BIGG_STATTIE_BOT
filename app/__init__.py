# app/__init__.py
from flask import Flask
from .config import Config
from .db_service import init_db  # Add database initialization function here once db_service is set up

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')  # Temporary route for testing
    def home():
        return "Hello, BIGG STATTIE BOT!"

    # Initialize the database connection
    init_db(app)  # This function will be set up in db_service.py

    # Register blueprints here as they are created
    # from .blueprints.home import home as home_blueprint
    # app.register_blueprint(home_blueprint, url_prefix='/home')

    return app
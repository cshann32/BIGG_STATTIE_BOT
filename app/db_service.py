# app/db_service.py
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """Initializes the database with the given Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///bigg_stattie_bot.db')
    API_KEY = os.getenv('API_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Disables modification tracking to save resources

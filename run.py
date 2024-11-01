# run.py
from app import create_app

# Create the application instance
app = create_app()

# Run the app in debug mode for development
if __name__ == "__main__":
    app.run(debug=True)

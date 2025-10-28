# backend/app.py
import sys, os
# Add current directory (backend) to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from routes.disease_routes import disease_bp  # Local import now works

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Register routes
app.register_blueprint(disease_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "AnimalCare API is running"}

if __name__ == "__main__":
    app.run(debug=True)

# backend/app.py
import os
import logging
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.disease_routes import disease_bp

# Logging setup
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "app.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_BUILD_PATH = os.path.abspath(os.path.join(BASE_DIR, "../frontend/build"))

# Flask app setup
app = Flask(
    __name__,
    static_folder=FRONTEND_BUILD_PATH,
    static_url_path="/"
)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# Register routes
app.register_blueprint(disease_bp, url_prefix="/api")

# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    target = os.path.join(FRONTEND_BUILD_PATH, path)
    if path != "" and os.path.exists(target):
        return send_from_directory(FRONTEND_BUILD_PATH, path)
    else:
        return send_from_directory(FRONTEND_BUILD_PATH, "index.html")

# Health check
@app.route("/api/health")
def health_check():
    logger.info("Health check route accessed")
    return {"message": "AnimalCare API is running"}

# Main
if __name__ == "__main__":
    logger.info("Starting Flask server...")
    app.run(host="0.0.0.0", port=8000, debug=True)

# backend/routes/disease_routes.py
from flask import Blueprint, request, jsonify
# from backend.config import get_db_connection
from config import get_db_connection
# from backend.utils.matching import match_disease
from utils.matching import match_disease
from psycopg2.extras import RealDictCursor

disease_bp = Blueprint("disease_bp", __name__)

@disease_bp.route("/predict-disease", methods=["POST"])
def predict_disease():
    data = request.json
    animal = data.get("animal")              # e.g. "chickens"
    selected_symptoms = data.get("symptoms") # e.g. ["fever", "cough"]

    if not animal or not selected_symptoms:
        return jsonify({"error": "Animal type and symptoms required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(f"SELECT disease_name, symptoms, medicine FROM {animal};")
        disease_rows = cursor.fetchall()
        conn.close()

        result = match_disease(selected_symptoms, disease_rows)
        return jsonify(result)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Database query failed"}), 500

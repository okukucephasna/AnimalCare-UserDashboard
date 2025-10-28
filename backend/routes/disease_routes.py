# backend/routes/disease_routes.py
from flask import Blueprint, request, jsonify
from config import get_db_connection
from utils.matching import match_disease
import logging

disease_bp = Blueprint("disease", __name__)
logger = logging.getLogger(__name__)

@disease_bp.route("/predict-disease", methods=["POST"])
def predict_disease():
    try:
        data = request.get_json()
        animal = data.get("animal")
        symptoms = data.get("symptoms", [])

        # Validate input
        if not animal or not symptoms:
            return jsonify({"error": "Missing animal or symptoms"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT disease_name, symptoms, medicine
            FROM diseases
            WHERE animal_type = %s;
        """
        cursor.execute(query, (animal,))
        rows = cursor.fetchall()

        disease_rows = []
        for row in rows:
            disease_rows.append({
                "disease_name": row[0],
                "symptoms": [s.strip().lower() for s in row[1].split(",")],
                "medicine": row[2]
            })

        # Match disease
        matched = match_disease(selected_symptoms=symptoms, disease_rows=disease_rows)

        cursor.close()
        conn.close()

        return jsonify({
            "animal": animal,
            "disease": matched["disease"],
            "medicine": matched["medicine"]
        }), 200

    except Exception as e:
        logger.error("Error in /predict-disease: %s", e)
        return jsonify({"error": str(e)}), 500

@disease_bp.route("/test-db", methods=["GET"])
def test_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT animal_type, disease_name, symptoms, medicine FROM diseases LIMIT 5;")
        rows = cursor.fetchall()

        data = [
            {
                "animal_type": row[0],
                "disease_name": row[1],
                "symptoms": row[2],
                "medicine": row[3]
            }
            for row in rows
        ]

        return jsonify({"status": "success", "data": data}), 200

    except Exception as e:
        logger.error("Error in /test-db: %s", e)
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

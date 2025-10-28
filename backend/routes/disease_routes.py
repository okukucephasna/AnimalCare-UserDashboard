# routes/disease_routes.py
from flask import Blueprint, request, jsonify
from config import get_db_connection
from utils.matching import match_disease

disease_bp = Blueprint("disease_bp", __name__)

@disease_bp.route("/api/predict-disease", methods=["POST"])
def predict_disease():
    try:
        data = request.get_json()

        # Validate input presence
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400

        animal = data.get("animal")
        symptoms = data.get("symptoms")

        # Validate animal
        valid_animals = ["chickens", "cows", "goats"]
        if not animal:
            return jsonify({"error": "Missing 'animal' field"}), 400
        if animal not in valid_animals:
            return jsonify({"error": f"Unknown animal type '{animal}'. Choose from {valid_animals}"}), 400

        # Validate symptoms
        if not symptoms or not isinstance(symptoms, list) or len(symptoms) == 0:
            return jsonify({"error": "Please provide a list of symptoms"}), 400

        # Proceed if all is valid
        conn = get_db_connection()
        cursor = conn.cursor()

        # Disease matching
        disease = match_disease(cursor, animal, symptoms)

        if not disease:
            return jsonify({"message": "No disease match found for given symptoms"}), 404

        return jsonify({"animal": animal, "predicted_disease": disease}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "An internal server error occurred"}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

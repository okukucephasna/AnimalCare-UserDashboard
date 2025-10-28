# backend/utils/matching.py

def match_disease(selected_symptoms, disease_rows):
    """
    Compare user's selected symptoms with disease data.
    Returns the best match or None.
    """
    for disease in disease_rows:
        disease_symptoms = disease['symptoms']
        if all(symptom in disease_symptoms for symptom in selected_symptoms):
            return {
                "disease": disease['disease_name'],
                "medicine": disease['medicine']
            }
    return {"disease": "Unknown", "medicine": "Consult a vet"}

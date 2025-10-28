// src/pages/Dashboard.jsx
import React, { useState } from "react";
import { Form, Button, Card, Row, Col } from "react-bootstrap";
import { api } from "../api/api";
import ResultModal from "../components/ResultModal";

function Dashboard() {
  const [animal, setAnimal] = useState("");
  const [symptoms, setSymptoms] = useState([]);
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [loading, setLoading] = useState(false);

  const symptomOptions = {
    chickens: ["fever", "cough", "diarrhea", "paralysis", "weakness"],
    cows: ["fever", "loss of appetite", "nasal discharge", "salivation", "diarrhea"],
    goats: ["fever", "diarrhea", "lethargy", "nasal discharge", "anorexia"],
  };

  const handleSymptomChange = (symptom) => {
    setSymptoms((prev) =>
      prev.includes(symptom)
        ? prev.filter((s) => s !== symptom)
        : [...prev, symptom]
    );
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const response = await api.post("/predict-disease", { animal, symptoms });
      setResult(response.data);
      setShowModal(true);
    } catch (err) {
      console.error(err);
      setResult({ disease: "Unknown", medicine: "No recommendation available" });
      setShowModal(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <Card className="shadow-lg p-4 rounded-4">
        <h3 className="text-center mb-4">🐾 AnimalCare Diagnosis Dashboard</h3>

        <Form onSubmit={handleSubmit}>
          <Row className="mb-3">
            <Col md={6}>
              <Form.Group>
                <Form.Label>Select Animal</Form.Label>
                <Form.Select
                  value={animal}
                  onChange={(e) => setAnimal(e.target.value)}
                  required
                >
                  <option value="">-- Choose an Animal --</option>
                  <option value="chickens">Chicken</option>
                  <option value="cows">Cow</option>
                  <option value="goats">Goat</option>
                </Form.Select>
              </Form.Group>
            </Col>
          </Row>

          {animal && (
            <div className="mb-4">
              <Form.Label>Select Symptoms</Form.Label>
              <div className="d-flex flex-wrap">
                {symptomOptions[animal].map((symptom) => (
                  <Form.Check
                    key={symptom}
                    type="checkbox"
                    id={symptom}
                    label={symptom}
                    checked={symptoms.includes(symptom)}
                    onChange={() => handleSymptomChange(symptom)}
                    className="me-3 mb-2"
                  />
                ))}
              </div>
            </div>
          )}

          <Button
            variant="primary"
            type="submit"
            disabled={!animal || symptoms.length === 0 || loading}
          >
            {loading ? "Diagnosing..." : "Diagnose"}
          </Button>
        </Form>
      </Card>

      <ResultModal
        show={showModal}
        onHide={() => setShowModal(false)}
        result={result}
      />
    </div>
  );
}

export default Dashboard;

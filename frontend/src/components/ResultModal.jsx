// src/components/ResultModal.jsx
import React from "react";
import { Modal, Button, ListGroup } from "react-bootstrap";

const ResultModal = ({ show, onHide, result }) => {
  const hasResult = result && (result.disease || result.medicine);

  return (
    <Modal show={show} onHide={onHide} centered>
      <Modal.Header closeButton>
        <Modal.Title>Diagnosis Result</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {hasResult ? (
          <ListGroup variant="flush">
            {result.animal && (
              <ListGroup.Item>
                <strong>Animal:</strong> {result.animal}
              </ListGroup.Item>
            )}
            {result.disease && (
              <ListGroup.Item>
                <strong>Disease:</strong> {result.disease}
              </ListGroup.Item>
            )}
            {result.medicine && (
              <ListGroup.Item>
                <strong>Medicine:</strong> {result.medicine}
              </ListGroup.Item>
            )}
          </ListGroup>
        ) : (
          <p className="text-muted">No diagnosis available for the selected inputs.</p>
        )}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={onHide}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default ResultModal;

// src/components/ResultModal.jsx
import React from "react";
import { Modal, Button } from "react-bootstrap";

const ResultModal = ({ show, onHide, result }) => {
  return (
    <Modal show={show} onHide={onHide} centered>
      <Modal.Header closeButton>
        <Modal.Title>Diagnosis Result</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {result ? (
          <>
            <p><strong>Animal:</strong> {result.animal}</p>
            <p><strong>Disease:</strong> {result.disease}</p>
            <p><strong>Medicine:</strong> {result.medicine}</p>
          </>
        ) : (
          <p>No result available.</p>
        )}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
};

export default ResultModal;

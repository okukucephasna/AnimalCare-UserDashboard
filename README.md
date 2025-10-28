# 🐾 AnimalCare Diagnosis Dashboard

A web application for diagnosing animal diseases based on selected symptoms. The project uses a **React frontend** and a **Flask backend** connected to a **PostgreSQL database**.

---

## Table of Contents

* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Setup & Installation](#setup--installation)
* [Database Setup](#database-setup)
* [Running the Application](#running-the-application)
* [Testing API Endpoints](#testing-api-endpoints)
* [Usage](#usage)
* [License](#license)

---

## Features

* Select an animal (Chicken, Cow, Goat).
* Choose multiple symptoms.
* Diagnose disease with recommended medicine.
* View results in a responsive modal.
* Fetch disease data from a PostgreSQL database.
* Health check endpoint for backend.

---

## Technologies Used

* **Frontend:** React, React Bootstrap, Axios
* **Backend:** Flask, Flask-CORS, Python
* **Database:** PostgreSQL
* **Other Tools:** Git, Postman

---

## Project Structure

```
AnimalCare-UserDashboard/
│
├── backend/
│   ├── app.py               # Flask app entry point
│   ├── config.py            # DB connection config
│   ├── routes/
│   │   └── disease_routes.py
│   └── utils/
│       └── matching.py
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── api.js       # Axios API instance
│   │   ├── components/
│   │   │   └── ResultModal.jsx
│   │   └── pages/
│   │       └── Dashboard.jsx
│   └── package.json
│
├── README.md
└── requirements.txt
```

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/AnimalCare-UserDashboard.git
cd AnimalCare-UserDashboard
```

2. **Backend Setup**

```bash
cd backend
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
# .venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. **Frontend Setup**

```bash
cd ../frontend
npm install
```

---

## Database Setup

1. Create PostgreSQL database `animalcare_db`.
2. Create table `diseases`:

```sql
CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    animal_type VARCHAR(50),
    disease_name VARCHAR(100),
    symptoms TEXT,
    medicine VARCHAR(200)
);

-- Sample data
INSERT INTO diseases (animal_type, disease_name, symptoms, medicine)
VALUES
('chickens', 'Newcastle', 'fever,cough,diarrhea,paralysis', 'Antiviral meds'),
('cows', 'Foot and Mouth', 'fever,loss of appetite,nasal discharge', 'Supportive care'),
('goats', 'Peste des Petits Ruminants', 'fever,diarrhea,lethargy', 'Vaccination and fluids');
```

3. Update your `config.py` with your database credentials.

---

## Running the Application

1. **Start Backend**

```bash
cd backend
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python app.py
```

Backend will run on `http://127.0.0.1:8000`.

2. **Start Frontend**

```bash
cd frontend
npm start
```

Frontend will run on `http://localhost:3000`.

---

## Testing API Endpoints (Postman)

1. **Health Check**

```http
GET http://127.0.0.1:8000/api/health
```

2. **Test DB Connection**

```http
GET http://127.0.0.1:8000/api/test-db
```

3. **Predict Disease**

```http
POST http://127.0.0.1:8000/api/predict-disease
Content-Type: application/json

{
  "animal": "cows",
  "symptoms": ["fever", "loss of appetite", "nasal discharge"]
}
```

---

## Usage

1. Open the frontend in your browser.
2. Select an animal from the dropdown.
3. Check symptoms that match the animal.
4. Click **Diagnose** to see the result.
5. A modal will show the disease and recommended medicine.

---
Working demo
<img width="959" height="401" alt="app working" src="https://github.com/user-attachments/assets/3cf5578b-c46f-4e0d-953f-b993a148f113" />


## License

This project is licensed under the MIT License.

---


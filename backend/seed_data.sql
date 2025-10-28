-- 1. Create the database (if not already created)
CREATE DATABASE animalcare_db;

-- 2. Connect to the database
\c animalcare_db;

-- 3. Create the 'diseases' table
CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,                  -- unique ID for each disease
    animal_type VARCHAR(50) NOT NULL,      -- type of animal (chickens, cows, goats)
    disease_name VARCHAR(100) NOT NULL,    -- name of the disease
    symptoms TEXT NOT NULL,                 -- comma-separated symptoms
    medicine VARCHAR(200) NOT NULL         -- recommended medicine/treatment
);

-- 4. Insert sample data
INSERT INTO diseases (animal_type, disease_name, symptoms, medicine) VALUES
('chickens', 'Newcastle Disease', 'fever,cough,diarrhea,paralysis,weakness', 'Antiviral meds, Supportive care'),
('chickens', 'Avian Influenza', 'fever,cough,loss of appetite', 'Vaccination, Isolation'),
('cows', 'Foot and Mouth', 'fever,loss of appetite,nasal discharge,salivation,diarrhea', 'Supportive care, Isolation'),
('cows', 'Mastitis', 'swelling,heat,redness,pain in udder', 'Antibiotics, Anti-inflammatory meds'),
('goats', 'Peste des Petits Ruminants', 'fever,diarrhea,lethargy,nasal discharge,anorexia', 'Vaccination, Fluids'),
('goats', 'Enterotoxemia', 'diarrhea,abdominal pain,lethargy', 'Antitoxins, Supportive care');

-- 5. Verify the data
SELECT * FROM diseases;

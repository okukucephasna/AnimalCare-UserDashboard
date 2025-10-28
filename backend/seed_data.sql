-- Create tables
CREATE TABLE IF NOT EXISTS chickens (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    symptoms TEXT[] NOT NULL,
    medicine VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS goats (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    symptoms TEXT[] NOT NULL,
    medicine VARCHAR(255) NOT NULL
);

-- Insert sample data
INSERT INTO chickens (disease_name, symptoms, medicine)
VALUES
('Newcastle Disease', ARRAY['fever', 'cough', 'diarrhea'], 'Vaccination and supportive care'),
('Avian Influenza', ARRAY['fever', 'lethargy', 'loss of appetite'], 'Antiviral drugs & isolation');

INSERT INTO goats (disease_name, symptoms, medicine)
VALUES
('Foot and Mouth Disease', ARRAY['fever', 'blisters', 'lameness'], 'NSAIDs and supportive care'),
('Peste des Petits Ruminants', ARRAY['fever', 'diarrhea', 'nasal discharge'], 'Vaccination & supportive therapy');

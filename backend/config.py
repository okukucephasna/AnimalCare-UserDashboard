# backend/config.py
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="animalcare2",
        user="postgres",       # replace with your username
        password="root" # replace with your password
    )
    return conn

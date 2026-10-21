import json
from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FILE = BASE_DIR / "data" / "processed" / "weather_processed.json"

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

with open(PROCESSED_FILE, "r") as file:
    weather = json.load(file)

query = """
INSERT INTO weather_data (
    ciudad,
    fechaHora,
    temperatura,
    humedad,
    velocidadViento
)
VALUES (
    :ciudad,
    :fechaHora,
    :temperatura,
    :humedad,
    :velocidadViento
)
"""

with engine.connect() as connection:
    connection.execute(
        text(query),
        weather
    )
    connection.commit()

print("Datos cargados correctamente en PostgreSQL")
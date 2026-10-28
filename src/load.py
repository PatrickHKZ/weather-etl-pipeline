import json
from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from logger import logger


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FILE = BASE_DIR / "data" / "processed" / "weather_processed.json"


try:

    load_dotenv()

    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL no encontrada en .env")


    engine = create_engine(DATABASE_URL)


    with open(PROCESSED_FILE, "r") as file:
        weather = json.load(file)


    if not weather:
        raise ValueError("El archivo procesado está vacío")


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


    logger.info("Datos cargados correctamente en PostgreSQL")




except Exception as error:

    logger.error(f"Error cargando datos en PostgreSQL: {error}")
    raise
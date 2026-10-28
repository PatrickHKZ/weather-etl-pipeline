import requests
import json
from datetime import datetime
from pathlib import Path
from logger import logger


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"


def extract():

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    URL = "https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.66&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        logger.info(
            f"API response status: {response.status_code}"
        )

        data = response.json()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = RAW_DIR / f"weather_{timestamp}.json"

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        logger.info(f"Archivo raw guardado: {filename}")

        return filename

    except Exception as error:
        logger.error(f"Error durante extracción: {error}")
        raise
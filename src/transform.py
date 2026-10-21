import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from logger import logger

BASE_DIR=Path(__file__).resolve().parent.parent
RAW_DIR=BASE_DIR/"data"/"raw"
PROCESSED_DIR=BASE_DIR/"data"/"processed"

try:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    files=list(RAW_DIR.glob("weather_*.json"))
    latest_file=max(files,key=lambda file: file.stat().st_mtime)
    with open(latest_file,"r") as file:
        data=json.load(file)

    if "current" not in data:
        raise ValueError("La respuesta no contiene datos actuales del clima")

    current=data["current"]
    utc_time = datetime.fromisoformat(current["time"])
    utc_time = utc_time.replace(tzinfo=ZoneInfo("UTC"))
    chile_time = utc_time.astimezone(
        ZoneInfo("America/Santiago")
    )

    transformed_data={
        "ciudad":"Santiago",
        "fechaHora": chile_time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura": current["temperature_2m"],
        "humedad":current["relative_humidity_2m"],
        "velocidadViento": current["wind_speed_10m"]   
    }

    output_file=PROCESSED_DIR/"weather_processed.json"
    with open(output_file,"w") as file:
        json.dump(transformed_data,file,indent=4)
except Exception as error:
    logger.error(f"Error durante transformación: {error}")
    raise

logger.info(f"Archivo transformado {output_file}")

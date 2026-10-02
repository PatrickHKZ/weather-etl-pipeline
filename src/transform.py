import json
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
RAW_DIR=BASE_DIR/"data"/"raw"
PROCESSED_DIR=BASE_DIR/"data"/"processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
files=list(RAW_DIR.glob("weather_*.json"))
latest_file=max(files,key=lambda file: file.stat().st_mtime)
with open(latest_file,"r") as file:
    data=json.load(file)

current=data["current"]

transformed_data={
    "city":"Santiago",
    "timestamp": current["time"],
    "temperature": current["temperature_2m"],
    "humidity":current["relative_humidity_2m"],
    "wind_speed": current["wind_speed_10m"]   
}

output_file=PROCESSED_DIR/"weather_processed.json"
with open(output_file,"w") as file:
    json.dump(transformed_data,file,indent=4)

print(f"Archivo transformado {output_file}")

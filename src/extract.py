import requests
import json
from datetime import datetime
from pathlib import Path
BASE_DIR= Path(__file__).resolve().parent.parent
RAW_DIR=BASE_DIR/"data"/"raw"
#Crear carpeta cuando no existe
RAW_DIR.mkdir(parents=True,exist_ok=True)

URL = "https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.66&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

response=requests.get(URL)
response.raise_for_status()
print(response.status_code)

data=response.json()

timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
filename=f"{RAW_DIR}/weather_{timestamp}.json"

with open(filename, "w") as file:
    json.dump(data,file,indent=4)

print(f"Archivo Guardado: {filename}")
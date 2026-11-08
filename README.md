# ETL Weather Pipeline

## Descripción

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) desarrollado en Python que obtiene información meteorológica desde la API de Open-Meteo, transforma los datos y los almacena en una base de datos PostgreSQL.

El proyecto fue desarrollado con una arquitectura modular, utilizando Docker para facilitar su despliegue y garantizar un entorno reproducible.

---

# Objetivos

- Consumir datos desde una API REST.
- Procesar y transformar información en formato JSON.
- Almacenar los datos en PostgreSQL.
- Aplicar una arquitectura ETL modular.
- Contenerizar la aplicación utilizando Docker.
- Gestionar la configuración mediante variables de entorno.
- Versionar el proyecto con Git y GitHub.

---

# Tecnologías utilizadas

- Python 3.14
- PostgreSQL 18
- Docker
- Docker Compose
- SQLAlchemy
- Requests
- python-dotenv
- Git
- GitHub

---

# Arquitectura del proyecto

```text
                    Open-Meteo API
                           │
                           ▼
                    extract.py
                           │
                           ▼
                 data/raw/*.json
                           │
                           ▼
                   transform.py
                           │
                           ▼
        data/processed/weather_processed.json
                           │
                           ▼
                      load.py
                           │
                           ▼
                     PostgreSQL
```

---

# Estructura del proyecto

```text
etl_weather/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docker/
│   └── init/
│
├── logs/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── main.py
│   └── logger.py
│
├── .env
├── .env.docker
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Flujo ETL

## 1. Extract

Se realiza una solicitud HTTP a la API de Open-Meteo para obtener información meteorológica de Santiago de Chile.

Los datos obtenidos se almacenan automáticamente dentro de:

```text
data/raw/
```

Cada ejecución genera un archivo JSON con marca de tiempo.

---

## 2. Transform

El proceso de transformación:

- Lee el archivo RAW más reciente.
- Valida la estructura de los datos.
- Convierte la fecha desde UTC a la zona horaria de Chile.
- Extrae únicamente la información necesaria.
- Genera un archivo procesado.

Resultado:

```text
weather_processed.json
```

---

## 3. Load

La etapa de carga:

- Lee el archivo procesado.
- Establece conexión con PostgreSQL mediante SQLAlchemy.
- Inserta la información en la tabla:

```text
weather_data
```

---

# Ejecución del proyecto

## Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd etl_weather
```

---

## Crear entorno virtual

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configurar variables de entorno

Crear un archivo:

```text
.env
```

Ejemplo:

```env
DATABASE_URL=postgresql://postgres:admin@localhost:5432/weather_dw_local
```

Para Docker:

```env
DATABASE_URL=postgresql://postgres:admin@postgres:5432/weather_dw
```

---

## Ejecutar localmente

```bash
python src/main.py
```

---

## Ejecutar con Docker

Construir la imagen

```bash
docker compose build
```

Levantar servicios

```bash
docker compose up -d
```

Ejecutar el pipeline

```bash
docker exec -it weather_etl python src/main.py
```

---

# Base de datos

Tabla principal:

```text
weather_data
```

Campos:

| Campo | Descripción |
|--------|-------------|
| ciudad | Ciudad consultada |
| fechaHora | Fecha y hora local |
| temperatura | Temperatura actual |
| humedad | Humedad relativa |
| velocidadViento | Velocidad del viento |

---

# Características implementadas

- Arquitectura ETL modular.
- Separación de responsabilidades.
- Variables de entorno para distintos ambientes.
- Conversión de zona horaria UTC → America/Santiago.
- Manejo de excepciones.
- Registro mediante logger.
- Dockerización completa del proyecto.
- Persistencia de datos mediante volúmenes Docker.
- Versionado con Git y GitHub.

---

# Aprendizajes obtenidos

Durante el desarrollo de este proyecto se aplicaron conocimientos relacionados con:

- Consumo de APIs REST.
- Procesamiento de datos JSON.
- Automatización de procesos ETL.
- Manejo de PostgreSQL desde Python.
- SQLAlchemy.
- Docker y Docker Compose.
- Variables de entorno.
- Organización modular de proyectos Python.
- Control de versiones con Git.

---

# Autor

**Patrick Hernandez**

Ingeniero en Informática

Proyecto desarrollado como parte de mi preparación para roles de Data Analyst y Data Engineering.
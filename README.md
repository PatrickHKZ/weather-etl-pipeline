# ETL Weather Pipeline

Pipeline ETL desarrollado en Python que obtiene información meteorológica desde la API de Open-Meteo, procesa los datos y los almacena en PostgreSQL.

El proyecto utiliza Docker y Docker Compose para crear un entorno reproducible, evitando la necesidad de instalar manualmente Python, PostgreSQL u otras dependencias.

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
- Github

---

# Arquitectura del proyecto

```text
                Open-Meteo API
                      |
                      v
                Extract
                      |
                      v
              Datos RAW (JSON)
                      |
                      v
              Transformación
                      |
                      v
          Datos procesados (JSON)
                      |
                      v
                  Load
                      |
                      v
              PostgreSQL Database
```

---

# Requisitos previos

Antes de ejecutar el proyecto, instalar:

## Docker Desktop

Debe estar instalado y ejecutándose.

Verificar:

```bash
docker --version
docker compose version
```

## Git

Verificar:

```bash
git --version
```

---

# Instalación del proyecto

## 1. Abrir Docker Desktop

Abrir Docker Desktop y esperar hasta que indique:

```text
Engine running
```

---

## 2. Clonar el repositorio

Elegir una carpeta donde guardar el proyecto.

Ejemplo:

```text
C:\Proyectos
```

Clonar:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd etl_weather
```

> Nota: La ruta puede variar dependiendo de dónde se haya descargado el proyecto.

---

# Configuración inicial

## Crear archivo de configuración Docker

Dentro de la carpeta principal del proyecto ejecutar:

Windows CMD:

```cmd
echo DATABASE_URL=postgresql://postgres:admin@postgres:5432/weather_dw> .env.docker
```

El archivo debe llamarse exactamente:

```text
.env.docker
```

No debe quedar como:

```text
.env.docker.txt
```

---

# Ejecución del proyecto

## 1. Construir e iniciar los contenedores

Ejecutar:

```bash
docker compose up -d --build --wait
```

La primera ejecución puede tardar varios minutos mientras Docker descarga las imágenes necesarias.

Al finalizar deben existir dos servicios activos:

```text
weather_postgres
weather_etl
```

Verificar:

```bash
docker ps
```

---

# Ejecutar pipeline ETL

Ejecutar:

```bash
docker compose exec etl python src/main.py
```

El proceso realizará:

1. Extracción desde Open-Meteo.
2. Transformación de datos.
3. Carga en PostgreSQL.

---

# Revisar ejecución

Los registros del proceso se almacenan en:

```text
logs/etl.log
```

Consultar:

Windows CMD:

```cmd
type logs\etl.log
```

Ejecución correcta:

```text
Datos cargados correctamente en PostgreSQL

PIPELINE FINALIZADO
```

---

# Consultar resultados

Para visualizar los datos almacenados:

```bash
docker compose exec postgres psql -U postgres -d weather_dw -c "SELECT * FROM weather_data ORDER BY id DESC;"
```

El comando mostrará los registros almacenados en la tabla:

```text
weather_data
```

---

# Detener el proyecto

Cuando finalice la prueba:

```bash
docker compose down
```

Los datos se conservan.

No utilizar:

```bash
docker compose down -v
```

ya que elimina los volúmenes y la información almacenada en PostgreSQL.

---

# Estructura del proyecto

```text
etl_weather/
│
├── src/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── logger.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── docker/
│   └── init/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.docker
└── README.md
```

---

# Solución de problemas comunes

## Docker no inicia

Verificar que Docker Desktop esté abierto y mostrando:

```text
Engine running
```

---

## Error de conexión a PostgreSQL

Revisar que los contenedores estén activos:

```bash
docker ps
```

Debe aparecer:

```text
weather_postgres
weather_etl
```

---

## El proyecto fue detenido anteriormente

Ejecutar:

```bash
docker compose down
```

Luego:

```bash
docker compose up -d --build --wait
```

---

# Autor

Patrick Hernandez

Proyecto desarrollado como parte de preparación para roles de Data Analyst y Data Engineering.
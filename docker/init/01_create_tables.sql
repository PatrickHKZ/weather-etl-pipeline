CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    ciudad VARCHAR(100),
    fechaHora TIMESTAMP,
    temperatura FLOAT,
    humedad INTEGER,
    velocidadViento FLOAT
);
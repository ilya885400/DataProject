CREATE TABLE weather_events (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    temperature_c FLOAT NOT NULL,
    humidity_percent FLOAT NOT NULL,
    pressure_hpa FLOAT NOT NULL,
    wind_speed_ms FLOAT NOT NULL
);

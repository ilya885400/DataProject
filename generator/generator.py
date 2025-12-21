import time
import random
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="db",
    database="weather",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()

def generate_realistic_weather():
    # Температура от -20 до +35
    temp = round(random.uniform(-20, 35), 2)
    # Влажность 20–100%
    hum = round(random.uniform(20, 100), 2)
    # Давление 980–1040 гПа
    pressure = round(random.uniform(980, 1040), 2)
    # Скорость ветра 0–20 м/с
    wind = round(random.uniform(0, 20), 2)

    return temp, hum, pressure, wind

while True:
    temperature, humidity, pressure, wind = generate_realistic_weather()
    
    cursor.execute("""
        INSERT INTO weather_events (temperature_c, humidity_percent, pressure_hpa, wind_speed_ms)
        VALUES (%s, %s, %s, %s)
    """, (temperature, humidity, pressure, wind))
    
    conn.commit()
    print("Inserted event at", datetime.now())

    time.sleep(1)

# src/weather_api.py
import requests
import os

# Configuration de l'API
API_KEY = os.getenv("API_KEY", "a69b8bc00846de2a42dcff82d4fcb8fa")  # Remplace "votre_clé_api" par ta clé ou définis la variable d'environnement
VILLE = os.getenv("VILLE", "Paris")
URL_API = f"http://api.openweathermap.org/data/2.5/weather?q={VILLE}&appid={API_KEY}&units=metric&lang=fr"

def get_weather():
    """Récupère les données météorologiques depuis l'API OpenWeatherMap."""
    try:
        response = requests.get(URL_API, timeout=5)
        response.raise_for_status()
        donnees = response.json()
        temperature = donnees['main']['temp']
        conditions = donnees['weather'][0]['description']
        humidite = donnees['main']['humidity']
        return temperature, conditions, humidite
    except Exception as e:
        print("Erreur lors de la récupération des données météo :", e)
        return None, None, None

if __name__ == "__main__":
    temp, cond, hum = get_weather()
    print(f"Température : {temp}°C, Conditions : {cond}, Humidité : {hum}%")

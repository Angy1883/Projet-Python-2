import requests
import os

# Variables de configuration
API_KEY = os.getenv("API_KEY", "a69b8bc00846de2a42dcff82d4fcb8fa")  # Tu peux mettre ta clé API ici ou la récupérer depuis un .env
CITY = os.getenv("CITY", "Paris")  # Ville par défaut : Paris
API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    """Récupère la météo à partir de l'API OpenWeatherMap."""
    try:
        response = requests.get(API_URL)
        data = response.json()

        # Extraire les informations principales
        temperature = data['main']['temp']
        conditions = data['weather'][0]['description']
        humidity = data['main']['humidity']

        return temperature, conditions, humidity

    except Exception as e:
        print(f"Erreur lors de la récupération des données météo : {e}")
        return None, None, None

# Test rapide du module
if __name__ == "__main__":
    temperature, conditions, humidity = get_weather()
    print(f"Température: {temperature}°C - {conditions} - Humidité: {humidity}%")

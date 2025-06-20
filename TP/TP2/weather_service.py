import requests
import json
from datetime import datetime

def get_temperature(city):
    """Récupère la température d'une ville via une API"""
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': 'fake_api_key',
        'units': 'metric'
    }
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.RequestException:
        return None
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        return None

def save_weather_report(city, filename="weather_log.json"):
    """Récupère la météo et la sauvegarde dans un fichier"""

    # 1. Récupérer la température
    temp = get_temperature(city)
    if temp is None:
        return False

    # 2. Créer le rapport
    report = {
        'city': city,
        'temperature': temp,
        'timestamp': datetime.now().isoformat()
    }

    # 3. Sauvegarder dans le fichier
    try:
        # Lire le fichier existant
        with open(filename, 'r') as f:
            reports = json.load(f)
    except FileNotFoundError:
        reports = []

    reports.append(report)

    with open(filename, 'w') as f:
        json.dump(reports, f)

    return True
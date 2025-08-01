from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Załaduj zmienne z pliku .env

# Dane z ENV
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
FROM = os.environ["FROM"]
TO = os.environ["TO"]
API_KEY = os.environ["API_KEY"]
CITY = os.environ["CITY"]

def get_weather():
    WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pl"
    r = requests.get(WEATHER_URL)
    data = r.json()

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    return f"🌤️ Pogoda w {CITY}:\n🌡️ {temp}°C\n🌬️ Wiatr: {wind} m/s\n🌥️ {desc.capitalize()}"

def send_whatsapp(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=FROM,
        to=TO
    )

if __name__ == "__main__":
    weather = get_weather()
    send_whatsapp(weather)

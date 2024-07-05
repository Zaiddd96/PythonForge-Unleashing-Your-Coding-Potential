import requests
from twilio.rest import Client

# Constants for API endpoints and credentials
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "__YOUR_OWM_API_KEY__"
TWILIO_ACCOUNT_SID = "__YOUR_TWILIO_ACCOUNT_ID__"
TWILIO_AUTH_TOKEN = "__YOUR_TWILIO_AUTH_TOKEN__"

# Parameters for the weather API request
weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": API_KEY,
    "cnt": 4,
}

# Fetch weather data
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain
will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in weather_data["list"])

# Send SMS alert if it will rain
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR_TWILIO_VIRTUAL_NUMBER",
        to="YOUR_TWILIO_VERIFIED_REAL_NUMBER"
    )
    print(message.status)

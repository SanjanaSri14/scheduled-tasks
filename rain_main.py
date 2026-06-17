import os
import requests
from twilio.rest import Client

access_key = "6T9RVQJ9FU9A728545P6DMDA"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("API_KEY")
account_sid = "AC62d70857288794f20319c366206ec74c"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TO_NUM = os.environ.get("TO_NUM")

parameters = {
    "lat": 26.144518,
    "lon": 91.736237,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_id = weather_data["list"]

will_rain = False
for i in weather_data["list"]:
    if i["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella!☔",
        to="whatsapp:TO_NUM"
    )

    print(message.status)

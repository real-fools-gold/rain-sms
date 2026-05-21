import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
parameters = {
    "lat": 51.924419,
    "lon": 4.477733,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an umbrella☔️ today.",
        from_="+19383005382",
        to="+31683830726",
    )
    print(message.status)

# import libraries
import requests
from twilio.rest import Client

# define environment variables
account_sid = "twilio account id"
auth_token = "account auth token"
parameters = {  # set parameters
    "appid": "openweather api id",
    "lat": 6.922338, # latitude of the location
    "lon": 79.866815, # longitude of the location
    "exclude": "current,minutely,daily",


}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters) # get the connection with api
response.raise_for_status() # check the connection
weather_data = response.json() # convert data into json mode
weather_slice = weather_data["hourly"][:12] # get the relevant data

will_rain = False # not rain

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700: # check the climate id
        will_rain = True # rain

if will_rain: # if rain
    client = Client(account_sid, auth_token) # connect with twilio

    # create a message
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔", # message
        from_="twilio default number", # sender's number
        to="receiver's number",
    )

    print(message.status)


# import libraries
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "email address"
PASSWORD = "password"

# current location
MY_LAT = 6.922194
MY_LONG = 79.867031

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json") # connect with the API
    response.raise_for_status() # check the connectivity
    data = response.json() # convert data into json format

    iss_latitude = float(data["iss_position"]["latitude"]) # get the position
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = { # set the parameters
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) # connect with the API
    response.raise_for_status() # check the connectivity
    data = response.json() # convert data into json format
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) # get the sunrise time
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) # get the sunset time

    time_now = datetime.now().hour # get the current hour of the time

    if time_now >= sunset or time_now <= sunrise: # check the current time is at night
        return True


while True: # if night
    time.sleep(60) # sleep 60 seconds and run again
    if is_night() and is_iss_overhead(): # if night and ISS moving over the current location
        connection = smtplib.SMTP("smtp.google.com") # connect with gmail smtp protocol
        connection.starttls() # encrypt the transaction
        connection.login(user=MY_EMAIL, password=PASSWORD) # login to the gmail
        connection.sendmail( # send the mail
            from_addr=MY_EMAIL, # sender's mail
            to_addrs=MY_EMAIL, # receiver's mail
            msg="Subject:Look up in the sky 👆\n\nThe ISS is above you in the sky" # message
        )


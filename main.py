import requests
import smtplib


parameters = {
    "lat": 19.075983,
    "lon": 72.877655,
    "exclude": "current,minutely,daily",
    "appid": YOUR API KEY HERE
}
end_point = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(end_point, params=parameters)
response.raise_for_status()
data = response.json()
weather_slicing = data["hourly"][:12]
# print(weather_slicing)
will_rain = False
for hour_data in weather_slicing:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

        # print("Bring an umbrella")
        # print("You will need that Today")
if will_rain:
    mail = YOUR MAIL HERE
    password = YOUR PASSWORD HERE
    to = WHO IS GOING TO RECEIVE THE MAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs=to,
                            msg=f"Subject:Weather alert\n\n Bring an umbrella ")
else:
     mail = YOUR MAIL HERE
    password = YOUR PASSWORD HERE
    to = WHO IS GOING TO RECEIVE THE MAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs=to,
                            msg=f"Subject:Weather alert\n\n 'No need' to Bring an umbrella")
# print(data["hourly"][0]["weather"][0]["id"])

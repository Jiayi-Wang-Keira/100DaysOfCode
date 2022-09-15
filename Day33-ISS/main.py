import requests
import datetime as dt
import smtplib
LONG = -3.533620
LAT = 50.721802
# setup email
my_email = "kyawang0113@gmail.com"
my_password = "369258147@Wjy"

# get iss now
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["latitude"])

# get sunrise/set time
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now = dt.datetime.now().hour()
print(time_now)

if LONG-5 <= iss_longitude <= LONG+5 and LAT-5 <= iss_latitude <= LAT+5 and (time_now>sunset or time_now<sunrise):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email ,password=my_password)
        connection.sendmail(from_addr="kkk@gmail.com", to_addrs="kkk@gmail.com", msg="see")

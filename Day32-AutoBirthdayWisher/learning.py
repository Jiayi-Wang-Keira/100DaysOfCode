import smtplib
import datetime as dt
import random

# get weekday
now = dt.datetime.now()
day_of_week = now.weekday()

# setup email
my_email = "kyawang0113@gmail.com"
my_password = "369258147@Wjy"

if day_of_week == 2:
    # randomly choose quotes
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        random_quote = random.choice(all_quotes)

    # send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="jw1289@exeter.ac.uk", msg=f"Subject:HELLO\n\n"
                                                                                    f"{random_quote}")

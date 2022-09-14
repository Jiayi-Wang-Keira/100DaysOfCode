import smtplib

import pandas as pd
import datetime as dt
import random

# 1. Update the birthdays.csv
birth_info = pd.read_csv("birthdays.csv")
print(birth_info)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthday = (now.month, now.day)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birth_info.iterrows()}

if birthday in birthdays_dict:
    random_letter = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
    with open(random_letter) as letter:
        contents = letter.read()
        contents_replace = contents.replace("[NAME]", birthdays_dict[birthday]["name"])

    # setup email
    my_email = "kyawang0113@gmail.com"
    my_password = "369258147@Wjy"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[birthday]["email"], msg=f"Subject: Happy "
                                                                                                "Birthday\n\n"
                                                                                                f"{contents_replace}")






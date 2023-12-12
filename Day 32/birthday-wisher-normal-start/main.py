##################### Normal Starting Project ######################

import datetime as dt
import smtplib
import pandas
import random

# 1. Update the birthdays.csv with your friends & family's details. 

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

df = pandas.read_csv("Day 32/birthday-wisher-normal-start/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today]
    choice = random.randint(1,3)
    with open(f"Day 32/birthday-wisher-normal-start/letter_templates/letter_{choice}.txt") as letter:
        contents = letter.read()
        final_letter = contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "catentertainers@gmail.com"
    my_password = "stsu muqc tbbf mwwu"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=birthday_person["email"], 
                                msg=f"Subject:Happy Birthday\n\n{final_letter}"
            )


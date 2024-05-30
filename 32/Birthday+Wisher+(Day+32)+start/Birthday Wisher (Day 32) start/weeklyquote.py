# #stsu muqc tbbf mwwu
# import smtplib

# my_email = "catentertainers@gmail.com"
# my_password = "stsu muqc tbbf mwwu"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="hicks.carissa@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)
# if year == 2023:
#     print("wear a face mask!")

# month = now.month
# print(month)

# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1996, month=4, day=6)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

my_email = "catentertainers@gmail.com"
my_password = "stsu muqc tbbf mwwu"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("Day 32\Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="hicks.carissa@gmail.com", 
                            msg=f"Subject:Your Weekly Quote\n\n{quote}"
        )
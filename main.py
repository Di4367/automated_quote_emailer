import smtplib
import random
import datetime as dt

MY_EMAIL = "sharma.disha.it@gmail.com"
PASSWORD = "wzkghwhahymyljgf"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation Quotes\n\n{quote}"
                            )
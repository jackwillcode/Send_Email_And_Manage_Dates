# import smtplib
#
# my_email = "jackiewillcode@gmail.com"
# my_password = "b&66gKCOyhnt&0#Oq#@O"
# googleSMTP = "smtp.gmail.com"
# yahooSMTP = "smtp.mail.yahoo.com"
#
# # Smtplib object to connect to our email provider's smtp email server
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # Secure our connection to email server using tls
#     connection.starttls()
#     # Login to email
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="jackwillcode@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email, again."
#                         )

import smtplib
import datetime as dt
import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get current date and time
now = dt.datetime.now()
day_index = now.weekday()

if days[day_index] == "Monday":
    # Open and read all quotes from file line-by-line
    with open("quotes.txt") as file_object:
        quotes = file_object.readlines()

    random_quote = random.choice(quotes)

    my_email = "jackiewillcode@gmail.com"
    my_password = "b&66gKCOyhnt&0#Oq#@O"
    googleSMTP = "smtp.gmail.com"
    yahooSMTP = "smtp.mail.yahoo.com"

    # Smtplib object to connect to our email provider's smtp email server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # Secure our connection to email server using tls
        connection.starttls()
        # Login to email
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jackwillcode@yahoo.com",
                            msg=f"Subject:Monday Motivation Quote\n\n{random_quote}"
                            )
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

# Get today day and month
dt = dt.datetime.today()
current_day = dt.day
current_month = dt.month

birthday_data = pandas.read_csv("birthdays.csv")



for index, row in birthday_data.iterrows():
    if row['day'] == current_day and row['month'] == current_month:
        random_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter}.txt", "r") as letter:
            content = letter.read().replace("[NAME]", row['name'])
            receiver_email = row['email']

gmail_user = 'oppajeongpython@gmail.com'
gmail_password = 'jeongpython123'
sent_from = gmail_user
to = receiver_email
subject = 'I love you so much!!!'
body = content

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user=gmail_user, password=gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')




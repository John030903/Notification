import streamlit as st
import datetime
import smtplib
import ssl
from email.message import EmailMessage
from lunarcalendar import  Lunar
import schedule
import time


def send_email():
    today = datetime.datetime.now()
    lunar = Lunar.from_date(datetime.date(today.year,today.month,today.day))
    if lunar.day == 1 or lunar.day == 15:
        email_sender = 'nguyenhoangkhanhduy030923@gmail.com'
        email_password = 'hutohayrvhiritth'
        email_receiver = '21522002@gm.uit.edu.vn'

        # Set the subject and body of the email
        subject = 'Today is fasting day'

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

st.header('Notification App')
schedule.every().day.at("05:00").do(send_email)
while True:
    schedule.run_pending()
    time.sleep(1000)

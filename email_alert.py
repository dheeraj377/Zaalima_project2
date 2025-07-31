# email_alert.py
import smtplib
from email.mime.text import MIMEText

def send_email(product_title, price, url):
    sender = "dheerajnani2255@gmail.com"
    password = "vrqu wcgc wluq uiag"
    receiver = "dheerajnani2255@gmail.com"

    subject = f"Price Drop Alert for {product_title}"
    body = f"The price is now ₹{price}.\nCheck here: {url}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

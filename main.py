import urllib.request
import smtplib
from email.mime.text import MIMEText
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.google.com"
is_service_up = True


def send_email():
    # sender email
    gmail_user = 'your_email@gmail.com'
    # This is an app specific password.
    # You can find how to generate a password here -> https://support.google.com/accounts/answer/185833?hl=en
    gmail_password = ''

    sent_from = gmail_user
    # Email Body
    body = """
    This is an email sent by Python Script.
    """
    message = MIMEText(body)
    # A list of recipients ( No limit - Min 1 )
    recipients = ['mail@gmail.com', 'mail2@gmail.com', 'mail3@hotmail.com']
    # Message Subject
    message['Subject'] = "Subject line"
    message['From'] = gmail_user
    message['To'] = ", ".join(recipients)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, recipients, message.as_string())
        server.close()
    except:
       print('Something went wrong...')

while is_service_up:
    try:
        response = urllib.request.urlopen(url)
        code = response.getcode()
        if code != 200:
            send_email()
            is_service_up = False
    except Exception as e:
        send_email()
        is_service_up = False
    # define sleep time by seconds
    time.sleep(60)


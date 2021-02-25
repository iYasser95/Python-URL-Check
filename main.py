import urllib.request
import smtplib
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.google.com"
is_service_up = True


def send_email():
    # sender email
    gmail_user = ''
    # This is an app specific password.
    gmail_password = ''

    sent_from = gmail_user
    # Receiver
    to = ['']
    # Email Body
    body = """
    This is an email sent by Python Script.
    """
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, body)
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


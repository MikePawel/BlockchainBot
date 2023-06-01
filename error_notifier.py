import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


def get_info():
    "C:/Users/radli/code/documentation/plt/doc/sell_rbc.csv"
    myfile = open("C:/Users/radli/code/autoswap_js/notifier/txt/swap_info", "r")
    result = myfile.read()
    myfile.close()
    return result


def buy_init_error():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(smtp, port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "BUY INIT ERROR :(\n"
    body = "Please Restart"
    # and then attach that body
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)

    # lastly quit the server
    server.quit()


def sell_init_error():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "SELL INIT ERROR:(\n"
    body = "Please Restart"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()


def pancake_init_error():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "PANCAKE ERROR!!!\n"
    body = "Please Restart"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()


def uniswap_init_error():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")
    sms_gateway = "radlinski.mikolaj@gmail.com"

    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "UNISWAP ERROR!!!\n"
    body = "Please Restart"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()


def setup_init_error(tokenname):

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    # Make sure you add a new line in the subject
    if tokenname == "XED":
        msg["Subject"] = "SETUP ERROR (XED)!\n"
    elif tokenname == "RBC":
        msg["Subject"] = "SETUP ERROR (RBC)!\n"
    else:
        msg["Subject"] = "SETUP ERROR!!!\n"
    # Make sure you also add new lines to your body
    body = "Please Restart"
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)

    # lastly quit the server
    server.quit()


def died_intentionally():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "I will die intentionally :)\n"
    body = "Full chill, don't panic, I'll die in 30s"
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()


def setting_up():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "CHILLEX\n"
    body = "Setting up..."
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()


def swapped():

    email = "skastradingalert@gmail.com"
    pas = os.getenv("EMAIL_PAS")

    sms_gateway = "radlinski.mikolaj@gmail.com"
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = sms_gateway
    msg["Subject"] = "SWAPPED!!!\n"
    body = get_info()
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, "plain"))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)
    server.quit()

from distutils.log import info
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


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
msg["Subject"] = "Go swap\n"
with open("swap_info.txt", "r") as myfile:
    swap_info = myfile.read()
print(swap_info)
body = swap_info
# and then attach that body furthermore you can also send html content.
msg.attach(MIMEText(body, "plain"))

sms = msg.as_string()

server.sendmail(email, sms_gateway, sms)
server.quit()

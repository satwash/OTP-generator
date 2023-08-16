import smtplib
from email.mime.text import MIMEText
import random
sender = "otp_sender_mail@gmail.com"          #email which sends OTP
key = "pass/key"


###########################################################################################

otp_requestor = "otp_requestor_mail@gmail.com"     #email who wants OTP


def otp(otp_requestor):
    temp = random.randint(1000,9999)
    body = "your one time password is:" + str(temp)
    msg = MIMEText(body)
    msg["Subject"] = "Your OTP is"
    msg['To'] = otp_requestor


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, key)
       smtp_server.sendmail(sender, otp_requestor, msg.as_string())
    print("Message sent!")



otp(otp_requestor)

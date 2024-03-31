import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

userid = "rajgoraeklavya@gmail.com"
password = "gcur bofk zbvc dsvl"

try:
    server.login(userid, password)
except smtplib.SMTPAuthenticationError:
    print("Error: Unable To Authenticate.\nPlease Check Your Email-ID and Password.")
    exit()

otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
body = "Your OTP: " + otp

receiver = input("Enter Your Email-ID: ")

if "@" not in receiver or "." not in receiver:
    print("Error: Invalid email address.")
    exit()

try:
    msg = MIMEMultipart()
    msg['From'] = userid
    msg['To'] = receiver
    msg['Subject'] = "OTP Verification"
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(userid, receiver, msg.as_string())
    print("OTP Sent Successfully")
except Exception as e:
    print("Error:", e)
    exit()

receiver_otp = input("Enter OTP For Verification: ")
if receiver_otp == otp:
    print("OTP Verified")
else:
    print("Invalid OTP")

server.quit()
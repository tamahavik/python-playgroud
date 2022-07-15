import smtplib

SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "xxxxxxx"
PASSWORD = "xxxxxx"

connection = smtplib.SMTP(SMTP_ADDRESS)
# secure connection
connection.starttls()
connection.login(user=EMAIL, password=PASSWORD)
connection.sendmail(from_addr=EMAIL, to_addrs="xxxxxxxx", msg="hellow")
connection.close()

import smtplib
import sys
sys.path.append(r'C:\Users\Helen\Desktop\gmit\details')
import details # password and email are stored outside of git folder in details module
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
FROM_EMAIL_ADDRESS = input('Who is sending the email?')
TO_EMAIL_ADDRESS = input('Who do you want to send the email to?')
SUBJECT= input("Enter the subject of the email")
TEXT = input('Write your message')
MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
server.login(details.username,details.password)
server.sendmail(FROM_EMAIL_ADDRESS,TO_EMAIL_ADDRESS,MESSAGE, SUBJECT)
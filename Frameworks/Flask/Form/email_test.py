import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.ehlo()
# server.starttls()
# server.login('myprojectgateway@gmail.com', 'dlvqesmydzahpaqe')
# msg = MIMEMultipart()
# msg['From'] = 'lasantha'
# msg['To'] = 'sglasanthapradeep@gmail.com'
# msg['Subject'] = 'Just a testing text'
# message = 'From Flask Email Testing_2'
# msg.attach(MIMEText(message))
# server.send_message(msg)
# server.quit()
# print("Email Sent.")


def email(receiver,subject,message_content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('myprojectgateway@gmail.com', 'dlvqesmydzahpaqe')
        msg = MIMEMultipart()
        msg['From'] = 'lasantha'
        msg['To'] = receiver
        msg['Subject'] = subject
        message = message_content
        msg.attach(MIMEText(message))
        server.send_message(msg)
        server.quit()
        print("Email Sent.")



receiver="sglasanthapradeep@gmail.com"
subject="Testing"
message_content="From Flask Third test"

email(receiver,subject,message_content)


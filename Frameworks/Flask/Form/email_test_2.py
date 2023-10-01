import smtplib

message="Sample email from flask !"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('myprojectgateway@gmail.com','dlvqesmydzahpaqe')
server.sendmail('myprojectgateway@gmail.com','sglasanthapradeep@gmail.com',message)

print("Message Sent")

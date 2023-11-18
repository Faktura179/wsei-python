import email
import smtplib

with open("message.txt", 'r') as file:
    sender_name, recipient_email, subject, content = file.read().splitlines()

message = email.message.EmailMessage()
message.set_content(content)
message['Subject'] = subject
message['From'] = sender_name
message['To'] = recipient_email

with open("settings.txt", 'r') as file:
    username, password = file.read().splitlines()

smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_username = username
smtp_password = password

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred while sending the email:", str(e))

import smtplib, ssl
import getpass as gp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Open the attachment file for reading in binary mode (using 'rb'), and make it a MIMEApplication class
def file_attacher(email_message, file_name):
    with open(file_name, 'rb') as f:
        file_attachment = MIMEApplication(f.read())
        # Add header/name to the attachments  
        file_attachment.add_header("Content-Disposition",f"attachment; filename = {file_name}")
        # Attach the file to the message
        email_message.attach(file_attachment)

# Defining required details
smtp_server = "smtp.gmail.com"
port = "465"
html = """
This message contains an attachment, html enclosed text and simple text(this sentence).
<h1 style = "color:#045803;">Hello Prathamesh!</h1><br>
<p> This is the second Program file for <b>Python Experiment 13<b>. </p>
<p> The Python program used to send this email itself is the second program file. <b>Thanks for replying !.</b></p>
"""
sender = "2021ca06f@sigce.edu.in"
receiver = "2021ca69f@sigce.edu.in"
password = gp.getpass(f"Enter your app password for {sender}: ")

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = sender
email_message['To'] = receiver
email_message['Subject'] = "SMTP e-mail test (HTML, File Attachments)"

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attaching a file to the email message using function
file_attacher(email_message, "Program13b.py")

# Convert it as a string
email_string = email_message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender, password)

    #sending the email:
    server.sendmail(sender, receiver, email_string)

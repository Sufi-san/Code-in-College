import smtplib, ssl
import getpass as gp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Defining HTML Doc:
html = """
This is an e-mail message to be sent in HTML format
<html>
<body>
    <b>This is an HTML message.</b>
    <h1>This is a heading.</h1>
</body>
</html>
"""

# Defining Required Details
smtp_server = "smtp.gmail.com"
port = 465

sender = "2021ca06f@sigce.edu.in"
receiver = "2021ca21f@sigce.edu.in"
password = gp.getpass("Enter your password (2021ca06f@sigce.edu.in): ")

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = sender
email_message['To'] = receiver
email_message['Subject'] = "SMTP HTML e-mail test"

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender, password)

    #sending the email:
    server.sendmail(sender, receiver, email_string)
    

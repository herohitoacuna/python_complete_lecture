# ******************* SENDING EMAIL *********************

# with this Obj we can email message that includes both html and plain text
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib              # server, use for sending email

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"

# use to attach a content to the body of email
message.attach(MIMEText("Body"))
# message.attach(Path("mosh.png").read_bytes())         # Sending image. first we need to convert into binary file


# .SMTP(depends on the server we use)
# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# smtp.close

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()     # use to start the communication between smtp server and client
    smtp.starttls()     # puts the smtp connection in tls mode. TLS(transport layer Security) = use to encrypt all the commands in smtp server
    smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
    smtp.send(message)
    print("Sent...")
# result: Error because the email that we use is not valid anymore

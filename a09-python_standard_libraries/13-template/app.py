# ********************* TEMPLATE ************************
# with this class we can replace the "$" sign in our html
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

template = Template(Path("template.html").read_text)


message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"

# return a string, you can pass a dictionary
body = template.substitute({"name": "John"})
# return a string, or you can pass a keyword argument
body = template.substitute(name="John")
print(body)
# message.attach(MIMEText("Body"))
message.attach(MIMEText(body, "html"))

# message.attach(Path("mosh.png").read_bytes())

# .SMTP(depends on the server we use)
# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# smtp.close

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
    smtp.send(message)
    print("Sent...")

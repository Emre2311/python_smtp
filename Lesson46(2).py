import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smpt_server= "smtp.gmail.com"
sender_email = "elhadyemre@gmail.com"
receiver_email = "fortniteplaystation2311@gmail.com"
password = input("Type your password and press enter: ")
message = MIMEMultipart("alternative")
message["Subject"]="multipart test"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
hello there
I am emre
"""
html = """/
<html>
    <body>
        <h2>HTML MEssage</h2>
            <p>Hi.<br>
                <b>How are you?</b><br>
                <a href="http://ww.realpython.com">Real Python</a>
                has many great tutorials.
            </p>
        </body>
    </html>
"""
            
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

message.attach(part1)
message.attach(part2)
                 
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,message)

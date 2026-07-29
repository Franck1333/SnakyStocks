#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
# ChatGPT / VSC / CoPilot / GithubAi
# https://docs.python.org/3.15/library/email.examples.html#email-examples
#

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

from pathlib import Path 

def send_email(file, sender, recipient):
    # Open the plain text file whose name is in textfile for reading.
    with open(file) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    # sender == the sender's email address
    # recipient == the recipient's email address
    msg['Subject'] = f'The contents of {file}'
    msg['From'] = sender
    msg['To'] = recipient

    # Send the message via Google's SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, 'your_password') # Replace 'your_password' with the actual password or use an app password
    s.send_message(msg)
    s.quit()


if __name__ == "__main__":
    # Example usage
    # send_email('example.txt', 'sender@example.com', 'recipient@example.com')

    file = Path(r"/home/franck/Documents/debian.txt")
    if file.exists():
        print("Fichier trouvé: ", file)

        send_email(file, 'francois.lapresse@gmail.com', 'fun13@live.fr')

    else:
        print("Fichier introuvable: ", file)


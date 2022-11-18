from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

def MailSender(html,title,explanation,receiver=None):
    """
    Mail Sender
    :param mesage: your mesage
    :param alan: if na dont send mesage
    :return: None ()
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = os.getenv("SENDER_EMAIL")
    msg['To'] = receiver
    text = explanation
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    if receiver != None:
        try:
            # server protokol SMTP
            server = smtplib.SMTP("smtp.gmail.com", 587)
            #tls protokol
            server.starttls()
            # host mail host
            server.login(os.getenv("SENDER_EMAIL"),os.getenv("SENDER_PASSWORD"))
            #host mail + target mail + mesage
            server.sendmail(os.getenv("SENDER_EMAIL"), receiver, msg.as_string())
            server.quit()
            return True
        except:
            return False
            # loglama servisi ekelenecek
    else:
        raise "email target is empty"

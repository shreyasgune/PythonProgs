
import smtplib

sender = 'hotlava@grr.la'
receivers = ['shreyas.enug@gmail.com']

message = """From: From Person <hotlava@grr.la>
To: To Person <shreyas.enug@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('smtp.grr.la')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"

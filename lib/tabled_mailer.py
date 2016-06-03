#!/usr/bin/python

"""
author: Jaideep Kekre
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import HTML


def mail_this(listone, chat_id, bucket_list):
    # me == my email address
    # you == recipient's email address
    #Pretty Table creation
    htmlcode = HTML.table(listone, header_row=['Question', 'Response'])
    htmlcode = htmlcode + '<BR>' + HTML.table(bucket_list, header_row=['Disease', 'Fraction'])

    me = "jaideepkekre@gmail.com"
    you = "jaideepkekre@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = str(chat_id)
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = ""
    html = htmlcode

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()
    mail.login('medibotreport', os.environ.get('PASSWORD_MAILER'))
    # mail.sendmail(me, you, msg.as_string())
    mail.sendmail(me, 'jaideepkekre@gmail.com', msg.as_string())
    mail.sendmail(me, 'sameer.deshmukh93@gmail.com', msg.as_string())
    mail.quit()
    print "mail sent"

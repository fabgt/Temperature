#!/usr/bin/python

#Import smtplib for the actual sending function
import smtplib
from getpass import getpass
import sys
import os
import re

#Import the email modules we'll need
from email.mime.text import MIMEText

textfile = open("textfile.txt",'rb')

#Open a plain text file for reading. For this example, assume that
#the text file contains only ASCII characters.
with textfile as fp:
# open("textfile.txt", 'rb') as fp:
	#Create a text/plain message
	msg = MIMEText(fp.read())

#me == sender's email address
#you == the recipient's email address
fromMe='fab.python@yahoo.com'
toYou='fabienclement.desvignes@gmail.com'


msg['Subject']='The contents of %s' %textfile
msg['From']=fromMe
msg['To']=toYou
debuglevel = True

#Define pw
username = str('fab.python@yahoo.com')
passd = getpass('Password for "%s": ' %username)


#Send the message via our own SMTP server, but don't include the 
#envelope header.
try:
	server=smtplib.SMTP('smtp.mail.yahoo.com', 587)
	server.set_debuglevel(debuglevel)
	#server.ehlo()
	server.starttls()
	#server.ehlo()
	server.login(username,passd)
	try:
		server.sendmail(fromMe, toYou, msg.as_string())
	finally:
		server.quit()
		print 'email sent'
except:
	print 'error'
	#sys.exit("mail failed; %s" % "CUSTOM_ERROR")


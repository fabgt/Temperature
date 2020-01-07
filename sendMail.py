#!/usr/bin/python

#Import smtplib for the actual sending function
import smtplib
from getpass import getpass
import sys
import os
import re
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

textfile = open("textfile.txt",'rb')
fileToSend = "TemperatureExtract.xlsx"

msg=MIMEMultipart()

#define sender and recipent
fromMe='fabgt.python@gmail.com'
toYou='fabienclement.desvignes@gmail.com'


msg['Subject']='The contents of log' #%s' %textfile
msg['From']=fromMe
msg['To']=toYou
msg.preamble = "content"
debuglevel = True

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
	ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
	fp = open(fileToSend)
	attachment = MIMEText(fp.read(), _subtype=subtype)
	fp.close()
elif maintype == "image":
	fp = open(fileToSend, "rb")
	attachment = MIMEImage(fp.read(), _subtype=subtype)
	fp.close()
elif maintype == "audio":
	fp = open(fileToSend, "rb")
	attachment = MIMEAudio(fp.read(), _subtype=subtype)
	fp.close()
else:
	fp = open(fileToSend, "rb")
	attachment = MIMEBase(maintype, subtype)
	attachment.set_payload(fp.read())
	fp.close()
	encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment) 

#Add text from file
#with textfile as fp:
#	fp = open("textfile.txt", 'rb')
#msg = MIMEText(fp.read())
#fp.close()

#Define pw
username = str('fabgt.python@gmail.com')
passd = getpass('Password for "%s": ' %username)


#Send the message via our own SMTP server, but don't include the 
#envelope header.
try:
	server=smtplib.SMTP('smtp.gmail.com:587')
	print('server instanciated')
	#server.set_debuglevel(debuglevel)
	server.ehlo()
	server.starttls()
	print('start tls')
	#server.ehlo()
	print(passd)
	print(username)
	server.login(username,passd)
	print('logged in')
	try:
		server.sendmail(fromMe, toYou, msg.as_string())
	finally:
		server.quit()
		print 'email sent'
except:
	print 'error'
	#sys.exit("mail failed; %s" % "CUSTOM_ERROR")


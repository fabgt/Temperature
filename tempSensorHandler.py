#!/usr/bin/python
#Import Libraries
import os
import glob
import datetime
import numpy as np
import httplib
import urllib
import time

#Initialize GPIO Pins
os.system('modprobe w1-gpio') #turns on the gpio module
os.system('modprobe w1-therm') #turns on the temperature module

#Define thingspeak API key
key = "E2TRNT32ZP9DQEG1"

#Find the correct device file that holds the temperature data
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'
device1_file = '/sys/bus/w1/devices/28-0316471d4dff/w1_slave'
device2_file = '/sys/bus/w1/devices/28-03164764a3ff/w1_slave'

#A function that reads the sensors data
def read_temp_raw(device_file):
 f=open(device_file, 'r') #Opens the temperature device file
 lines=f.readlines() #Returns the text
 f.close()
 return lines

#Convert the value of the sensor into a temperature
def read_temp(device_file):
 lines=read_temp_raw(device_file) #Read the temperature 'device file'

 #While the first line does not contain 'YES', wait for 0.2s
 #and then read the device file again.
 while lines[0].strip()[-3:]!='YES':
  time.sleep(0.2)
  lines = read_temp_raw(device_file)

 #Look for the position of the '=' in the second line of the
 #device file.
 equals_pos = lines[1].find('t=')

 #If the '=' is found, convert the rest of the line after the
 #'=' into degrees Celsisu, then degrees Fahrenheit
 if equals_pos != -1:
  temp_string=lines[1][equals_pos+2:]
  temp_c=float(temp_string)/1000.0
  #temp_f=temp_c*9.0/5.0+32.0
  return temp_c #,temp_f

#Print out the temperature until the program is stopped.
with open('textfile.txt','w') as destination:
 print('Temperature being logged.')
 while True:
  time_stamp=str(datetime.datetime.now())
  data1=[time_stamp,read_temp(device1_file)]
  #print(data)
  destination.write('%s\n' % data1)
  temp1 = read_temp(device1_file)
  temp2 = read_temp(device2_file)

  #Send data to thingspeak
  params = urllib.urlencode({'field1':temp1,'field2':temp2,'key':key})
  headers = {"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
  conn = httplib.HTTPConnection("api.thingspeak.com:80")
  try:
    conn.request("POST","/update",params,headers)
    response = conn.getresponse()
    dataResponse = response.read()
    #print temp1,temp2
    #print response.status #,reponse.reason
    conn.close()
  except:
    print "Thingspeak connection failed"
    execfile("sendMail.py")
  #Wait 5 min before sending again
  time.sleep(120)


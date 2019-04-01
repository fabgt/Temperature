#!/usr/bin/python
import xlsxwriter

#Define all functions

def ExtractDateAndTempPosition(stringFromFile):
 "Extract temperature and date positions in string from file"
 #dateStart=0
 #dateEnd=0

 global indexDateMax
 indexDateMax = len(stringFromFile)
 print("indexDateMax: ",indexDateMax)
 for indexDate in range(0, (indexDateMax-1)):
  print(indexDate)
  if stringFromFile[indexDate]=='[':
   global dateStart
   dateStart=indexDate+1
   print("dateStart index is equal to: ", dateStart)
   break
  #else:
   #print("Error in extract dateStart position")

 for indexDateBis in range(0, (indexDateMax-1)):
  if stringFromFile[indexDateBis]==',':
   global dateEnd
   dateEnd=indexDateBis
   print("dateEnd index is equal to: ", dateEnd)
   break
  #else:
   #print("Error in extract dateEnd position")
   #Error

 #Determine temperature first and last character position
 global tempStart
 tempStart=dateEnd+2
 print("tempStart index is equal to: ",tempStart)
 for indexTemp in range(0, (indexDateMax-1)):
  if stringFromFile[indexTemp]==']':
   global tempEnd
   tempEnd=indexTemp-1
   print("tempEnd index is equal to: ",tempEnd)
   break
  #else:
   #Error
   #print("Error in extract temp position")
 #print(dateStart, dateEnd, tempStart, tempEnd)

def ExtractDateAndTemp(stringFromFile,dateStart,dateEnd,tempStart,tempEnd):
 "Determine value of date and temperature"
 global dateRawValue
 dateRawValue=''
 global tempValue
 tempValue=''
 for i in range (dateStart, dateEnd):
  dateRawValue=dateRawValue+stringFromFile[i]
 print("dateRawValue is equal to :",dateRawValue)
 for j in range (tempStart, tempEnd):
  tempValue=tempValue+stringFromFile[j]
 print("tempValue is equal to :",tempValue)
 #return dateRawValue,tempValue

def ConvertRawDateToDate(dateRawValue):
 "Convert Raw Date to readable excel format date"
 global dateValue
 dateValue=dateRawValue

 #return dateValue

def CopyDateAndTempToExcel(columnDate,columnTemp,row,dateValue,tempValue):
 "Copy each date and temperature logged in text file to excel file"
 cellDate=columnDate+str(row)
 cellTemp=columnTemp+str(row)
 worksheet.write(cellDate,dateValue)
 worksheet.write(cellTemp,tempValue)


#MAIN#
#Read lines of text file
#fp=open("textfile.txt",'r')
#data = fp.read()
#fp.close()

columnDate='A'
columnTemp='B'
row=1

dateStart=0
dateEnd=0
tempStart=0
tempEnd=0
dateRawValue=''
dateValue=0
tempValue=''

#Create a new Excel File and add a worksheet
workbook = xlsxwriter.Workbook('TemperatureExtract.xlsx')
worksheet = workbook.add_worksheet('Temperature data')

#Widen the forst column to make the text clearer
worksheet.set_column('A:A', 20)

fp=open("textfile.txt",'r')
line=fp.readline()
print(line)

ExtractDateAndTempPosition(line)
ExtractDateAndTemp(line,dateStart,dateEnd,tempStart,tempEnd)
ConvertRawDateToDate(dateRawValue)
CopyDateAndTempToExcel(columnDate,columnTemp,row,dateValue,tempValue)

while line: #for stringFromFile in data:
  line=fp.readline()
  print(line)
  if line=='':
   print("Enf Of file")
   break
  ExtractDateAndTempPosition(line)
  ExtractDateAndTemp(line,dateStart,dateEnd,tempStart,tempEnd)
  ConvertRawDateToDate(dateRawValue)
  CopyDateAndTempToExcel(columnDate,columnTemp,row,dateValue,tempValue)

  row=row+1
fp.close()
workbook.close()


#bold = workbook.add_format({'bold': True})

#Text with formatting
#worksheet.write('A2', 'World', bold)


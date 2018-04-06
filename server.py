#!/usr/bin/python

import socket
import ast
import re

s = socket.socket()
host = input('Enter the local IP address: ')
port = 3000
s.bind((host,port))
s.listen(5)

p = re.compile('([-]*\d+)\s*([+,-,/,*]+)\s*([-]*\d+)')

while 1:
	c, addr = s.accept()
	message = c.recv(1024).decode('utf-8')

	try:
		if p.match(message):
			message = eval(message)
		else:
			message = 'Invalid syntax: ' + message
	except RegexError as err:
		message = 'Invalid syntax: ' + message

	print(message)
	c.send(str(message).encode('utf-8'))
	c.close()

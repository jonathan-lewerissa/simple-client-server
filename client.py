#!/usr/bin/python

import socket


a = input('Enter an expression: ')

s = socket.socket()
host = input('Enter the server IP address: ')
port = 3000

s.connect((host,port))
s.send(str(a).encode('utf-8'))
print (s.recv(1024).decode('utf-8'))
s.close()

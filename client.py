#!/usr/bin/python

import socket


a = input('Enter an expression: ')

s = socket.socket()
host = input('Enter the server IP address ')
port = 3000

s.connect((host,port))
s.sendto(str(a).encode('utf-8'),host)
print (s.recv(1024).decode('utf-8'))
s.close()
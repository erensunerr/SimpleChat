#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from socket import *
import sys
print("To close type \"close\"")
port = input("PORT = ")
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",int(port)))
print(s.recv(1024).decode("ascii"))
s.send("Connected".encode("utf-8"))
while True:
	a4 = input("Client -> ")
	if a4 =="close":
		print("Closing...")
		s.send("Client requested, closing...".encode("utf-8"))
		sys.exit()
	b1 = str(a4).encode("ascii")
	s.send(b1)
	a5 = s.recv(4096)
	a5 = str(a5.decode("ascii"))
	print("Host -> "+a5)

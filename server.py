# -*- coding: UTF-8 -*-
#!/usr/bin/python3
from socket import *
import sys
import random
s = socket(AF_INET,SOCK_STREAM)
port = random.randint(0,10000)
s.bind(("localhost",port))
s.listen(5)
print("To close type \"close\"")
print("PORT = "+str(port))
while True:
	c,a = s.accept()
	c.send("Connected".encode("ascii"))
	print(c.recv(1024).decode("utf-8"))
	while True:
		a4 = input("Host -> ")
		if a4 == "close":
			print("Closing...")
			c.send("Server requested, Closing...".encode("ascii"))
			sys.exit()
		b1 = str(a4).encode("ascii")
		c.send(b1)
		a5 = c.recv(4096)
		a5 = str(a5.decode("utf-8"))
		print("Client -> "+a5)
			


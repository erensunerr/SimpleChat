import socket, time, random, threading,sys



def receive():
	global s, hostConnect
	while True:
			data = s.recv(1024)
			if data:
				print("\n{0} -> {1}".format(hostConnect,data.decode('ascii')))


def send():
	global s
	while True:
		time.sleep(1)
		MyInput = input("Me ->")
		if MyInput:
			if MyInput == '!quit':
				sys.exit(0)

			else:
				s.send(MyInput.encode('ascii'))




port = int(input("Port -> "))
hostConnect = "192.168.0.23"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hostConnect,port))
T_Receive = threading.Thread(target=receive)
T_Send = threading.Thread(target=send)
T_Receive.start()
T_Send.start()

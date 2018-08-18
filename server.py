import socket, sys, random, threading, time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '192.168.0.23'
port = random.randint(1000,9999)
print("Port: {}".format(port))
s.bind((host,port))
s.listen(1)
cs, caddr = s.accept()
print("{} just appeared.".format(caddr[0]))

def send():
    global s
    while True:
        time.sleep(1)
        myInput = input("Me -> ")
        f = open("a.py",'r').read()
        for line in f:
        if myInput:
            if myInput == '!quit':
                sys.exit(0)
            else:
            cs.send(myInput.encode('ascii'))


def receive():
    global s, caddr
    while True:
        time.sleep(1)
        data = cs.recv(1024)
        if data:
            print("\n{0} -> {1}".format(caddr[0],data.decode('ascii')))

T_receive = threading.Thread(target=receive)
T_send = threading.Thread(target=send)
T_receive.start()
T_send.start()

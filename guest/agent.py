# Echo server program
import socket
import subprocess

HOST = ''                   # Symbolic name meaning all available interfaces
PORT = 7474              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print "Catch me if you CAN"
while 1:
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    data = conn.recv(1024)
    conn.sendall(data)
    print "What ? :"+str(data)

conn.close()
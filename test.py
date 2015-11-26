import time
import socket
from util import log
 
HOST='127.0.0.1' #localhost
PORT=7474
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while(1):
    try:
        time.sleep(0.5)
        s.connect((HOST,PORT))
        log.log_yellow("VM wake up")
        s.send(b'malware-upload')
        data=s.recv(1024)
        s.close()
        break
    except:
        print "wait"




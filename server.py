from util.color import bcolors
from util.intro import intro
from process import kvm
import os
import socket
import time
import glob
from ConfigParser  import ConfigParser
from util import log
import subprocess
_current_dir = os.path.abspath(os.path.dirname(__file__))
IYCFM_ROOT = os.path.normpath(os.path.join(_current_dir, "."))
config = ConfigParser()
RootDir_conf = IYCFM_ROOT
RootDir_conf += '/conf/cmc.conf'
config.read(RootDir_conf)

VM_IP=config.get("VM","ip")
intro()


log.log_yellow("CMIYC Server Start")

while 1:
    up_check = glob.glob('malware/*')
    if len(up_check)>0:
        kvm.vm_start()
        break
subprocess.check_output("rm malware/*",shell=True)





HOST=VM_IP #localhost
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


kvm.vm_shutdown()
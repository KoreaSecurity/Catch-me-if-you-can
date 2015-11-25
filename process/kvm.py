import os,sys,subprocess
from ConfigParser  import ConfigParser
from util import log

_current_dir = os.path.abspath(os.path.dirname(__file__))
IYCFM_ROOT = os.path.normpath(os.path.join(_current_dir, ".."))
config = ConfigParser()
RootDir_conf = IYCFM_ROOT
RootDir_conf += '/conf/cmc.conf'
print str(IYCFM_ROOT)
config.read(RootDir_conf)
VM_NAME=config.get("VM","name")

def vm_start():
    cmd="virsh snapshot-revert --domain "+str(VM_NAME)+" --current"
    subprocess.check_output(cmd,shell=True)
    message="#Start VM NAME: "+str(VM_NAME)
    log.log_yellow(message)



def vm_shutdown():
    cmd="virsh destroy --domain "+str(VM_NAME)
    subprocess.check_output(cmd,shell=True)
    message="#Shut Down VM NAME: "+str(VM_NAME)
    log.log_yellow(message)

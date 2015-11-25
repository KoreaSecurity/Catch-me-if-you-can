from util.color import bcolors
from util.intro import intro
from process import kvm
import os

intro()


kvm.vm_start()
kvm.vm_shutdown()



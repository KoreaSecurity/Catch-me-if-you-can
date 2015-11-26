import sys
import os

if len(sys.argv) is 1:
  print "Usage : python upload.py MalwareName"

else:
    malware=str(sys.argv[1])
    if(os.path.exists(malware)):
        cmd="cp "+malware+" malware"
        os.system(cmd)
        print "File name :"+malware+" ---- Analysis.. start"
    else:
        print "Not files..."




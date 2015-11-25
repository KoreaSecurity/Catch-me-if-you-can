import datetime
from util.color import bcolors


def log_red(message):
    print bcolors.Red + str(get__time())+" "+str(message) + bcolors.White

def log_yellow(message):
    print bcolors.Yellow + str(get__time())+" "+str(message) + bcolors.White

def log_green(message):
    print bcolors.Green + str(get__time())+" "+str(message) + bcolors.White


def get__time():

    now = datetime.datetime.now()
    logtime = "["+str(now)+"]"
    return logtime
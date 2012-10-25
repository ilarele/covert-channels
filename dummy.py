#!/usr/bin/python
import os
from subprocess import Popen

def start():
    cmd_str = "./dummy_proc_consummer.py"
    for i in range(4):
        Popen([cmd_str], shell=True,
                  stdin=None, stdout=None, stderr=None, close_fds=True)



def stop():
    os.system("kill $(ps aux | grep ./dummy_proc_consummer.py | awk '{ print $2 }') 2> log.txt")
    


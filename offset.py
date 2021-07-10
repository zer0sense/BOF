#!/usr/bin/python
import sys, socket

ip = ''
port=
command = "TRUN /.:/"
offset =""

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send((command + offset))
        s.close()

except:
        print "Error Connecting to Server"
        sys.exit()
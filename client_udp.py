#!/usr/bin/env python
#coding:utf-8


import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Maichn', b'aaa', b'cccc']:
    client.sendto(data, ('192.168.1.101',9999))
    print(client.recv(1024).decode('utf-8'))
client.close()


#!/usr/bin/env python
#coding:utf-8

import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
print(client.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Salary']:
    client.send(data)
    print(client.recv(1024).decode('utf-8'))
client.send(b'exit')
client.close()

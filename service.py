#!/usr/bin/env python
#coding:utf-8

import socket
import threading, time

def tcplink(socket, addr):
    print('Accept new connection from %s:%s...' % addr)
    socket.send(b'welcom')
    while True:
        data = socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        socket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    socket.close()
    print('Connect from %s:%s closed.' % addr)
    


service = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 监听端口：
service.bind(('127.0.0.1',9999))
# 监听端口
service.listen(5)
print('Waiting for connection...')

while True:
    # 接收一个新的连接
    socket, addr = service.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink,args=(socket,addr))
    t.start()


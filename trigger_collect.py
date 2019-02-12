#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-
# auth: zhoujunke
# date: 20190212

# command: trigger, update 
#       trigger: all host start hw info collect and post the data to API server
#       update:  all host update the script on host

# crypto : data(base64) ^ data(md5) + data(md5)

import cryptolib
import socket
import time
import Queue
import threading

# config
hostlistfile = 'host.txt'
port = 63001
apiserver = '192.168.146.131'
apiserverport = 5000
command = 'trigger'
updateurl = ''

nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
data = apiserver + '|' + str(apiserverport) + '|' + command + '|' + updateurl + '|' + nowtime 

cryptodata = cryptolib.encryptdata(data)

queue = Queue.Queue() 

def socketTrigger(host,port):
    s = socket.socket()
    s.connect((host, port))
    s.send(cryptodata.encode('utf8'))
    print s.recv(1024).decode(encoding='utf8')
    s.close()


with open(hostlistfile, 'r') as f:
    for host in f.readlines():
        queue.put(host, True, None)


for i in range(20):
    t = threading.Thread(target=socket, args=())
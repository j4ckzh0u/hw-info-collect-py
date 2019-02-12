#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-
# auth: zhoujunke
# date: 20190212

# command: trigger, update 
#       trigger: all host start hw info collect and post the data to API server
#       update:  all host update the script on host

# crypto : data(base64) ^ data(md5) + data(md5)
# data = apiserver + '|' + str(apiserverport) + '|' + command + '|' + updateurl + '|' + nowtime 

import cryptolib
import time
import os
import urllib2
import sys

#data = raw_input()
data = sys.stdin.readline()
# print "data1: " + data

try:
    data = cryptolib.decryptdata(data.split('\n')[0])
    # print "data2: " + data
    apiserver = data.split('|')[0]
    apiserverport = data.split('|')[1]
    command = data.split('|')[2]
    updateurl = data.split('|')[3]
except:
    print 'data is error!!!'
    sys.exit()

print 'APIServer: ', apiserver
print 'APIServerPort: ', apiserverport
print 'Command: ', command

if command == 'trigger':
    os.system("python /root/py_code/salt_get_hwinfo.py")
    print 'command exec success!'
elif command == 'update':
    with open("/root/py_code/salt_get_hwinfo.py", 'wb') as f:
        d = urllib2.urlopen(updateurl)
        data = d.read()
        f.write(data)
    print 'script update success'



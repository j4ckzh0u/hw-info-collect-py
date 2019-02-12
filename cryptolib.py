#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-
# auth: zhoujunke
# date: 20190212

# command: trigger, update 
#       trigger: all host start hw info collect and post the data to API server
#       update:  all host update the script on host

# crypto data : data(base64) xor data(md5) + data(md5)

import base64 as b64
import hashlib

### encrypt: first xor with key ,2nd base64
def xor_encrypt(data,key):
    ldata=len(data)
    lkey=len(key)
    secret=[]
    num=0
    for each in data:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    return b64.b64encode( "".join( secret ).encode() ).decode()

### decrypt: first decode base64 ,2nd xor with key
def xor_decrypt(secret,key):
    data = b64.b64decode( secret.encode() ).decode()
    ldata=len(data)
    lkey=len(key)
    secret=[]
    num=0
    for each in data:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    return "".join( secret )
### get data md5 hexdigest
def md5(data):
    m = hashlib.md5()
    m.update(data)
    md5digest = m.hexdigest()
    return md5digest


def encryptdata(data):
    md5digest = md5(data)
    datatmp = xor_encrypt(data, md5digest)
    data = datatmp + md5(data)
    return data

def decryptdata(data):
    md5digest = data[-32:]
    datalen = len(data) - 32
    datatmp = data[0:datalen]
    data = xor_decrypt(datatmp, md5digest)
    if md5(data) == md5digest:
        return data
    else:
        print 'data is error'
        return ''





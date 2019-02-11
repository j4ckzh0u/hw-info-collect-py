#! /usr/bin/env python2.7
# -*- coding: gbk -*_
# -*- coding: utf-8 -*-
# this script is use saltstack get hardware info.
# eg. CPU/MEM/HardDisk/serverNO..
# auth: jackzhou
# data: 2019-01-31

import salt.config
import salt.loader
import salt.modules.smbios as __smbios__
import salt.modules.disk as __disk__
import psutil
import copy
import json
import requests

minionConfig='/etc/salt/minion'
server='http://192.168.146.131:5000/hwinfo'

__opts__ = salt.config.minion_config(minionConfig)
__grains__ = salt.loader.grains(__opts__)

allIPv4   =  __grains__['ipv4']
ipGateway =  __grains__['ip4_gw']
allinterIp   =  __grains__['ip4_interfaces']
allInter  =  __grains__['hwaddr_interfaces']
hostName  =  __grains__['fqdn']
cpuModel  =  __grains__['cpu_model']
cpuArch   =  __grains__['cpuarch']
cpusoltNum = psutil.cpu_count(logical=False)
logiccpuNum = __grains__['num_cpus']
gpuModel  =  __grains__['gpus'][0]
gpuNum    =  __grains__['num_gpus']
memTotal  =  __grains__['mem_total']
diskList  =  __grains__['disks']
osType    =  __grains__['os']
osFamily  =  __grains__['os_family']
osArch    =  __grains__['osarch']
osRelease =  __grains__['osrelease']
kernelRelease = __grains__['kernelrelease']
serverProduct = __grains__['productname']
serverFacturer = __grains__['manufacturer']
serverSerialnum = __grains__['serialnumber']
serverId   = __grains__['server_id']
machineId  = __grains__['machine_id']
isVirtual  = __grains__['virtual']
basebordManufacturer = __smbios__.get('baseboard-manufacturer')
basebordNamd = __smbios__.get('baseboard-product-name')
basebordSerialnum = __smbios__.get('baseboard-serial-number')

#get disk id eg. sda sdb
diskList2 = []
filterdisk = ['sr','cd','dvd','dm','ram','loop']
for disk in diskList:    
    if not any(disk.startswith(keyfilter) for keyfilter in filterdisk):
        diskList2.append(disk)

#main IP 
mainIP={}
for eth in allinterIp.keys():
    if allinterIp[eth]:
            if cmp(ipGateway.split('.')[0:3], allinterIp[eth][0].split('.')[0:3]) == 0:
                    mainIP['mainEth']=eth
                    mainIP['mainIp']=allinterIp[eth][0]

#disk part size
tmplist = {}
partlist = {}
for part in psutil.disk_partitions():
    tmplist['device'] = part[0]
    tmplist['mountpoint'] = part[1]
    tmplist['fstype'] = part[2]
    partlist[part[1]]=copy.deepcopy(tmplist)

for part in partlist.keys():
    partlist[part]['total'] = psutil.disk_usage(part)[0]
    partlist[part]['Used'] = psutil.disk_usage(part)[1]
    partlist[part]['free'] = psutil.disk_usage(part)[2]
    partlist[part]['percent'] = psutil.disk_usage(part)[3]


#cpu pinpao

info=mainIP['mainIp'],mainIP['mainEth'],allinterIp,ipGateway,allInter,hostName,cpuModel,cpuArch,cpusoltNum,logiccpuNum,gpuModel,gpuNum,memTotal,diskList2,partlist,basebordManufacturer,basebordNamd,basebordSerialnum,osType,osFamily,osArch,osRelease,kernelRelease,serverProduct,serverFacturer,serverSerialnum,serverId,machineId,isVirtual

#print info
data = {}
data['data'] = info

# datap = urllib.urlencode(data)
req = requests.post(server, data=json.dumps(data))
print req.text

#! /usr/bin/env python2.7
from flask import Flask
from flask import request
from flask_script import Manager
import time
import json
import pymysql

#flask app
app = Flask(__name__)
manager = Manager(app)

#mysql db
mysqlserver = '127.0.0.1'
mysqlport = 3306
mysqluser = 'root'
mysqlpasswd = 'root'
mysqldatabase = 'hw_info'

conn = pymysql.connect(mysqlserver, mysqluser, mysqlpasswd, mysqldatabase, mysqlport, charset='utf8', use_unicode=True)
try:
    conn.ping()
    cursor = conn.cursor()
    msg = "Mysql DB connect Success !!!"
except:
    msg = "Mysql DB connect Error !!!"
    conn.close()
    exit()
# finally:
#     cursor.close()
#     conn.close()



# inster data
def execsql(data):
    ip = data[0]
    countsql= 'select * from server_hw_info where mainIP = "%s"' % ip
    # print countsql
    row_num = cursor.execute(countsql)
    # print row_num
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if row_num:
        sql = 'update server_hw_info set mainEth = "%s", allIPv4 = "%s", ipGateway = "%s", allInter = "%s", hostName = "%s", cpuModel = "%s", cpuArch = "%s", cpusoltNum = "%s", logiccpuNum = "%s", gpuModel = "%s", gpuNum = "%s", memTotal = "%s", diskList = "%s", partsize = "%s", basebordManufacturer = "%s", basebordName = "%s", basebordSerialnum = "%s", osType = "%s", osFamily = "%s", osArch = "%s", osRelease = "%s", kernelRelease = "%s", serverProduct = "%s", serverFacturer = "%s", serverSerialnum = "%s", serverId = "%s", machineId = "%s", isVirtual = "%s", time = "%s" where mainIP = "%s"' % (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], nowtime, data[0])        
    else:
        sql = 'insert into server_hw_info (mainIP, mainEth, allIPv4, ipGateway, allInter, hostName, cpuModel, cpuArch, cpusoltNum, logiccpuNum, gpuModel, gpuNum, memTotal, diskList, partsize, basebordManufacturer, basebordName, basebordSerialnum, osType, osFamily, osArch, osRelease, kernelRelease, serverProduct, serverFacturer, serverSerialnum, serverId, machineId, isVirtual,time) values ( "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s" )' % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], nowtime)
    # sql = 'insert into server_hw_info (mainIP, mainEth, allIPv4, ipGateway, allInter, hostName, cpuModel, cpuArch, cpusoltNum, logiccpuNum, gpuModel, gpuNum, memTotal, diskList, partsize, basebordManufacturer, basebordName, basebordSerialnum, osType, osFamily, osArch, osRelease, kernelRelease, serverProduct, serverFacturer, serverSerialnum, serverId, machineId, isVirtual) values ( "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s" )' % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28])
    print sql
    return sql

@app.route('/')
def index():
    return '''
	<!doctype html>
	<title>status Info</title>
	<h1>Server: Running .... </h1><br>
    <h1>DB: %s </h1>
	''' % msg

@app.route('/hwinfo',methods = ['GET','POST'])
def hwinfo():
    if request.method == 'POST':
        content = request.data
        # print content
        data = json.loads(content)['data']
        filename = str(data[0]) + '_' + str(nowtime)
        try:
            conn.ping(reconnect=True)
            sql = execsql(data)
            cursor.execute(sql)
            conn.commit()
            print 'SQL exec success!'
        except:
            conn.rollback()
            print 'SQL exec fail, rollback!'
        with open(str(filename)+".json", "w") as f:
            f.write(content)
            f.close()
        return "Success!"
    return '''
	<!doctype html>
        <title>Info</title>
        <h1>server is running</hi>
	'''
if __name__ == "__main__":
#    app.run(debug=True)
    manager.run()

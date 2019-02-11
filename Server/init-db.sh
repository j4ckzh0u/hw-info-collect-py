#! /usr/bin/env sh
# start flask web app
# auth: zhoujk
# date: 20190211

# mysql env:
# MYSQL_ROOT_PASSWORD
# MYSQL_DATABASE
# MYSQL_USER
# MYSQL_PASSWORD
# MYSQL_ALLOW_EMPTY_PASSWORD
# MYSQL_RANDOM_ROOT_PASSWORD
# MYSQL_ONETIME_PASSWORD

MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD:-TGBIJN<><;<}
MYSQL_DATABASE=${MYSQL_DATABASE:-hw_info}
MYSQL_USER=${MYSQL_USER:-mysqluser}
MYSQL_PASSWORD=${MYSQL_PASSWORD:-WDFUHCJKIHN>><<?#@}

# test db is exist.
# `mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "use ${MYSQL_DATABASE}"`
# result=`echo $?`
# print ${result}

#create db
createsql="\
    CREATE DATABASE ${MYSQL_DATABASE};
    USE ${MYSQL_DATABASE};
    GRANT ALL ON ${MYSQL_DATABASE}.'*' TO ${MYSQL_USER}@'%' identified by ${MYSQL_PASSWORD} 
    CREATE TABLE server_hw_info ( mainIP  varchar(32), mainEth  varchar(32), allIPv4  varchar(1024), ipGateway  varchar(32), allInter  varchar(1024), hostName  varchar(255), cpuModel  varchar(255), cpuArch  varchar(255), cpusoltNum varchar(255), logiccpuNum  varchar(255), gpuModel  varchar(255), gpuNum  varchar(255), memTotal  varchar(512), diskList  varchar(512), partsize  varchar(4096), basebordManufacturer  varchar(255) , basebordName  varchar(255), basebordSerialnum  varchar(255), osType  varchar(32) , osFamily  varchar(32) , osArch  varchar(32) , osRelease  varchar(32), kernelRelease  varchar(64), serverProduct  varchar(64), serverFacturer  varchar(64), serverSerialnum  varchar(64), serverId  varchar(64), machineId  varchar(64), isVirtual  varchar(32), time varchar(32) );
    "
if [ ${result} -eq 0 ]; then
    echo "database is exist"
else;
    mysql -
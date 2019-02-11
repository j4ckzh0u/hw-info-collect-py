# hw-info-collect-py

## 硬件信息收集

> 使用saltstack 客户端
>
> repo中包含了saltstack的minion的安装包，ver 2018.3.3.1

收集的信息如下：

#主机IP,主网卡,所有IP地址,网关,所有网卡+MAC地址,主机名,[CPU品牌,CPU类型],CPU型号,[CPU主频],CPU架构,物理CPU个数,逻辑CPU个数,GPU类型,GPU个数,内存大小(MB),硬盘位,硬盘分区,主板厂家,主板型号,主板序列号,OS类型,系统厂家,OS架构,OS版本,内核版本,服务器型号,服务器厂家,服务器序列号,服务识别号,服务器ID,是否为虚拟机,收集时间

##  mysql 表

CREATE TABLE  server_hw_info ( mainIP  varchar(32), mainEth  varchar(32), allIPv4  varchar(1024), ipGateway  varchar(32), allInter  varchar(1024), hostName  varchar(255), cpuModel  varchar(255), cpuArch  varchar(255), cpusoltNum varchar(255), logiccpuNum  varchar(255), gpuModel  varchar(255), gpuNum  varchar(255), memTotal  varchar(512), diskList  varchar(512), partsize  varchar(4096), basebordManufacturer  varchar(255) , basebordName  varchar(255), basebordSerialnum  varchar(255), osType  varchar(32) , osFamily  varchar(32) , osArch  varchar(32) , osRelease  varchar(32), kernelRelease  varchar(64), serverProduct  varchar(64), serverFacturer  varchar(64), serverSerialnum  varchar(64), serverId  varchar(64), machineId  varchar(64), isVirtual  varchar(32), time varchar(32) );






-- MySQL dump 10.13  Distrib 5.6.43, for Linux (x86_64)
--
-- Host: localhost    Database: hw_info
-- ------------------------------------------------------
-- Server version	5.6.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `server_hw_info`
--

DROP TABLE IF EXISTS `server_hw_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_hw_info` (
  `mainIP` varchar(32) DEFAULT NULL,
  `mainEth` varchar(32) DEFAULT NULL,
  `allIPv4` varchar(1024) DEFAULT NULL,
  `ipGateway` varchar(32) DEFAULT NULL,
  `allInter` varchar(1024) DEFAULT NULL,
  `hostName` varchar(255) DEFAULT NULL,
  `cpuModel` varchar(255) DEFAULT NULL,
  `cpuArch` varchar(255) DEFAULT NULL,
  `cpusoltNum` varchar(255) DEFAULT NULL,
  `logiccpuNum` varchar(255) DEFAULT NULL,
  `gpuModel` varchar(255) DEFAULT NULL,
  `gpuNum` varchar(255) DEFAULT NULL,
  `memTotal` varchar(512) DEFAULT NULL,
  `diskList` varchar(512) DEFAULT NULL,
  `partsize` varchar(4096) DEFAULT NULL,
  `basebordManufacturer` varchar(255) DEFAULT NULL,
  `basebordName` varchar(255) DEFAULT NULL,
  `basebordSerialnum` varchar(255) DEFAULT NULL,
  `osType` varchar(32) DEFAULT NULL,
  `osFamily` varchar(32) DEFAULT NULL,
  `osArch` varchar(32) DEFAULT NULL,
  `osRelease` varchar(32) DEFAULT NULL,
  `kernelRelease` varchar(64) DEFAULT NULL,
  `serverProduct` varchar(64) DEFAULT NULL,
  `serverFacturer` varchar(64) DEFAULT NULL,
  `serverSerialnum` varchar(64) DEFAULT NULL,
  `serverId` varchar(64) DEFAULT NULL,
  `machineId` varchar(64) DEFAULT NULL,
  `isVirtual` varchar(32) DEFAULT NULL,
  `time` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server_hw_info`
--

-- LOCK TABLES `server_hw_info` WRITE;
-- /*!40000 ALTER TABLE `server_hw_info` DISABLE KEYS */;
-- INSERT INTO `server_hw_info` VALUES ('192.168.146.136','eth0','{u\'lo\': [u\'127.0.0.1\'], u\'eth0\': [u\'192.168.146.136\']}','192.168.146.2','{u\'lo\': u\'00:00:00:00:00:00\', u\'eth0\': u\'00:0c:29:7d:60:7f\'}','localhost.localdomain','Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz','x86_64','2','2','{u\'model\': u\'SVGA II Adapter\', u\'vendor\': u\'unknown\'}','1','1860','[u\'sda\']','{u\'/boot\': {u\'Used\': 41772032, u\'percent\': 8.8, u\'free\': 431369216, u\'fstype\': u\'ext4\', u\'device\': u\'/dev/sda1\', u\'mountpoint\': u\'/boot\', u\'total\': 499355648}, u\'/\': {u\'Used\': 2521272320, u\'percent\': 5.5, u\'free\': 43091939328, u\'fstype\': u\'ext4\', u\'device\': u\'/dev/mapper/VolGroup-lv_root\', u\'mountpoint\': u\'/\', u\'total\': 48061423616}}','Intel Corporation','440BX Desktop Reference Platform','None','CentOS','RedHat','x86_64','6.10','2.6.32-754.el6.x86_64','VMware Virtual Platform','VMware, Inc.','VMware-56 4d 64 a8 a8 d5 f6 be-a0 7a 6d 77 d8 7d 60 7f','1732821699','c1e02265ec1ff51441b04d5400000007','VMware','2019-02-10 00:26:45'),('192.168.146.131','ens33','{u\'lo\': [u\'127.0.0.1\'], u\'docker0\': [u\'172.17.0.1\'], u\'veth6704cac\': [], u\'ens33\': [u\'192.168.146.131\']}','192.168.146.2','{u\'lo\': u\'00:00:00:00:00:00\', u\'docker0\': u\'02:42:c6:ee:8c:d4\', u\'veth6704cac\': u\'aa:f4:9d:d7:b3:93\', u\'ens33\': u\'00:0c:29:2c:ae:25\'}','localhost.localdomain','Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz','x86_64','2','4','{u\'model\': u\'SVGA II Adapter\', u\'vendor\': u\'unknown\'}','1','1823','[u\'sda\']','{u\'/var/lib/docker/overlay2\': {u\'Used\': 7218229248, u\'percent\': 18.2, u\'free\': 32482435072, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/mapper/centos-root\', u\'mountpoint\': u\'/var/lib/docker/overlay2\', u\'total\': 39700664320}, u\'/boot\': {u\'Used\': 149258240, u\'percent\': 14.0, u\'free\': 913997824, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/sda1\', u\'mountpoint\': u\'/boot\', u\'total\': 1063256064}, u\'/var/lib/docker/containers\': {u\'Used\': 7218229248, u\'percent\': 18.2, u\'free\': 32482435072, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/mapper/centos-root\', u\'mountpoint\': u\'/var/lib/docker/containers\', u\'total\': 39700664320}, u\'/\': {u\'Used\': 7218229248, u\'percent\': 18.2, u\'free\': 32482435072, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/mapper/centos-root\', u\'mountpoint\': u\'/\', u\'total\': 39700664320}}','Intel Corporation','440BX Desktop Reference Platform','None','CentOS','RedHat','x86_64','7.4.1708','3.10.0-693.el7.x86_64','VMware Virtual Platform','VMware, Inc.','VMware-56 4d c2 b5 bf 7a e5 a2-e2 34 6f d9 90 2c ae 25','531551915','9b7e0d190f264f4386f362cb76acf3a5','VMware','2019-02-11 11:38:24'),('192.168.146.128','ens33','{u\'lo\': [u\'127.0.0.1\'], u\'docker0\': [u\'172.17.0.1\'], u\'ens33\': [u\'192.168.146.128\']}','192.168.146.2','{u\'lo\': u\'00:00:00:00:00:00\', u\'docker0\': u\'02:42:e0:88:7d:37\', u\'ens33\': u\'00:0c:29:df:50:80\'}','ctfhost','Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz','x86_64','2','2','{u\'model\': u\'SVGA II Adapter\', u\'vendor\': u\'unknown\'}','1','1823','[u\'sda\']','{u\'/boot\': {u\'Used\': 149258240, u\'percent\': 14.0, u\'free\': 913997824, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/sda1\', u\'mountpoint\': u\'/boot\', u\'total\': 1063256064}, u\'/\': {u\'Used\': 5096951808, u\'percent\': 12.8, u\'free\': 34603712512, u\'fstype\': u\'xfs\', u\'device\': u\'/dev/mapper/centos-root\', u\'mountpoint\': u\'/\', u\'total\': 39700664320}}','Intel Corporation','440BX Desktop Reference Platform','None','CentOS','RedHat','x86_64','7.4.1708','3.10.0-693.el7.x86_64','VMware Virtual Platform','VMware, Inc.','VMware-56 4d aa 81 23 a1 7d aa-4a b4 e6 25 8e df 50 80','800777096','9b7e0d190f264f4386f362cb76acf3a5','VMware','2019-02-10 00:27:24');
-- /*!40000 ALTER TABLE `server_hw_info` ENABLE KEYS */;
-- UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-11  6:36:42

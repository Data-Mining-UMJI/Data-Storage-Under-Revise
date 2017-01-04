# Hadoop-MongoDB

## Version

* Hadoop: v2.7.3-stable (have been renamed as hadoop in this computer for convinience)
* MongoDB: v3.4.1

## Config

* Hadoop: 
 - add "export PATH=$PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin" to ~/.bashrc
 - source ~/.bashrc

* Procedures to reset the hdfs (hadoop file system):
 - ./stop.sh
 - ./reformat.sh under Peng-System
 - ./reformat.sh under wanglab-ThinkPad-T440
 - ./format.sh
 - ./start.sh

* Check the status of hdfs:
 - ./check_status.sh

## Reference

* Hadoop setup: 
 - http://www.powerxing.com/install-hadoop/
* Hadoop Replica Set setup: 
 - http://www.powerxing.com/install-hadoop-cluster/
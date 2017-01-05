# Hadoop-MongoDB

## Version

* Hadoop: v2.7.3-stable (have been renamed as hadoop in Peng-System for convinience)
* MongoDB: v3.4.1
* MongoDB-driver (java): v3.4.1
* MongoDB-Hadoop Connector: v2.0.1

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

* Notice:
 - YARN is closed currently, and need to modified *yarn-site.xml* to enable it, which is good for the Cluster with multiple servers.

## Current Problems:
 
* Where:
Script '/home/hadoop/Desktop/mongo-hadoop/gradle/hadoop.gradle' line: 213

* What went wrong:
Execution failed for task ':historicalYield'.
> Process 'command '/home/hadoop/Desktop/mongo-hadoop/hadoop-binaries/hadoop-2.7.2/bin/hadoop'' finished with non-zero exit value 1


## Reference

* Hadoop setup: 
 - http://www.powerxing.com/install-hadoop/
* Hadoop Cluster setup: 
 - http://www.powerxing.com/install-hadoop-cluster/
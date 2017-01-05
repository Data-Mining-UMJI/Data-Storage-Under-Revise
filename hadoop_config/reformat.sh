#! /bin/bash

cd /usr/local

# Delete Hadoop temporary files
sudo rm -r ./hadoop/tmp
# Delete log files
sudo rm -r ./hadoop/logs/*

tar -zcf ~/hadoop.master.tar.gz ./hadoop
cd ~
# scp ./hadoop.master.tar.gz wanglab-ThinkPad-T440:/home/hadoop
scp ./hadoop.master.tar.gz walden-PU450CD:/home/hadoop
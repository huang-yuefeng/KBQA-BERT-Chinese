#!/bin/bash

chown -R mysql:mysql /var/lib/mysql
service mysql start
source /home/huangyf/anaconda2/bin/activate tf1.13
export PATH=/home/huangyf/anaconda2/bin:$PATH
su - huangyf -c 'cd /home/huangyf/work/flask && /home/huangyf/anaconda2/envs/tf1.13/bin/python kbqa.py'
echo 'init finished'

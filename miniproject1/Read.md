# Hadoop Project Report

## Hadoop cluster setup

/etc/hosts

```hosts
192.241.155.216 node-master
157.230.219.210 node1
157.230.219.201 node2
```



~/.profile

```bash
...
export HADOOP_HOME=/home/student/hadoop

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HDFS_NAMENODE_USER=student
export HDFS_DATANODE_USER=student
export HDFS_SECONDARYNAMENODE_USER=student
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
```



### ~/hadoop/etc/hadoop/core-site.xml

跟集群有关的配置，设置了文件系统的url

```xml
<configuration>
   <property>
     <name>fs.defaultFS</name>
     <value>hdfs://node-master:9000</value>
   </property>
</configuration>
```

### ~/hadoop/etc/hadoop/yarn-site.xml

配置资源管理

```xml
<configuration>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>node-master</value>
  </property>

  <property>
     <name>yarn.nodemanager.aux-services</name>
     <value>mapreduce_shuffle</value>
   </property>

  <property>
     <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
     <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>

  <property>
     <name>yarn.application.classpath</name>
     <value>
	     $HADOOP_CONF_DIR,${HADOOP_COMMON_HOME}/share/hadoop/common/*,
	     ${HADOOP_COMMON_HOME}/share/hadoop/common/lib/*,
	     ${HADOOP_HDFS_HOME}/share/hadoop/hdfs/*,
	     ${HADOOP_HDFS_HOME}/share/hadoop/hdfs/lib/*,
	     ${HADOOP_MAPRED_HOME}/share/hadoop/mapreduce/*,
	     ${HADOOP_MAPRED_HOME}/share/hadoop/mapreduce/lib/*,
	     ${HADOOP_YARN_HOME}/share/hadoop/yarn/*,
	     ${HADOOP_YARN_HOME}/share/hadoop/yarn/lib/*
     </value>
  </property>

</configuration>
```



~/hadoop/etc/hadoop/

配置一些mr参数

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>

  <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=/home/student/hadoop</value>
  </property>
  <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=/home/student/hadoop</value>
  </property>
  <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=/home/student/hadoop</value>
  </property>
</configuration>
```



~/hadoop/etc/hadoop/hdfs-site.xml

```xml
<configuration>
    <property>
      <name>dfs.replication</name>
      <value>2</value>
    </property>
    <property>
      <name>dfs.namenode.name.dir</name>
      <value>file:///home/student/hdfs/namenode</value>
    </property>
    <property>
      <name>dfs.datanode.data.dir</name>
      <value>file:///home/student/hdfs/datanode</value>
    </property>
</configuration>
```



## Hadoop security Setting:

I restricted all public IPs to access 3 servers. Only one ip from my own Was Virtual Machine is allowed to log into name node  through ssh. And 3 servers can access to each other



## Part 2 Docker

The way to test docker file 

```bash
docker build -t my-hadoop .
docker run -p 8088:8088 --name my-hadoop-container -d my-hadoop
docker exec -it my-hadoop-container bash

```

After login into the docker, test 

```bash
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.0.jar pi 2 5
```

We will get 

```bash
......
Job Finished in 24.857 seconds
Estimated value of Pi is 3.60000000000000000000
```



## Part 3 testing method

An n-gram of size 1 is referred to as a "unigram"; size 2 is a "bigram" (or, less commonly, a
"digram"); size 3 is a "trigram". 

The number **n** should be added after mapper.py. For example, when number n is 2

```bash
student@CC-PM-34:~$ echo "helllleoeold" > q3.txt
```

```bash
student@CC-PM-34:~$ hadoop jar hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file mapper.py -mapper 'mapper.py 2' -file reducer.py -reducer reducer.py -input q3.txt -output q3out3
```

```bash
student@CC-PM-34:~$ hdfs dfs -cat q3out3/part-00000
el	1
eo	2
he	1
ld	1
le	1
ll	3
oe	1
ol	1
```



## Part 4 testing method

1. How many hits were made to the website item “/assets/img/home-logo.png”?

   ```bash
   student@CC-PM-34:~$ hadoop jar hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file minipj/mapper_req.py -mapper mapper_req.py -file minipj/reducer_req.py -reducer reducer_req.py -input access_log -output req3
   ```

   ```bash
   student@CC-PM-34:~/minipj$ hdfs dfs -head req3/part-00000
   /assets/img/home-logo.png	 98716
   ```

   **98716** hits were made to "/assets/img/home-logo.png"

   

2. How many hits were made from the IP: 10.153.239.5

   ```bash
   student@CC-PM-34:~$ hadoop jar hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file minipj/mapper_ip.py -mapper mapper_ip.py -file minipj/reducer_ip.py -reducer reducer_ip.py -input access_log -output ip2
   ```

   ```bash
   student@CC-PM-34:~$ hdfs dfs -head ip2/part-00000
   10.153.239.5	547
   ```

   **547** hits were made from 10.153.239.5

3. Which path in the website has been hit most? How many hits were made to
   the path?

利用hadoop streamingjar包，来将mapper和reducer函数指定为某个脚本，只要保证mapper和reducer是可以接收标准输入并把结果输出在标准输出的脚本即可。python、shell、R都可以。注意input和output的文件路径都是指HDFS的路径

   ```bash
   student@CC-PM-34:~$ hadoop jar hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file minipj/mapper_req.py -mapper mapper_req.py -file minipj/reducer_sort.py -reducer reducer_sort.py -input access_log -output most_req
   ```

   ```bash
   student@CC-PM-34:~$ hdfs dfs -head most_req/part-00000
   /assets/css/combined.css	117326
   /assets/js/javascript_combined.js	106813
   /	98767
   /assets/img/home-logo.png	98716
   /assets/css/printstyles.css	93151
   /images/filmpics/0000/3695/Pelican_Blood_2D_Pack.jpg	91884
   /favicon.ico	66829
   /robots.txt	51973
   /images/filmpics/0000/3139/SBX476_Vanquisher_2d.jpg	39577
   /assets/img/search-button.gif	38975
   /assets/img/play_icon.png	34030
   /images/filmmediablock/290/Harpoon_2d.JPG	32529
   /images/filmpics/0000/1421/RagingPhoenix_2DSleeve.jpeg	29242
   /assets/img/x.gif	29196
   /release-schedule/	25919
   /assets/img/release-schedule-logo.png	24292
   /assets/img/banner/ten-years-banner-grey.jpg	22128
   /assets/img/banner/ten-years-banner-white.jpg	22120
   /assets/img/banner/ten-years-banner.png	21929
   /release-schedule	18926
   /assets/img/banner/ten-years-banner-black.jpg	17208
   ```

   The most hitted path is **/assets/css/combined.css**. 

   **117326** hits were made

4. Which IP accesses the website most? How many accesses were made by it?

   ```bash
   student@CC-PM-34:~$ hadoop jar hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file minipj/mapper_ip.py -mapper mapper_ip.py -file minipj/reducer_sort.py -reducer reducer_sort.py -input access_log -output most_ip
   ```

   ```bash
   student@CC-PM-34:~$ hdfs dfs -head most_ip/part-00000
   10.216.113.172	158614
   10.220.112.1	51942
   10.173.141.213	47503
   10.240.144.183	43592
   10.41.69.177	37554
   10.169.128.121	22516
   10.211.47.159	20866
   10.96.173.111	19667
   10.203.77.198	18878
   10.31.77.18	18721
   ```

   The **10.216.113.172** accesses the website most with **158614** numbers.


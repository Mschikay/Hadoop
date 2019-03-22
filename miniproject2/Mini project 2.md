# Mini project 2

Members: Ziqi Tang, Linglu Liu, Rongkai Liu



All the programming works are under the directory `~/ziqi/miniproject2/`  on the cloud server `192.241.155.216`

### Part 2: Developing Spark programs 

The task is to printout the total listening counts of each artist. Your program should print out the
listening counts per artist in descending order. In the ‘user_artists.dat’ file, listening counts for each
user-artist pair is indicated by the variable ‘weight’. 

Run:

![image-20190321083836653](/Users/eric/Library/Application Support/typora-user-images/image-20190321083836653.png)

```bash
student@CC-PM-34:~$ spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 512m \
    --executor-cores 1 \
    --queue default \
    ~/ziqi/miniproject2/question2-1.py
```

Result:

![image-20190321083806780](/Users/eric/Library/Application Support/typora-user-images/image-20190321083806780.png)

```bash
student@CC-PM-34:~$ head resultQ2 
('289', 2393140)
('72', 1301308)
('89', 1291387)
('292', 1058405)
('498', 963449)
('67', 921198)
('288', 905423)
('701', 688529)
('227', 662116)
('300', 532545)
```



### Part 3: Developing Spark programs 2

In this project, you need to program a program using Spark to answer the questions and also provide
the performance measurements for whether processing the data with cached RDD (resilient
distributed dataset: http://spark.apache.org/docs/latest/rdd-programming-guide.html#resilientdistributed-datasets-rdds ) or not.

Run without RDD:

![image-20190322001714113](/Users/eric/Library/Application Support/typora-user-images/image-20190322001714113.png)

```bash
student@CC-PM-34:~$ spark-submit --master yarn --deploy-mode client --driver-memory 512m --executor-memory 512m --executor-cores 1 --queue default ~/ziqi/miniproject2/question3-nordd.py 
```



Run with RDD:

![image-20190321083859839](/Users/eric/Library/Application Support/typora-user-images/image-20190321083859839.png)

```bash
student@CC-PM-34:~$ spark-submit --master yarn \
    --deploy-mode client \
    --driver-memory 512m \
    --executor-memory 512m \
    --executor-cores 1 \
    --queue default \
    ~/ziqi/miniproject2/question3-1.py 
```



Results without RDD:

![image-20190322001521905](/Users/eric/Library/Application Support/typora-user-images/image-20190322001521905.png)

```bash
294
297
Row(value='/assets/css/combined.css', count=117348)
Row(value='10.216.113.172', count=158614)
time consumed:  754.9370460510254
```



Results with RDD:

![image-20190321083936965](/Users/eric/Library/Application Support/typora-user-images/image-20190321083936965.png)

```bash
294
297
('/assets/css/combined.css', 117348)
('10.216.113.172', 158614)
time consumed:  93.71608328819275
```

1. How many hits were made to the website item “/assets/img/loading.gif”?**

   294

2. **How many hits were made to the website item “/assets/js/lightbox.js”?**

   297

3. **Which path in the website has been hit most? How many hits were made to the path?**

   '/assets/css/combined.css'

   117348 hits were made

4. **Which IP accesses the website most? How many accesses were made by it?**

   '10.216.113.172', 

   158614 accesses were made

The results are the same compare to **miniproject1**. 
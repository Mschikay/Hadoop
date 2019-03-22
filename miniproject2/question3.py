# 1. How many hits were made to the website item “/assets/img/loading.gif”?
# 2. How many hits were made to the website item “/assets/js/lightbox.js”?
# 3. Which path in the website has been hit most? How many hits were made to the path?
# 4. Which IP accesses the website most? How many accesses were made by it?


from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import re
import time


if __name__ == "__main__":
    start = time.time()
    spark = SparkSession \
        .builder \
        .appName("RDD_and_DataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    sc = spark.sparkContext

    file = sc.textFile("file:///Users/hannah/PreviousContent/grad/2018_2019_spring/cloud/miniproject2/access_log")

    # below is the first task
    # 294
    # 297
    # ('/assets/css/combined.css', 117348)
    # ('10.216.113.172', 158614)
    # 65.52329087257385

    web1 = file.filter(lambda l: re.match(r'.*/assets/img/loading.gif.*', l))
    res1 = web1.count()  # 294

    web2 = file.filter(lambda l: re.match(r'.*/assets/js/lightbox.js.*', l))
    res2 = web2.count()  # 297

    web3 = file.map(lambda l: (l.split(' ')[6], 1))
    res3 = web3.reduceByKey(lambda x, y: x + y).sortBy(lambda l: l[1], False).first()

    ip = file.map(lambda l: (l.split()[0], 1)).reduceByKey(lambda x, y: x + y)
    rank = ip.sortBy(lambda l: l[1], False)
    res4 = rank.first()

    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print('time consumed: ', time.time()-start)


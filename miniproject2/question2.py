# As part of the project you will be working with the ‘hetrec2011-lastfm-2k’ data set. In particular
# you will be working on the ‘user_artists.dat’ data file.

# The task is to printout the total listening counts of each artist. Your program should print out the
# listening counts per artist in descending order. In the ‘user_artists.dat’ file, listening counts for each
# user-artist pair is indicated by the variable ‘weight’.

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # 初始化SparkSession
    spark = SparkSession \
        .builder \
        .appName("RDD_and_DataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    sc = spark.sparkContext
    file = sc.textFile("file:///Users/hannah/PreviousContent/grad/2018_2019_spring/cloud/miniproject2/hetrec2011-lastfm-2k/user_artists.dat")
    parts = file.map(lambda l: l.split('\t'))
    header = parts.first()
    parts = parts.filter(lambda l: l != header)
    p = parts.map(lambda l: (l[1], int(l[2])))
    p2 = p.groupByKey().map(lambda x: (x[0], sum(list(x[1]))))
    result = p2.sortBy(lambda x: x[1], False).collect()

    # write result to disk
    fileObject = open('resultQ2', 'w')
    for r in result:
        fileObject.write(str(r))
        fileObject.write('\n')
    fileObject.close()


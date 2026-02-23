from pyspark.sql import SparkSession

# Q3 (5 Marks) – RDD Transformations (Option A)
spark = SparkSession.builder.appName("rdd").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

rdd = spark.sparkContext.textFile("data.txt")
result = rdd.flatMap(lambda x: x.split()).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

print("=== Word Count Result ===")
print(result.collect())

spark.stop()

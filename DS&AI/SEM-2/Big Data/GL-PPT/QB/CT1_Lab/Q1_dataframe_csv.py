from pyspark.sql import SparkSession

# Q1 (10 Marks) – Create DataFrame from CSV (Option A)
spark = SparkSession.builder.appName("csv").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("students.csv", header=True, inferSchema=True)

print("=== DataFrame Contents ===")
df.show()

print("=== Schema ===")
df.printSchema()

spark.stop()

from pyspark.sql import SparkSession

# Q2 (5 Marks) – DataFrame Operations (Option A)
spark = SparkSession.builder.appName("csv").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("students.csv", header=True, inferSchema=True)

print("=== Students with marks > 60 ===")
df.filter(df.marks > 60).select("name", "marks").show()

spark.stop()

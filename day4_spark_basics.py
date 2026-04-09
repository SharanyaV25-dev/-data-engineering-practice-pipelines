from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
spark = SparkSession.builder.appName("Day4_SparkBasics").getOrCreate()
data = [
    ("Annie", "Chennai", 50000),
    ("Balu", "Bangalore", 60000),
    ("David", "Hyderabad", 80000),
    ("Eve", "Chennai", 45000),
    ("Frank", "Bangalore", 70000),
    ("Grace", "Hyderabad", 55000),
    ("Henry", "Chennai", 65000)
]
columns = ["name","city","salary"]
#creating dataframe
df = spark.createDataFrame(data,columns)
#Filter salary > 50000
df.filter(df.salary > 50000).show()
#Group by city and calculate average salary
df.groupBy("city").avg("salary").show()
#Add new column salary_category
df = df.withColumn("salary_category", when(col("salary") > 60000, "High").otherwise("Low"))
df.show()
#sort by salary
df.orderBy("salary").show()
#Stop the SparkSession
spark.stop()
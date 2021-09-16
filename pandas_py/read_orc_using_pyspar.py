from pyspark.sql import SparkSession

filename = "/Users/manikandan.kk/hello_world_orc/part-00000-b6e99eb9-cf0c-4b0b-b627-d1dcddb42dfc-c000.snappy.orc"


spark = (SparkSession.builder.appName("SparkSQLExampleApp").getOrCreate())

df = (spark.read.format("orc").option("inferSchema", "true").option("header", "true").load(filename))
print(df)
print(type(df))

pandas_df = df.toPandas()
print(type(pandas_df))
print(pandas_df)

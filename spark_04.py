from pyspark import SparkConf, SparkContext, SQLContext
sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
df = sqlContext.read.json("output_twitter.json")
df.printSchema()
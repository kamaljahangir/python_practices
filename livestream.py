#!/usr/bin/python3

import findspark
# loading pyspark
findspark.init('/spark24')
# use pyspark
from pyspark import SparkContext    # for word count
# live data streamin
from pyspark.streaming import StreamingContext
# using Spark context
#sc=SparkContext()   #local system, argument message
sc=SparkContext("local[2]", "Networkwordcount")
# to assign delay in message
ssc=StreamingContext(sc, 10)
# defining tcp socket IP & port
lines=ssc.socketTextStream("13.234.83.222", 9999)  # bind the tcp socket
# above line will take each and every data in lines

# now splitting line with space
words=lines.flatMap(lambda word: (line.split(" "))
# assigning number 1 to each word

pairs = words.map(lambda word: (word, 1))

wordCounts = pairs.reduceByKey(lambda x, y: x + y)
# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()
# Start the computation
ssc.start()
# Wait for the computation to terminate
ssc.awaitTermination()




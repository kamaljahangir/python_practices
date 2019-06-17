import findspark
findspark.init('/spark24')
# Calling pyspark
from pyspark import SparkContext
sc=SparkContext()
# Loading file
frdd=sc.textFile('/root/a.txt')
# Pick single line
data=frdd.collect()
print(data)
# Searching for flatmap function
[i for i in dir(frdd) if 'flat' in i]
# Splitting the line
linesplit=frdd.flatMap(lambda line:line.split(' '))
# Applying map function
mapping=linesplit.map(lambda word:(word,1))
# Now applying Reduce function
count=mapping.reduceByKey(lambda a,b:a+b)
count.collect()
print(count.collect())

## Cookbook for Data Mining with Hadoop Ecosystem


### Data Storage

* Way to combine Spark with Hadoop HDFS.
    - ***To be studied.***


### Data Preprocessing

* Basic Data Import from outer file/source into Hadoop HDFS.
    - Just do as regular file systems since HDFS has do the abstraction for us, and we only need to take the cluster as a whole FS.
    - No need to be too detailed, to be updated based on the particular situation.
* Way to Implement Data Preprocessing methods under Hadoop Ecosystems:
    - Raw Hadoop MapReduce:
        + Too low-level, difficult to handle.
    - Pig/Hive:
        + ***To be studied.***
    - Spark [Currently Suggested Method]:
        + Data Cleaning
            - Noisy Points [TBD, based on other ML algorithms]
            - Missed Value
                + filter to eliminate
                + fill to missed values
        + Data Integration
            - ChiSqTest/CorrelationTest
                * https://spark.apache.org/docs/2.0.2/api/python/pyspark.mllib.html?highlight=chi#pyspark.mllib.stat.Statistics.chiSqTest
            - MetaData Comparasion

### Data Integration Methods

* How traditional ETL methods differ from Hadoop?


### Spark

* How does Spark make RDDs resilient in case a partition is lost?
    - Tracks the history of each partition and reruns what is needed to restore it.
    
    
### Others

* One important point in Hadoop-like architecture is to apply the characteristics of the static data. Then cache-like strategies can be applied to improve the efficiency when dealing with the Big Data.
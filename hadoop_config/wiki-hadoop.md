* MapReduce:
    - A kind of Processing framework.
    - Map:
        + Raw Data => map() => <key, value>
            * All the pairs are passed to several reducers.
    - Between the Map() and Reduce(), Hadoop conducts shuffle and sort such that all the pairs with the same key are collected together and be sorted with respect to the key.
    - Shuffle and group:
        + Hadoop shuffle the <key, value> pairs into different partitions with respect to the key value (stable hash map), and sort within each partition by key. If only 1 reducer is specified, HDFS will conduct global merge sorting to aggregate all partitions into one group, which is passed to that reducer. Otherwise, *n* intermediate groups will be formed, where *n* is the number of the reducers.
    - Reduce:
        + <key, value> => reduce() => final results
            * Do kind of Aggregation
    - Map/Reduce Functions are defined by users.
    - All the above operations are done in parallel, which means on all the nodes run the corresponding map/reduce functions at the same time.
    - We can test the program without Hadoop just with Unix ***pipeline*** and ***sort*** commands.
    - Hadoop distributes the Map() function to each datanode, and distributes the resulted groups to Reduce() function. 

* Hadoop:
    - Origin from Google.
    - Name comes from the name of a toy elephant of the son of Doug Cutting, one of the developers of the Hadoop.
    - Can't deal with real-time data since HDFS works based on batch job, which will cumulate certain amount of data, then do its work. Thus HDFS serves as a static database, which is the target case for MapReduce framework.
    - HBase: Solution to implement the pseudo real-time data storage for Hadoop. But can only work periodically due to the initial raw-data importing way. (batch job instead of Message Queue, which works as Streams)

* Spark:
    - A kind of Processing framework.
    - Rely on a DFS.
    - Able to process streaming data, while Hadoop's MapReduce can only handle static data.
    - Much faster than Hadoop's MapReduce (batch job: 10:1, analyze data in memory: 100:1).
        + Reason: 
            * Hadoop's MapReduce runs step by step, and each step covers a complete read/process/write procedure, while Spark only do one read/process/write procedure. And for the read and write parts, they need to access the disks for many times, which leads to the poor performance in iteratively disk R/W algorithms, eg. Machine Learning. 
            * When applying Hadoop's MapReduce framework, we have to exactly follow the Map/Reduce workflow. So it should have a mapper and a reducer state, not more or less. Thus Spark provides more combinations such as map=>reduce=>map.
            * Hadoop's MapReduce is based on JAVA protosomatically. We can do programming in Python, but the overall invoking is not user-friendly. We have too handle complicated commands when applying Hadoop Streaming [Mechanism to enable writing Map/Reduce codes in any language] to run Map/Reduce with Python.
    - Better to apply if requiring multiple processing, which frequently happen in Machine Learning.
    - Memory-base processing, Spark applies in-memory caching of data, which is specified by the user, which accesses great performance in iterative algorithms based on the same dataset => so gains 10~100 faster speed than Hadoop MapReduce.

* Spark Mechanism
    - Instead of writing Map() and Reduce() separately, we use a general function to adapt to the required works.


* Core Hadoop:
    - Store data on Hadoop's HDFS
    - Distributive storage on clusters (server sets)
    - Processing with MapReduce.

* Hadoop Streaming:
    - Make MapReduce codes be written in any language.

* MapReduce Mechanism:
    - Mapper: see which parts can be processed in parallel instead of in serial.
    - Reducer: Manipulate the piled parts on each Reducer in parallel, and the default case for Hadoop only has one reducer.
    + Data is passed as {key: value} pairs from Mappers to Reducers.

* Pseudo-HDFS:
    - Hadoop running on one Machine.


## Working:

* HDFS can be manipulated just like Linux OS, but in a Hadoop way.
* If the output directory has already existed, the Hadoop will stop that action without modifying any current content.
* If one DataNode fails/be broken, Hadoop will re-replicate the data on that node and continue the normal work. [Always 3 backups exist in a cluster]
* The default block size on HDFS is 64MB for the sake of processing & management efficiency
* A block is only processed by a single Mapper. However, this mapper output can be passed to the Reducer on another node. 


* Question:
    - Why if each reducer generate many output files for HDFS to manage, then apply fewer reducers than cores can be better?


###  Useful Links

* http://sci2s.ugr.es/BigData
* https://bdataanalytics.biomedcentral.com/articles/10.1186/s41044-016-0014-0
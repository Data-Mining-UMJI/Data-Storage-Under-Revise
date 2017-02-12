* MapReduce:
    - A kind of Processing framework.

* Hadoop:
    - Origin from Google.
    - Name comes from the name of a toy elephant of the son of Doug Cutting, one of the developers of the Hadoop.

* Core Hadoop:
    - Store data on Hadoop's HDFS
    - Distributive storage on clusters (server sets)
    - Processing with MapReduce.

* Hadoop Streaming:
    - Make MapReduce codes be written in any language.

* MapReduce Mechanism:
    - Mapper: see which parts can be processed in parallel instead of in serial.
    - Reducer: Manipulate the piled parts on each Reducer in parallel.
    + Data is passed as {key: value} pairs from Mappers to Reducers.

* Pseudo-HDFS:
    - Hadoop running on one Machine.


## Working:

* HDFS can be manipulated just like Linux OS, but in a Hadoop way.
* If the output directory has already existed, the Hadoop will stop that action without modifying any current content.
* If one DataNode fails/be broken, Hadoop will re-replicate the data on that node and continue the normal work. [Always 3 backups exist in a cluster]
* The default block size on HDFS is 64MB for the sake of processing & management efficiency
* A block is only processed by a single Mapper. However, this mapper output can be passed to the Reducer on another node. 
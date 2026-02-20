# Unit 2: Big Data Analytics using Artificial Intelligence Technologies
## Apache Spark — RDDs, Spark SQL, and Distributed Query Processing

> **References:** Holden Karau et al. – *Learning Spark* | Raj Kamal & Preethi Saxena – *Big Data Analytics*, TMH

---

## Table of Contents

1. [Introduction to Apache Spark](#1-introduction-to-apache-spark)
2. [Architecture of Apache Spark](#2-architecture-of-apache-spark)
3. [RDDs – Resilient Distributed Datasets](#3-rdds--resilient-distributed-datasets)
   - 3.1 What is an RDD?
   - 3.2 RDD Creation
   - 3.3 RDD Transformations
   - 3.4 RDD Actions
   - 3.5 RDD Persistence and Caching
   - 3.6 RDD Lineage and Fault Tolerance
   - 3.7 Pair RDDs
4. [Spark SQL](#4-spark-sql)
   - 4.1 What is Spark SQL?
   - 4.2 DataFrames
   - 4.3 Datasets
   - 4.4 SparkSession
   - 4.5 Catalyst Optimizer
   - 4.6 Tungsten Execution Engine
5. [SQL Queries in Spark](#5-sql-queries-in-spark)
   - 5.1 Running SQL Queries
   - 5.2 Reading Data
   - 5.3 DataFrame Operations
   - 5.4 Joins
   - 5.5 Aggregations and Grouping
   - 5.6 Window Functions
   - 5.7 Writing Data

---

## 1. Introduction to Apache Spark

### 1.1 What is Apache Spark?

**Apache Spark** is an open-source, unified analytics engine for **large-scale data processing**. It provides high-level APIs in **Java, Scala, Python (PySpark), and R**, and an optimized engine that supports general **execution graphs** (DAGs).

- Originally developed at **UC Berkeley's AMPLab** in 2009 by Matei Zaharia
- Donated to the **Apache Software Foundation** in 2013
- The name "Spark" reflects its key feature — **in-memory speed** (like a spark vs. the slow disk-based "fire" of MapReduce)

### 1.2 Why Spark? Problems with Hadoop MapReduce

| Limitation of MapReduce | How Spark Solves It |
|------------------------|---------------------|
| Writes intermediate results to disk after every stage | Stores intermediate results **in memory (RAM)** |
| High latency for iterative algorithms (ML, graph) | Iterative jobs reuse in-memory data — 10–100x faster |
| Only batch processing | Supports batch, streaming, SQL, ML, and graph in one framework |
| Verbose Java-only API | High-level Python, Scala, Java, R APIs |
| No interactive shell | Interactive `spark-shell` (Scala) and `pyspark` (Python) |
| Poor support for real-time | **Structured Streaming** for real-time processing |

### 1.3 Key Features of Apache Spark

1. **Speed**: In-memory computation; 100x faster than MapReduce for iterative workloads, 10x faster for disk-based operations
2. **Ease of Use**: High-level APIs; functional programming style; interactive shells
3. **Generality**: One framework for batch processing, SQL queries, streaming, machine learning, and graph processing
4. **Compatibility**: Runs on YARN, Mesos, Kubernetes, or standalone; reads from HDFS, S3, Cassandra, HBase, JDBC, and more
5. **Fault Tolerance**: RDD lineage enables automatic recovery without data replication overhead
6. **Lazy Evaluation**: Transformations are not executed until an action is triggered — enables whole-pipeline optimization

### 1.4 Spark vs Hadoop MapReduce

| Feature | Hadoop MapReduce | Apache Spark |
|---------|-----------------|--------------|
| **Processing** | Disk-based (HDFS after every stage) | In-memory (RAM-first, spills to disk) |
| **Speed** | Baseline | 10–100x faster |
| **Ease of API** | Verbose Java | Python, Scala, Java, R |
| **Workloads** | Batch only | Batch, SQL, Streaming, ML, Graph |
| **Fault Tolerance** | Block replication | RDD lineage |
| **Real-time** | No | Yes (Structured Streaming) |
| **Interactive** | No | Yes (spark-shell, pyspark, notebooks) |
| **Iterative Jobs** | Very slow (re-reads HDFS each iteration) | Fast (caches data in RAM) |
| **MapReduce Steps** | Two steps (Map + Reduce) | Multi-step DAG (flexible) |
| **Latency** | High (minutes) | Low (seconds) |

### 1.5 Spark Ecosystem (Unified Platform)

```
+-----------------------------------------------------------------------+
|                        SPARK ECOSYSTEM                                |
|                                                                       |
|  +------------+  +-----------+  +----------+  +-----------+          |
|  | Spark SQL  |  |  Spark    |  |  MLlib   |  |  GraphX   |          |
|  | Structured |  | Streaming |  | (Machine |  | (Graph    |          |
|  | Data / SQL |  | Real-time |  | Learning)|  | Processing|          |
|  +------------+  +-----------+  +----------+  +-----------+          |
|                                                                       |
|  +------------------------------------------------------------------+ |
|  |                     SPARK CORE (RDDs)                            | |
|  |          DAG Scheduler | Task Scheduler | Memory Manager          | |
|  +------------------------------------------------------------------+ |
|                                                                       |
|  +------------------------------------------------------------------+ |
|  |              CLUSTER MANAGERS                                    | |
|  |   Standalone  |   YARN   |   Mesos   |   Kubernetes             | |
|  +------------------------------------------------------------------+ |
|                                                                       |
|  +------------------------------------------------------------------+ |
|  |              DATA SOURCES                                        | |
|  |  HDFS | S3 | HBase | Cassandra | JDBC | Kafka | Parquet | ORC   | |
|  +------------------------------------------------------------------+ |
+-----------------------------------------------------------------------+
```

| Module | Purpose |
|--------|---------|
| **Spark Core** | Base engine — RDDs, memory management, DAG scheduling, task scheduling |
| **Spark SQL** | Structured data querying using SQL and DataFrame/Dataset APIs |
| **Spark Streaming / Structured Streaming** | Real-time stream processing (micro-batch or continuous) |
| **MLlib** | Scalable machine learning — classification, regression, clustering, NLP, pipelines |
| **GraphX** | Graph-parallel computation — PageRank, connected components, triangle counting |

### 1.6 Spark Use Cases

- **Batch ETL**: Replace Hive + MapReduce with faster Spark jobs
- **Real-time Analytics**: Stream processing of IoT, clickstream, financial transactions
- **Machine Learning**: Large-scale model training with MLlib
- **Interactive Exploration**: Jupyter notebooks + PySpark for ad-hoc analysis
- **Graph Analytics**: Social network analysis, fraud detection graphs
- **Log Processing**: Parse and aggregate server logs in near real-time

---

## 2. Architecture of Apache Spark

### 2.1 Overview

Spark uses a **master-worker architecture** where:
- The **Driver** is the master — hosts the application logic and coordinates execution
- **Executors** are workers — run tasks and store cached data
- A **Cluster Manager** allocates physical resources

```
+-----------------------------------------------------------+
|                    DRIVER PROGRAM                         |
|                                                           |
|   User Code (PySpark / Scala)                            |
|         ↓                                                 |
|   SparkSession / SparkContext                            |
|         ↓                                                 |
|   DAG Scheduler      Task Scheduler                      |
|   (Logical → Stages) (Stage → Tasks → Executors)         |
+----------------------------+------------------------------+
                             |
               +-------------+-------------+
               |                           |
    +----------+----------+     +----------+----------+
    |   CLUSTER MANAGER   |     |   CLUSTER MANAGER   |
    |  (YARN / Mesos /    |     |  (Standalone / K8s) |
    |   Kubernetes)        |     |                     |
    +----------+----------+     +---------------------+
               |
    +----------+-------+----------+
    |          |                  |
+---+------+ +-+-------+ +--------+--+
| Worker 1 | | Worker 2| | Worker 3  |
| Executor | | Executor| | Executor  |
| +------+ | | +------+| | +------+  |
| |Task 1| | | |Task 3|| | |Task 5|  |
| +------+ | | +------+| | +------+  |
| +------+ | | +------+| | +------+  |
| |Task 2| | | |Task 4|| | |Task 6|  |
| +------+ | | +------+| | +------+  |
| [Cache ] | | [Cache ]| | [Cache ]  |
+----------+ +---------+ +-----------+
```

### 2.2 Driver Program

The **Driver** is the process that runs the main function of the Spark application. It is the **brain** of the Spark application.

**Responsibilities:**
- Hosts the `SparkSession` (or `SparkContext`)
- Converts user code into a **logical plan** (DAG of RDD transformations)
- Builds the **DAG** (Directed Acyclic Graph) of stages and tasks
- Schedules tasks on Executors via the Task Scheduler
- Collects results from Executors
- Monitors the application and displays progress (Spark UI on port 4040)

**Driver runs on:**
- Client machine (in `--deploy-mode client`) — default; Driver lives on submitting machine
- Cluster node (in `--deploy-mode cluster`) — Driver is inside the cluster

### 2.3 SparkContext / SparkSession

**SparkContext** (Spark 1.x): The entry point to Spark Core (RDDs).

**SparkSession** (Spark 2.x+): The unified entry point — combines SparkContext, SQLContext, HiveContext, and StreamingContext into one object.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("yarn") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .enableHiveSupport() \
    .getOrCreate()

# Access underlying SparkContext
sc = spark.sparkContext
```

### 2.4 Cluster Manager

The **Cluster Manager** is responsible for allocating physical resources (CPU, memory) across the cluster. Spark is cluster-manager agnostic:

| Cluster Manager | Description | When to Use |
|----------------|-------------|-------------|
| **Standalone** | Spark's built-in, simple cluster manager | Small clusters, dev/test |
| **Apache YARN** | Hadoop's resource manager | Existing Hadoop clusters |
| **Apache Mesos** | General-purpose cluster manager | Mixed workloads |
| **Kubernetes** | Container orchestration | Cloud-native deployments |
| **Local** | Runs in single JVM thread / multiple threads | Development and testing |

```bash
# Local mode (1 thread)
spark.master = local

# Local mode (all cores)
spark.master = local[*]

# Local mode (4 cores)
spark.master = local[4]

# YARN cluster
spark.master = yarn

# Standalone
spark.master = spark://master-host:7077
```

### 2.5 Executors

**Executors** are JVM processes launched on **worker nodes** by the Cluster Manager at the start of an application. They live for the entire duration of the application.

**Responsibilities:**
- Execute **tasks** assigned by the Driver's Task Scheduler
- Store **cached RDD partitions** in memory (or disk if configured)
- Return task results to the Driver
- Report heartbeats to Driver

**Executor Resources:**
```bash
# Configure executor resources when submitting
spark-submit \
  --executor-memory 4g \
  --executor-cores 2 \
  --num-executors 10 \
  my_app.py
```

### 2.6 DAG (Directed Acyclic Graph)

Spark represents computation as a **DAG of stages**:

```
RDD A (textFile)
    |
    | map()          ← Narrow transformation
    |
RDD B (words)
    |
    | filter()       ← Narrow transformation
    |
RDD C (filtered)
    |
    | groupByKey()   ← Wide transformation (SHUFFLE BOUNDARY)
    |               ========================
RDD D (grouped)
    |
    | mapValues()    ← Narrow transformation
    |
RDD E (result)
    |
    count()          ← ACTION → triggers execution
```

**Stage 1:** textFile → map → filter (all narrow — no shuffle)
**Stage 2:** groupByKey (wide — requires shuffle across partitions)
**Stage 3:** mapValues (narrow — within same partition)

### 2.7 Narrow vs Wide Transformations

| Type | Definition | Examples | Shuffle? |
|------|-----------|----------|----------|
| **Narrow** | Each input partition contributes to at most one output partition | `map`, `filter`, `flatMap`, `union`, `mapPartitions` | No |
| **Wide** | Each input partition may contribute to multiple output partitions | `groupByKey`, `reduceByKey`, `sortByKey`, `join`, `distinct`, `repartition` | Yes (network shuffle) |

**Significance:**
- Narrow transformations are **pipelined** within a single stage (fast — no network I/O)
- Wide transformations cause **stage boundaries** — require data shuffle across network (slow)
- Minimizing wide transformations = key performance optimization

### 2.8 Job, Stage, and Task

| Term | Definition | Scope |
|------|-----------|-------|
| **Application** | One Spark program (SparkSession to stop) | Entire program |
| **Job** | Triggered by one action | Per action call |
| **Stage** | Set of tasks with no shuffle boundary | Separated by wide transformations |
| **Task** | Work on one partition on one executor | One partition per task |

```
Application
  └── Job (one per action)
        └── Stage (separated by shuffles)
              └── Task (one per partition)
```

**Example:** A file with 10 partitions processed with `map → filter → reduceByKey → collect()`:
- 1 Job (triggered by `collect()`)
- 2 Stages (Stage 1: map+filter; Stage 2: reduceByKey)
- Stage 1: 10 tasks (one per partition)
- Stage 2: N tasks (N = number of reduce partitions, default 200)

### 2.9 Spark Memory Management

Each Executor's memory is divided into regions:

```
+-----------------------------------------------------------+
|                   EXECUTOR MEMORY                         |
|                                                           |
|  +---------------------+  +---------------------------+  |
|  |  Execution Memory   |  |    Storage Memory         |  |
|  |  (Shuffle, joins,   |  |  (RDD cache, broadcast    |  |
|  |   sorts, aggs)      |  |   variables)              |  |
|  +---------------------+  +---------------------------+  |
|           (Unified Memory — can borrow from each other)  |
|                                                           |
|  +---------------------+  +---------------------------+  |
|  |  User Memory        |  |  Reserved Memory          |  |
|  |  (User data         |  |  (Spark internals,        |  |
|  |   structures)       |  |   ~300 MB)                |  |
|  +---------------------+  +---------------------------+  |
+-----------------------------------------------------------+
```

**Default split (Spark 2.x+ Unified Memory Model):**
- `spark.memory.fraction` = 0.6 (60% for Execution + Storage)
- `spark.memory.storageFraction` = 0.5 (50% of the 60% for Storage)
- Remaining = User Memory + Reserved Memory

### 2.10 Spark Web UI

Spark provides a web interface at `http://driver-host:4040` showing:
- **Jobs**: List of all jobs, status, duration
- **Stages**: DAG visualization, task metrics
- **Storage**: Cached RDDs/DataFrames
- **Environment**: Spark configuration
- **Executors**: Executor status, memory, task counts
- **SQL**: Query plans for Spark SQL queries

### 2.11 Launching a Spark Application

```bash
# General syntax
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --driver-memory 2g \
  --executor-memory 4g \
  --executor-cores 2 \
  --num-executors 10 \
  --conf spark.sql.shuffle.partitions=100 \
  --py-files dependencies.zip \
  my_app.py arg1 arg2

# Interactive PySpark shell
pyspark --master yarn --executor-memory 4g

# Interactive Scala shell
spark-shell --master yarn
```

---

## 3. RDDs – Resilient Distributed Datasets

### 3.1 What is an RDD?

**RDD (Resilient Distributed Dataset)** is the **fundamental data abstraction** in Apache Spark. It is an **immutable**, **distributed** collection of objects that can be processed in parallel.

**Breaking down the name:**
- **Resilient**: Fault-tolerant — if a partition is lost, Spark can recompute it using the **lineage graph**
- **Distributed**: Data is split into **partitions** spread across multiple nodes in the cluster
- **Dataset**: A collection of data items (can be any Python/Java/Scala object)

**Key Properties of an RDD:**

| Property | Description |
|----------|-------------|
| **Immutable** | Once created, an RDD cannot be changed. Transformations always create new RDDs |
| **Distributed** | Partitioned across the cluster nodes |
| **Lazy** | Transformations are not executed until an action is called |
| **Typed** | Elements have a type (Int, String, Tuple, etc.) |
| **Fault-tolerant** | Lineage allows automatic recomputation of lost partitions |
| **Partitioned** | Data is split into partitions (default: one per HDFS block) |

**When to use RDDs (vs DataFrames):**
- When working with **unstructured data** (text, binary, media files)
- When you need **fine-grained control** over physical distribution
- When data does **not fit a schema** (heterogeneous records)
- For **low-level transformations** not expressible in SQL

### 3.2 RDD Creation

#### Method 1: Parallelizing an Existing Collection

```python
from pyspark import SparkContext

sc = SparkContext("local[*]", "RDD Demo")

# From Python list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data)

# Specify number of partitions
rdd = sc.parallelize(data, numSlices=4)

print(rdd.getNumPartitions())    # 4
print(rdd.collect())             # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# From a list of tuples (creates Pair RDD)
pairs = sc.parallelize([('a', 1), ('b', 2), ('c', 3)])
```

#### Method 2: Loading from External Storage

```python
# From HDFS text file (one line = one element)
rdd = sc.textFile("hdfs:///user/hadoop/data/input.txt")

# With explicit partitions
rdd = sc.textFile("hdfs:///data/input.txt", minPartitions=10)

# From local filesystem
rdd = sc.textFile("file:///home/hadoop/data.txt")

# From S3
rdd = sc.textFile("s3a://bucket/path/data.txt")

# Multiple files / wildcards
rdd = sc.textFile("hdfs:///data/logs/*.txt")

# wholeTextFiles: returns (filename, content) pairs
rdd = sc.wholeTextFiles("hdfs:///data/configs/")

# From SequenceFile (Hadoop binary format)
rdd = sc.sequenceFile("hdfs:///data/seqfile")

# From JSON (via SparkSession DataFrame, converted)
rdd = spark.read.json("data.json").rdd
```

#### Method 3: Transforming an Existing RDD

Every transformation on an RDD creates a **new RDD**:

```python
base_rdd = sc.textFile("hdfs:///data/input.txt")
words_rdd = base_rdd.flatMap(lambda line: line.split(" "))   # New RDD
filtered_rdd = words_rdd.filter(lambda w: len(w) > 3)        # New RDD
```

### 3.3 RDD Transformations

Transformations are **lazy** — they define the computation but do not execute it. They return a new RDD.

#### 3.3.1 Basic Transformations

```python
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# map: Apply function to each element; returns one output per input
squared = rdd.map(lambda x: x ** 2)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter: Keep elements that satisfy the condition
evens = rdd.filter(lambda x: x % 2 == 0)
# [2, 4, 6, 8, 10]

# flatMap: Like map, but each element can produce 0 or more outputs; flattens result
lines = sc.parallelize(["Hello World", "Spark is Fast"])
words = lines.flatMap(lambda line: line.split(" "))
# ['Hello', 'World', 'Spark', 'is', 'Fast']

# distinct: Remove duplicates
rdd2 = sc.parallelize([1, 1, 2, 2, 3, 3])
unique = rdd2.distinct()
# [1, 2, 3]

# sample: Random sample
sampled = rdd.sample(withReplacement=False, fraction=0.3, seed=42)

# union: Combine two RDDs (allows duplicates)
rdd_a = sc.parallelize([1, 2, 3])
rdd_b = sc.parallelize([3, 4, 5])
combined = rdd_a.union(rdd_b)
# [1, 2, 3, 3, 4, 5]

# intersection: Common elements
common = rdd_a.intersection(rdd_b)
# [3]

# subtract: Elements in rdd_a but not in rdd_b
diff = rdd_a.subtract(rdd_b)
# [1, 2]

# cartesian: Cartesian product (all pairs)
r1 = sc.parallelize([1, 2])
r2 = sc.parallelize(['a', 'b'])
product = r1.cartesian(r2)
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
```

#### 3.3.2 Partition-Level Transformations

```python
# mapPartitions: Apply function to entire partition (one iterator in, one out)
# More efficient than map for operations with setup overhead (e.g., DB connections)
def process_partition(iterator):
    # Open DB connection once per partition (not once per record)
    results = []
    for record in iterator:
        results.append(record * 2)
    return iter(results)

result = rdd.mapPartitions(process_partition)

# mapPartitionsWithIndex: Like mapPartitions but also gets partition index
def show_partition(index, iterator):
    return iter([f"Partition {index}: {x}" for x in iterator])

result = rdd.mapPartitionsWithIndex(show_partition)

# glom: Collect partition into a list (each partition becomes one element)
rdd = sc.parallelize(range(8), 4)
glomed = rdd.glom().collect()
# [[0, 1], [2, 3], [4, 5], [6, 7]]
```

#### 3.3.3 Repartitioning

```python
rdd = sc.parallelize(range(100), 10)

# repartition: Increase or decrease partitions (always shuffles)
rdd_20 = rdd.repartition(20)

# coalesce: Decrease partitions only (avoids full shuffle — more efficient)
rdd_5 = rdd.coalesce(5)
# Use coalesce to reduce partitions after filtering removes most data
```

#### 3.3.4 Sorting

```python
rdd = sc.parallelize([5, 3, 1, 4, 2])

# sortBy: Sort by a key function
sorted_rdd = rdd.sortBy(lambda x: x)                # Ascending
sorted_rdd = rdd.sortBy(lambda x: x, ascending=False) # Descending

# sortBy with complex key
words = sc.parallelize(["banana", "apple", "cherry", "date"])
sorted_words = words.sortBy(lambda w: len(w))
# ['date', 'apple', 'banana', 'cherry']

# zip: Combine two RDDs element-wise into pairs
rdd_a = sc.parallelize([1, 2, 3])
rdd_b = sc.parallelize(['a', 'b', 'c'])
zipped = rdd_a.zip(rdd_b)
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

#### 3.3.5 Pair RDD Transformations

Pair RDDs are RDDs of `(key, value)` tuples with additional key-based operations:

```python
pairs = sc.parallelize([
    ('Alice', 85), ('Bob', 92), ('Alice', 78),
    ('Bob', 88), ('Charlie', 95), ('Alice', 90)
])

# mapValues: Transform only the value, keep key unchanged
doubled = pairs.mapValues(lambda score: score * 2)
# [('Alice',170), ('Bob',184), ('Alice',156), ...]

# flatMapValues: Like mapValues but can return multiple values
expanded = pairs.flatMapValues(lambda score: [score, score + 10])

# keys: Extract all keys
keys_rdd = pairs.keys()       # ['Alice', 'Bob', 'Alice', ...]

# values: Extract all values
vals_rdd = pairs.values()     # [85, 92, 78, ...]

# groupByKey: Group values by key (→ key, Iterable<values>)
grouped = pairs.groupByKey()
# ('Alice', [85, 78, 90]), ('Bob', [92, 88]), ('Charlie', [95])
# WARNING: groupByKey shuffles ALL values → memory intensive
# Prefer reduceByKey or aggregateByKey

# reduceByKey: Aggregate values per key (more efficient — partial aggregation on map side)
total = pairs.reduceByKey(lambda a, b: a + b)
# [('Alice', 253), ('Bob', 180), ('Charlie', 95)]

# aggregateByKey: More flexible than reduceByKey
#   (seqOp: combine within partition, combOp: combine across partitions)
result = pairs.aggregateByKey(
    (0, 0),                              # zero value: (sum, count)
    lambda acc, val: (acc[0]+val, acc[1]+1),   # seqOp (within partition)
    lambda acc1, acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])  # combOp (across partitions)
)
# → then mapValues to compute average:
avg = result.mapValues(lambda x: x[0] / x[1])
# [('Alice', 84.33), ('Bob', 90.0), ('Charlie', 95.0)]

# combineByKey: Most general per-key aggregation
result = pairs.combineByKey(
    lambda val: (val, 1),                       # createCombiner
    lambda acc, val: (acc[0]+val, acc[1]+1),    # mergeValue
    lambda acc1, acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])  # mergeCombiners
)

# foldByKey: Like reduceByKey but with a zero value
total = pairs.foldByKey(0, lambda a, b: a + b)

# countByKey: Count occurrences of each key (returns dict to driver)
counts = pairs.countByKey()
# {'Alice': 3, 'Bob': 2, 'Charlie': 1}

# sortByKey: Sort by key
sorted_pairs = pairs.sortByKey()              # Ascending
sorted_pairs = pairs.sortByKey(ascending=False) # Descending

# join: Inner join two Pair RDDs on key
rdd1 = sc.parallelize([('Alice', 90), ('Bob', 85)])
rdd2 = sc.parallelize([('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'C')])
joined = rdd1.join(rdd2)
# [('Alice', (90, 'A')), ('Bob', (85, 'B'))]

# leftOuterJoin / rightOuterJoin / fullOuterJoin
left_joined = rdd1.leftOuterJoin(rdd2)
# [('Alice', (90, Some('A'))), ('Bob', (85, Some('B')))]

# cogroup: Group multiple RDDs by key
cogrouped = rdd1.cogroup(rdd2)
# Each key → (Iterable<rdd1 values>, Iterable<rdd2 values>)

# subtractByKey: Remove records in rdd1 whose key appears in rdd2
no_charlie = rdd2.subtractByKey(rdd1)
# [('Charlie', 'C')]
```

#### 3.3.6 Complete Transformation Reference

| Transformation | Input | Output | Shuffle? |
|---------------|-------|--------|----------|
| `map(f)` | RDD[T] | RDD[U] | No |
| `flatMap(f)` | RDD[T] | RDD[U] | No |
| `filter(f)` | RDD[T] | RDD[T] | No |
| `mapPartitions(f)` | RDD[T] | RDD[U] | No |
| `distinct()` | RDD[T] | RDD[T] | Yes |
| `union(other)` | RDD[T] | RDD[T] | No |
| `intersection(other)` | RDD[T] | RDD[T] | Yes |
| `subtract(other)` | RDD[T] | RDD[T] | Yes |
| `cartesian(other)` | RDD[T] | RDD[(T,U)] | No |
| `sample(f, p)` | RDD[T] | RDD[T] | No |
| `repartition(n)` | RDD[T] | RDD[T] | Yes |
| `coalesce(n)` | RDD[T] | RDD[T] | Minimal |
| `sortBy(f)` | RDD[T] | RDD[T] | Yes |
| `groupByKey()` | RDD[(K,V)] | RDD[(K,Iter[V])] | Yes |
| `reduceByKey(f)` | RDD[(K,V)] | RDD[(K,V)] | Yes |
| `aggregateByKey()` | RDD[(K,V)] | RDD[(K,U)] | Yes |
| `combineByKey()` | RDD[(K,V)] | RDD[(K,C)] | Yes |
| `sortByKey()` | RDD[(K,V)] | RDD[(K,V)] | Yes |
| `join(other)` | RDD[(K,V)] | RDD[(K,(V,W))] | Yes |
| `leftOuterJoin(other)` | RDD[(K,V)] | RDD[(K,(V,Option[W]))] | Yes |
| `mapValues(f)` | RDD[(K,V)] | RDD[(K,U)] | No |
| `keys()` | RDD[(K,V)] | RDD[K] | No |
| `values()` | RDD[(K,V)] | RDD[V] | No |

### 3.4 RDD Actions

Actions **trigger execution** of the lazy DAG and return a result to the Driver or write to storage.

```python
rdd = sc.parallelize([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
pairs = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('c', 4)])

# ── Returning values to driver ──────────────────────────────────────

# collect: Return ALL elements to driver as a Python list
#          WARNING: dataset must fit in driver memory
result = rdd.collect()
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# count: Return number of elements
n = rdd.count()
# 11

# first: Return the first element
first = rdd.first()
# 3

# take(n): Return first n elements (may not be sorted)
top3 = rdd.take(3)
# [3, 1, 4]

# top(n): Return top n elements (largest first)
top3 = rdd.top(3)
# [9, 6, 5]

# takeOrdered(n): Return first n elements (smallest first, or by key function)
bottom3 = rdd.takeOrdered(3)
# [1, 1, 2]
bottom3_rev = rdd.takeOrdered(3, key=lambda x: -x)
# [9, 6, 5]

# takeSample(withReplacement, n, seed): Random sample to driver
sample = rdd.takeSample(False, 3, seed=42)

# reduce: Aggregate all elements using a binary function (must be commutative + associative)
total = rdd.reduce(lambda a, b: a + b)
# 44

product = rdd.reduce(lambda a, b: a * b)

# fold: Like reduce but with a zero value
total = rdd.fold(0, lambda a, b: a + b)

# aggregate: Most general action — apply seqOp within partitions, combOp across partitions
# Allows changing the return type
result = rdd.aggregate(
    (0, 0),                                     # zero value: (sum, count)
    lambda acc, val: (acc[0]+val, acc[1]+1),    # seqOp
    lambda acc1, acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])  # combOp
)
avg = result[0] / result[1]

# ── Statistical actions ─────────────────────────────────────────────

rdd_num = sc.parallelize([1.0, 2.0, 3.0, 4.0, 5.0])
rdd_num.sum()        # 15.0
rdd_num.mean()       # 3.0
rdd_num.min()        # 1.0
rdd_num.max()        # 5.0
rdd_num.stdev()      # Standard deviation
rdd_num.variance()   # Variance
rdd_num.stats()      # StatCounter with all stats at once

# ── Key-value actions ───────────────────────────────────────────────

# countByKey: Count per key (returns dict)
counts = pairs.countByKey()
# {'a': 2, 'b': 1, 'c': 1}

# countByValue: Count occurrences of each unique value
rdd.countByValue()
# {1: 2, 3: 2, 5: 3, 2: 1, 4: 1, 6: 1, 9: 1}

# lookup(key): Return all values for a given key (only for Pair RDDs)
vals = pairs.lookup('a')
# [1, 3]

# ── Saving results ─────────────────────────────────────────────────

# Save as text file (one file per partition)
rdd.saveAsTextFile("hdfs:///output/result/")

# Save as SequenceFile (Pair RDD only)
pairs.saveAsSequenceFile("hdfs:///output/seqfile/")

# Save as Hadoop file
pairs.saveAsHadoopFile("hdfs:///output/", "org.apache.hadoop.mapred.TextOutputFormat")

# ── Iteration ──────────────────────────────────────────────────────

# foreach: Apply function to each element (side effects only, e.g., DB writes)
rdd.foreach(lambda x: print(x))   # Runs on executors, no return

# foreachPartition: Apply function to each partition (e.g., one DB connection per partition)
def write_to_db(partition):
    conn = open_db_connection()
    for record in partition:
        conn.insert(record)
    conn.close()

rdd.foreachPartition(write_to_db)
```

#### Action Reference Table

| Action | Returns | Description |
|--------|---------|-------------|
| `collect()` | List | All elements to driver |
| `count()` | Long | Number of elements |
| `first()` | T | First element |
| `take(n)` | List | First n elements |
| `top(n)` | List | Top n elements (largest) |
| `takeOrdered(n)` | List | First n elements (sorted) |
| `takeSample(r,n)` | List | n random samples |
| `reduce(f)` | T | Aggregate via binary function |
| `fold(zero, f)` | T | Reduce with zero value |
| `aggregate(zero, seq, comb)` | U | General aggregation |
| `sum()` | Double | Sum of numeric elements |
| `mean()` | Double | Mean of numeric elements |
| `max()` | T | Maximum element |
| `min()` | T | Minimum element |
| `stdev()` | Double | Standard deviation |
| `countByKey()` | Dict | Count per key (Pair RDD) |
| `countByValue()` | Dict | Count per value |
| `lookup(k)` | List | Values for key k (Pair RDD) |
| `foreach(f)` | None | Side effects on elements |
| `foreachPartition(f)` | None | Side effects on partitions |
| `saveAsTextFile(path)` | None | Write to text files |
| `saveAsSequenceFile(path)` | None | Write to SequenceFile |

### 3.5 RDD Persistence and Caching

By default, every action re-executes the entire lineage. **Persistence** stores RDD partitions in memory/disk to avoid recomputation.

```python
from pyspark import StorageLevel

# ── persist() with explicit storage level ─────────────────────────

rdd.persist(StorageLevel.MEMORY_ONLY)
rdd.persist(StorageLevel.MEMORY_AND_DISK)
rdd.persist(StorageLevel.MEMORY_ONLY_SER)          # Serialized (smaller footprint)
rdd.persist(StorageLevel.MEMORY_AND_DISK_SER)
rdd.persist(StorageLevel.DISK_ONLY)
rdd.persist(StorageLevel.MEMORY_ONLY_2)            # 2 copies in memory (replication)
rdd.persist(StorageLevel.OFF_HEAP)                 # Off-heap memory (Tachyon)

# ── cache() — shorthand for MEMORY_ONLY ──────────────────────────
rdd.cache()

# ── unpersist() — remove from cache ──────────────────────────────
rdd.unpersist()
```

#### Storage Level Comparison

| Storage Level | Space | CPU Time | Memory | Disk | Description |
|--------------|-------|----------|--------|------|-------------|
| `MEMORY_ONLY` | High | Low | Yes | No | Default; fast but may evict |
| `MEMORY_AND_DISK` | High | Medium | Yes | Spill | Safest option |
| `MEMORY_ONLY_SER` | Low | High | Yes | No | Serialized saves space |
| `MEMORY_AND_DISK_SER` | Low | High | Yes | Yes | Serialized + spills |
| `DISK_ONLY` | Low | High | No | Yes | Slowest but always available |
| `MEMORY_ONLY_2` | 2x | Low | Yes | No | 2 memory replicas |

#### When to Persist

```python
# Good candidate: RDD used in multiple actions
data = sc.textFile("hdfs:///large_dataset.txt") \
         .flatMap(lambda line: line.split(",")) \
         .filter(lambda x: x.isdigit()) \
         .map(int)

data.cache()    # ← Cache before multiple actions

print(data.count())          # Action 1 — computes + stores in cache
print(data.mean())           # Action 2 — reuses cache (fast!)
print(data.max())            # Action 3 — reuses cache (fast!)

data.unpersist()             # Release cache when done
```

### 3.6 RDD Lineage and Fault Tolerance

Spark tracks the **lineage** of every RDD — the sequence of transformations that produced it. This is stored as a **DAG**.

```python
rdd1 = sc.textFile("hdfs:///input.txt")          # Source
rdd2 = rdd1.flatMap(lambda l: l.split(" "))       # Transformation
rdd3 = rdd2.filter(lambda w: w != "")             # Transformation
rdd4 = rdd3.map(lambda w: (w, 1))                 # Transformation
rdd5 = rdd4.reduceByKey(lambda a, b: a + b)       # Transformation

# View lineage
print(rdd5.toDebugString().decode())
# (2) PythonRDD[5] at RDD at PythonRDD.scala:53 []
#  |  MapPartitionsRDD[4] at reduceByKey
#  |  PairwiseRDD[3] at reduceByKey
#  |  PythonRDD[2] at RDD at PythonRDD.scala:53 []
#  |  MapPartitionsRDD[1] at textFile
#  |  input.txt HadoopRDD[0]
```

**Fault Recovery:**
- If a partition of `rdd5` is lost (executor crashed), Spark re-executes only the lost partition's lineage: `textFile → flatMap → filter → map → reduceByKey`
- No data replication needed — lineage acts as the recovery mechanism
- For long lineages, **checkpointing** breaks the lineage and saves to HDFS:

```python
sc.setCheckpointDir("hdfs:///spark-checkpoints/")
rdd5.checkpoint()   # Forces evaluation + saves to HDFS; lineage reset from here
rdd5.count()        # Triggers checkpoint
```

### 3.7 Shared Variables

#### Broadcast Variables

Broadcast variables efficiently distribute a **read-only variable** to all executors (sent once, not once per task):

```python
# Without broadcast (sent with every task — inefficient for large data)
lookup = {'US': 'United States', 'IN': 'India', 'UK': 'United Kingdom'}
rdd.map(lambda code: lookup.get(code, 'Unknown'))  # lookup sent with every task

# With broadcast (sent once per executor — efficient)
broadcast_lookup = sc.broadcast(lookup)
result = rdd.map(lambda code: broadcast_lookup.value.get(code, 'Unknown'))

# Access broadcast value
broadcast_lookup.value        # Returns the dict
broadcast_lookup.unpersist()  # Remove from executors
broadcast_lookup.destroy()    # Remove from executors + driver
```

#### Accumulators

Accumulators are **write-only** (from tasks) shared variables, typically used as counters:

```python
# Create accumulator
error_count = sc.accumulator(0)
total_records = sc.accumulator(0)

def process(record):
    total_records.add(1)
    if not is_valid(record):
        error_count.add(1)
        return None
    return record

processed = rdd.map(process).filter(lambda x: x is not None)
processed.count()   # Triggers execution

print(f"Total: {total_records.value}, Errors: {error_count.value}")
```

**Important:** Accumulators in transformations may be incremented more than once if tasks are re-executed (fault recovery). Only use them for approximate metrics, not critical logic.

---

## 4. Spark SQL

### 4.1 What is Spark SQL?

**Spark SQL** is a Spark module for **structured data processing**. It provides:
- A **SQL interface** to query data using standard SQL syntax
- A **DataFrame API** (Python, Scala, Java, R) for programmatic structured data manipulation
- A **Dataset API** (Scala/Java) for type-safe structured data
- The **Catalyst Optimizer** for automatic query optimization
- The **Tungsten Engine** for CPU-efficient execution

**Spark SQL vs Traditional SQL Databases:**

| Aspect | Traditional RDBMS | Spark SQL |
|--------|------------------|-----------|
| Scale | Vertical (one server) | Horizontal (thousands of nodes) |
| Data Volume | GB to low TB | TB to PB |
| Processing | OLTP + OLAP | OLAP (batch analytics) |
| ACID | Full | Partial (Delta Lake adds it) |
| Latency | Milliseconds | Seconds to minutes |
| Data Formats | Proprietary | Parquet, ORC, JSON, CSV, JDBC, Delta |
| Real-time | Limited | Yes (Structured Streaming) |
| ML Integration | External | Native (MLlib) |

### 4.2 DataFrames

A **DataFrame** is Spark SQL's primary abstraction — a **distributed collection of data organized into named columns**, analogous to a table in a relational database or a Python Pandas DataFrame.

**DataFrame vs RDD:**

| Aspect | RDD | DataFrame |
|--------|-----|-----------|
| Schema | No (untyped) | Yes (named columns, types) |
| Optimization | No (user controls) | Yes (Catalyst optimizer) |
| API Level | Low-level | High-level |
| Performance | Manual tuning needed | Auto-optimized |
| Data Type | Any Python object | Structured (Row objects) |
| Serialization | Java/Python native | Efficient binary (Tungsten) |
| Use Case | Unstructured/complex logic | Structured/semi-structured |

#### Creating DataFrames

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import Row

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

# ── From Python list of dictionaries ─────────────────────────────

data = [
    {"name": "Alice", "age": 30, "salary": 75000.0, "dept": "Engineering"},
    {"name": "Bob",   "age": 25, "salary": 60000.0, "dept": "Marketing"},
    {"name": "Carol", "age": 35, "salary": 90000.0, "dept": "Engineering"},
    {"name": "Dave",  "age": 28, "salary": 65000.0, "dept": "HR"},
]
df = spark.createDataFrame(data)

# ── From list of Rows ────────────────────────────────────────────

data = [
    Row(name="Alice", age=30, salary=75000.0),
    Row(name="Bob",   age=25, salary=60000.0),
]
df = spark.createDataFrame(data)

# ── From list of tuples + explicit schema ────────────────────────

data = [("Alice", 30, 75000.0), ("Bob", 25, 60000.0)]
schema = StructType([
    StructField("name",   StringType(),  nullable=False),
    StructField("age",    IntegerType(), nullable=True),
    StructField("salary", DoubleType(),  nullable=True),
])
df = spark.createDataFrame(data, schema=schema)

# ── From RDD ────────────────────────────────────────────────────

rdd = sc.parallelize([("Alice", 30), ("Bob", 25)])
df = rdd.toDF(["name", "age"])
df = spark.createDataFrame(rdd, schema=["name", "age"])

# ── From Files ──────────────────────────────────────────────────

df_csv     = spark.read.csv("data.csv", header=True, inferSchema=True)
df_json    = spark.read.json("data.json")
df_parquet = spark.read.parquet("data.parquet")
df_orc     = spark.read.orc("data.orc")
df_text    = spark.read.text("data.txt")

# ── From Hive Table ──────────────────────────────────────────────

df = spark.table("analytics_db.employees")
df = spark.sql("SELECT * FROM employees")
```

#### Inspecting DataFrames

```python
df.show()                  # Print first 20 rows
df.show(n=5)               # Print first 5 rows
df.show(truncate=False)    # No truncation of long values
df.show(5, False)          # First 5 rows, no truncation

df.printSchema()           # Show schema tree
df.schema                  # StructType object
df.dtypes                  # [('name', 'string'), ('age', 'int'), ...]
df.columns                 # ['name', 'age', 'salary', 'dept']

df.count()                 # Row count
df.describe().show()       # Summary statistics for numeric/string columns
df.summary().show()        # Extended stats (percentiles, etc.)

df.head(3)                 # First 3 rows as list of Row objects
df.first()                 # First row as Row object
df.tail(3)                 # Last 3 rows (Spark 3.0+)
df.limit(10)               # Return new DataFrame with max 10 rows

df.rdd                     # Convert to RDD of Row objects
df.toPandas()              # Convert to Pandas DataFrame (fits in driver memory)
```

### 4.3 Datasets

**Datasets** (Scala/Java only) are typed DataFrames that provide **compile-time type safety**:

```scala
// Scala example
case class Employee(name: String, age: Int, salary: Double, dept: String)

val ds: Dataset[Employee] = spark.read
  .csv("employees.csv")
  .as[Employee]

// Type-safe operations
val engineers: Dataset[Employee] = ds.filter(_.dept == "Engineering")
val avgSalary: Double = engineers.map(_.salary).reduce(_ + _) / engineers.count()
```

In Python (PySpark), DataFrames and Datasets are the same API (`DataFrame = Dataset[Row]`).

### 4.4 SparkSession

`SparkSession` is the unified entry point for Spark 2.x+:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .master("yarn") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .config("spark.sql.shuffle.partitions", "100") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .enableHiveSupport() \
    .getOrCreate()

# Access SparkContext
sc = spark.sparkContext

# Access catalog (metadata)
spark.catalog.listDatabases()
spark.catalog.listTables()

# Read data
df = spark.read.parquet("path")

# Run SQL
result = spark.sql("SELECT * FROM table")

# Stop session (end of program)
spark.stop()
```

### 4.5 Catalyst Optimizer

The **Catalyst Optimizer** is Spark SQL's query optimizer — it automatically transforms user queries into efficient execution plans.

```
HiveQL / SQL / DataFrame API
          ↓
   Unresolved Logical Plan
          ↓ Analysis (resolve references using Catalog)
   Resolved Logical Plan
          ↓ Logical Optimization (rule-based)
   Optimized Logical Plan
          ↓ Physical Planning (select strategies)
   Physical Plan(s)
          ↓ Cost Model (select best physical plan)
   Selected Physical Plan
          ↓ Code Generation (Tungsten JIT)
   Executable Code (RDDs)
```

**Catalyst Optimization Rules:**

| Optimization | Description | Example |
|-------------|-------------|---------|
| **Constant Folding** | Pre-compute constant expressions | `WHERE 1+1 > 1` → `WHERE 2 > 1` |
| **Predicate Pushdown** | Move filters as close to data source as possible | Filter read at Parquet level |
| **Column Pruning** | Read only needed columns | `SELECT name` reads only `name` column |
| **Join Reordering** | Reorder joins for efficiency (CBO) | Smallest table joined first |
| **Broadcast Join** | Broadcast small tables to avoid shuffle | Tables < threshold broadcast |
| **Subquery Elimination** | Rewrite correlated subqueries | Convert to joins |
| **Null Propagation** | Eliminate unnecessary null checks | Simplify expressions |

### 4.6 Tungsten Execution Engine

**Tungsten** is the physical execution engine beneath Catalyst:

1. **Off-heap Memory Management**: Manages memory directly (bypasses JVM GC overhead)
2. **Cache-Aware Computation**: Optimizes memory access patterns for CPU caches
3. **Whole-Stage Code Generation**: Compiles entire query stages into single bytecode functions (eliminates virtual function call overhead)
4. **Vectorized Execution**: Processes data in batches (vectors) rather than row-by-row

---

## 5. SQL Queries in Spark

### 5.1 Running SQL Queries

Spark SQL allows running standard SQL queries against registered tables/views:

```python
# Register DataFrame as a temporary view (session-scoped)
df.createOrReplaceTempView("employees")

# Register as a global view (accessible across sessions)
df.createOrReplaceGlobalTempView("employees_global")

# Run SQL query
result = spark.sql("SELECT * FROM employees WHERE dept = 'Engineering'")
result.show()

# Access global temp view (note the prefix)
result = spark.sql("SELECT * FROM global_temp.employees_global")

# List all available views
spark.catalog.listTables()

# Drop a temp view
spark.catalog.dropTempView("employees")
```

**Full SQL Example:**

```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("employees")

# Simple SELECT with WHERE
spark.sql("""
    SELECT name, dept, salary
    FROM employees
    WHERE salary > 70000
    ORDER BY salary DESC
""").show()

# Aggregation
spark.sql("""
    SELECT
        dept,
        COUNT(*)          AS headcount,
        AVG(salary)       AS avg_salary,
        MAX(salary)       AS max_salary,
        MIN(salary)       AS min_salary
    FROM employees
    GROUP BY dept
    HAVING COUNT(*) >= 2
    ORDER BY avg_salary DESC
""").show()
```

### 5.2 Reading Data into DataFrames

#### Reading CSV

```python
# Basic CSV read
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("hdfs:///data/employees.csv")

# Explicit schema (faster + safer than inferSchema)
schema = StructType([
    StructField("emp_id",   IntegerType(), True),
    StructField("name",     StringType(),  True),
    StructField("dept",     StringType(),  True),
    StructField("salary",   DoubleType(),  True),
    StructField("hire_date",DateType(),    True),
])
df = spark.read \
    .schema(schema) \
    .option("header", "true") \
    .option("dateFormat", "yyyy-MM-dd") \
    .option("nullValue", "N/A") \
    .option("mode", "DROPMALFORMED") \
    .csv("hdfs:///data/employees.csv")

# Read multiple CSV files
df = spark.read.csv(["file1.csv", "file2.csv"], header=True, inferSchema=True)
df = spark.read.csv("hdfs:///data/csvfiles/*.csv", header=True)
```

#### Reading JSON

```python
# Single-line JSON (one JSON object per line)
df = spark.read.json("hdfs:///data/events.json")

# Multi-line JSON (one JSON object spans multiple lines)
df = spark.read \
    .option("multiLine", "true") \
    .json("hdfs:///data/pretty_events.json")

# Nested JSON is automatically parsed into nested StructType
df.printSchema()
df.select("user.name", "user.address.city").show()
```

#### Reading Parquet

```python
# Parquet preserves schema — no need for inferSchema
df = spark.read.parquet("hdfs:///data/employees.parquet")

# Read specific columns (Spark applies column pruning at file level)
df = spark.read.parquet("hdfs:///data/employees.parquet") \
    .select("name", "salary")

# Read partitioned Parquet
df = spark.read.parquet("hdfs:///data/logs/year=2024/month=01/")
# Spark infers partition columns automatically
```

#### Reading from JDBC (RDBMS)

```python
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://host:3306/mydb") \
    .option("dbtable", "employees") \
    .option("user", "root") \
    .option("password", "secret") \
    .option("driver", "com.mysql.jdbc.Driver") \
    .option("numPartitions", "10") \
    .option("partitionColumn", "emp_id") \
    .option("lowerBound", "1") \
    .option("upperBound", "100000") \
    .load()
```

#### Reading from Hive

```python
# With enableHiveSupport() in SparkSession
df = spark.table("analytics_db.employees")

# Or via SQL
df = spark.sql("SELECT * FROM analytics_db.employees")
```

### 5.3 DataFrame Operations (DSL API)

The DataFrame API provides a **Domain-Specific Language (DSL)** — SQL-equivalent operations in Python/Scala:

#### Selecting Columns

```python
from pyspark.sql import functions as F
from pyspark.sql.functions import col, column, lit, expr

# Select specific columns
df.select("name", "salary").show()
df.select(col("name"), col("salary")).show()
df.select(df["name"], df["salary"]).show()

# Select with expressions
df.select(
    "name",
    (col("salary") * 1.1).alias("new_salary"),
    F.upper(col("dept")).alias("dept_upper")
).show()

# selectExpr: Use SQL expressions as strings
df.selectExpr(
    "name",
    "salary * 1.1 AS new_salary",
    "UPPER(dept) AS dept_upper",
    "CASE WHEN salary > 80000 THEN 'High' ELSE 'Low' END AS salary_band"
).show()

# Drop columns
df.drop("salary", "hire_date").show()

# withColumn: Add or replace a column
df = df.withColumn("annual_bonus", col("salary") * 0.10)
df = df.withColumn("salary_band",
    F.when(col("salary") >= 90000, "High")
     .when(col("salary") >= 60000, "Mid")
     .otherwise("Low")
)

# withColumnRenamed: Rename a column
df = df.withColumnRenamed("salary", "base_salary")
```

#### Filtering Rows

```python
# filter / where (interchangeable)
df.filter(col("salary") > 70000).show()
df.where(col("salary") > 70000).show()

# String expression
df.filter("salary > 70000 AND dept = 'Engineering'").show()

# Multiple conditions
df.filter(
    (col("dept") == "Engineering") &
    (col("salary") > 70000) &
    col("name").isNotNull()
).show()

# isin
df.filter(col("dept").isin("Engineering", "Marketing")).show()

# NOT isin
df.filter(~col("dept").isin("HR", "Finance")).show()

# LIKE / RLIKE
df.filter(col("name").like("A%")).show()
df.filter(col("name").rlike("^[A-C]")).show()

# isNull / isNotNull
df.filter(col("email").isNull()).show()
df.filter(col("email").isNotNull()).show()

# between
df.filter(col("salary").between(60000, 90000)).show()

# startsWith / endsWith / contains
df.filter(col("name").startsWith("A")).show()
df.filter(col("dept").endsWith("ing")).show()
df.filter(col("name").contains("lic")).show()
```

#### Sorting

```python
# Sort ascending (default)
df.sort("salary").show()
df.orderBy("salary").show()

# Sort descending
df.sort(col("salary").desc()).show()
df.orderBy(col("salary").desc()).show()

# Multi-column sort
df.sort(col("dept").asc(), col("salary").desc()).show()

# Sort with null handling
df.sort(col("salary").asc_nulls_last()).show()
df.sort(col("salary").desc_nulls_first()).show()
```

#### Deduplication

```python
# Drop all duplicate rows
df.distinct().show()

# Drop duplicates based on specific columns
df.dropDuplicates(["dept"]).show()          # Keep first occurrence per dept
df.drop_duplicates(["name", "dept"]).show() # Alias
```

#### Limiting Results

```python
df.limit(10).show()    # Return first 10 rows
```

### 5.4 Joins

Spark SQL supports all standard SQL join types:

#### SQL-Style Joins

```python
employees = spark.table("employees")
departments = spark.table("departments")
salaries = spark.table("salaries")

# INNER JOIN
spark.sql("""
    SELECT e.name, e.dept, d.location, d.manager
    FROM employees e
    INNER JOIN departments d ON e.dept = d.dept_name
    WHERE d.location = 'Mumbai'
""").show()

# LEFT OUTER JOIN
spark.sql("""
    SELECT e.name, d.location
    FROM employees e
    LEFT JOIN departments d ON e.dept = d.dept_name
""").show()

# RIGHT OUTER JOIN
spark.sql("""
    SELECT d.dept_name, COUNT(e.emp_id) AS headcount
    FROM departments d
    RIGHT JOIN employees e ON d.dept_name = e.dept
    GROUP BY d.dept_name
""").show()

# FULL OUTER JOIN
spark.sql("""
    SELECT e.name, d.dept_name
    FROM employees e
    FULL OUTER JOIN departments d ON e.dept = d.dept_name
""").show()

# CROSS JOIN
spark.sql("SELECT * FROM employees CROSS JOIN departments").show()

# SELF JOIN
spark.sql("""
    SELECT e.name AS employee, m.name AS manager
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.emp_id
""").show()

# Multi-table JOIN
spark.sql("""
    SELECT e.name, e.dept, d.location, s.salary_grade
    FROM employees e
    JOIN departments d ON e.dept = d.dept_name
    JOIN salary_grades s ON e.salary BETWEEN s.min_salary AND s.max_salary
""").show()
```

#### DataFrame API Joins

```python
# Inner join (default)
df_joined = employees.join(departments, employees["dept"] == departments["dept_name"])

# Specify join type
df_left = employees.join(departments,
    employees["dept"] == departments["dept_name"],
    how="left"           # Options: inner, left, right, outer, cross, semi, anti
)

# Join on multiple columns
df = orders.join(customers,
    (orders["customer_id"] == customers["id"]) &
    (orders["region"] == customers["region"]),
    how="inner"
)

# Join on same-named column (avoids ambiguity)
df = employees.join(departments, on="dept_name", how="inner")

# Semi join (keep rows in left that have a match in right, but don't include right columns)
df = employees.join(departments,
    employees["dept"] == departments["dept_name"],
    how="left_semi"
)

# Anti join (keep rows in left that have NO match in right)
df = employees.join(departments,
    employees["dept"] == departments["dept_name"],
    how="left_anti"
)
```

#### Broadcast Join (Optimization)

For joining a **small table** with a large table — broadcast the small table to all executors to avoid shuffle:

```python
from pyspark.sql.functions import broadcast

# DataFrame API
result = large_orders.join(broadcast(small_products), "product_id")

# SQL hint
spark.sql("""
    SELECT /*+ BROADCAST(d) */ e.name, d.location
    FROM employees e
    JOIN departments d ON e.dept = d.dept_name
""")

# Auto broadcast threshold (tables smaller than this are auto-broadcast)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "10mb")
# Set to -1 to disable auto-broadcast
```

### 5.5 Aggregations and Grouping

#### Basic Aggregations

```python
from pyspark.sql import functions as F

# ── SQL style ─────────────────────────────────────────────────────

spark.sql("""
    SELECT
        dept,
        COUNT(*)                              AS headcount,
        COUNT(DISTINCT name)                  AS unique_employees,
        SUM(salary)                           AS total_salary,
        AVG(salary)                           AS avg_salary,
        MAX(salary)                           AS max_salary,
        MIN(salary)                           AS min_salary,
        STDDEV(salary)                        AS std_salary,
        COLLECT_LIST(name)                    AS names_list,
        COLLECT_SET(dept)                     AS unique_depts
    FROM employees
    GROUP BY dept
    HAVING COUNT(*) >= 2
    ORDER BY avg_salary DESC
""").show()

# ── DataFrame API ─────────────────────────────────────────────────

df.groupBy("dept").agg(
    F.count("*").alias("headcount"),
    F.count_distinct("name").alias("unique_emp"),
    F.sum("salary").alias("total_salary"),
    F.avg("salary").alias("avg_salary"),
    F.max("salary").alias("max_salary"),
    F.min("salary").alias("min_salary"),
    F.stddev("salary").alias("std_salary"),
    F.collect_list("name").alias("names"),
    F.collect_set("dept").alias("unique_depts")
).filter(F.col("headcount") >= 2) \
 .orderBy(F.col("avg_salary").desc()) \
 .show()

# Global aggregation (no GROUP BY)
df.agg(
    F.count("*").alias("total_rows"),
    F.avg("salary").alias("company_avg"),
    F.sum("salary").alias("total_payroll")
).show()
```

#### ROLLUP and CUBE

```python
# ROLLUP: Hierarchical aggregation (subtotals)
spark.sql("""
    SELECT dept, COALESCE(name, 'TOTAL') AS name, SUM(salary) AS total
    FROM employees
    GROUP BY ROLLUP(dept, name)
    ORDER BY dept, name
""").show()

# DataFrame ROLLUP
df.rollup("dept", "name") \
  .agg(F.sum("salary").alias("total")) \
  .show()

# CUBE: All possible combinations of GROUP BY
spark.sql("""
    SELECT dept, name, SUM(salary) AS total
    FROM employees
    GROUP BY CUBE(dept, name)
""").show()

df.cube("dept", "name") \
  .agg(F.sum("salary").alias("total")) \
  .show()

# GROUPING SETS (manual control over grouping combinations)
spark.sql("""
    SELECT dept, name, SUM(salary) AS total
    FROM employees
    GROUP BY GROUPING SETS ((dept), (name), (dept, name), ())
""").show()
```

#### Pivot Tables

```python
# Pivot: Turn row values into column names
spark.sql("""
    SELECT * FROM (
        SELECT dept, year(hire_date) AS hire_year, salary
        FROM employees
    )
    PIVOT (
        AVG(salary)
        FOR hire_year IN (2020, 2021, 2022, 2023, 2024)
    )
""").show()

# DataFrame pivot
df.groupBy("dept") \
  .pivot("hire_year", [2020, 2021, 2022, 2023]) \
  .agg(F.avg("salary")) \
  .show()
```

### 5.6 Window Functions

Window functions operate over a **sliding window of rows** relative to the current row, without collapsing results like GROUP BY.

#### Syntax

```sql
function() OVER (
    [PARTITION BY col1, col2, ...]
    [ORDER BY col3 [ASC|DESC], ...]
    [ROWS | RANGE BETWEEN frame_start AND frame_end]
)
```

**Frame boundary options:**
- `UNBOUNDED PRECEDING` — start of partition
- `n PRECEDING` — n rows before current row
- `CURRENT ROW` — current row
- `n FOLLOWING` — n rows after current row
- `UNBOUNDED FOLLOWING` — end of partition

#### Ranking Functions

```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F

# Define window
window_dept = Window.partitionBy("dept").orderBy(col("salary").desc())

# SQL
spark.sql("""
    SELECT
        name, dept, salary,
        ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS row_num,
        RANK()       OVER (PARTITION BY dept ORDER BY salary DESC) AS rank,
        DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dense_rank,
        PERCENT_RANK() OVER (PARTITION BY dept ORDER BY salary)    AS pct_rank,
        NTILE(4)     OVER (ORDER BY salary)                        AS quartile
    FROM employees
""").show()

# DataFrame API
df.withColumn("row_num",     F.row_number().over(window_dept)) \
  .withColumn("rank",        F.rank().over(window_dept)) \
  .withColumn("dense_rank",  F.dense_rank().over(window_dept)) \
  .withColumn("quartile",    F.ntile(4).over(Window.orderBy("salary"))) \
  .show()
```

#### Analytic Functions

```python
# LAG / LEAD: Access previous / next row's value
spark.sql("""
    SELECT
        name, dept, salary, hire_date,
        LAG(salary, 1, 0)  OVER (PARTITION BY dept ORDER BY hire_date) AS prev_salary,
        LEAD(salary, 1, 0) OVER (PARTITION BY dept ORDER BY hire_date) AS next_salary,
        salary - LAG(salary, 1, 0) OVER (PARTITION BY dept ORDER BY hire_date) AS salary_diff
    FROM employees
""").show()

# FIRST_VALUE / LAST_VALUE
spark.sql("""
    SELECT
        name, dept, salary,
        FIRST_VALUE(salary) OVER (PARTITION BY dept ORDER BY hire_date) AS first_hire_salary,
        LAST_VALUE(salary)  OVER (
            PARTITION BY dept ORDER BY hire_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS last_hire_salary
    FROM employees
""").show()
```

#### Aggregate Window Functions (Running Totals, Moving Averages)

```python
# Running total within department, ordered by hire date
spark.sql("""
    SELECT
        name, dept, salary, hire_date,
        SUM(salary) OVER (
            PARTITION BY dept
            ORDER BY hire_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS running_total,
        AVG(salary) OVER (
            PARTITION BY dept
            ORDER BY hire_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS moving_avg_3,
        COUNT(*) OVER (
            PARTITION BY dept
        ) AS dept_headcount
    FROM employees
""").show()

# DataFrame API equivalent
window_running = Window.partitionBy("dept") \
    .orderBy("hire_date") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

window_moving = Window.partitionBy("dept") \
    .orderBy("hire_date") \
    .rowsBetween(-2, Window.currentRow)

df.withColumn("running_total", F.sum("salary").over(window_running)) \
  .withColumn("moving_avg_3",  F.avg("salary").over(window_moving)) \
  .show()
```

#### Practical Window Function Example

```python
# Find top 3 earners per department
spark.sql("""
    SELECT name, dept, salary, rank
    FROM (
        SELECT
            name, dept, salary,
            RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank
        FROM employees
    )
    WHERE rank <= 3
    ORDER BY dept, rank
""").show()

# Alternatively with CTE (Common Table Expression)
spark.sql("""
    WITH ranked AS (
        SELECT
            name, dept, salary,
            DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dr
        FROM employees
    )
    SELECT name, dept, salary
    FROM ranked
    WHERE dr = 1    -- top earner per department
""").show()
```

### 5.7 Advanced SQL Features

#### Common Table Expressions (CTE)

```python
spark.sql("""
    WITH
    dept_stats AS (
        SELECT
            dept,
            AVG(salary) AS avg_salary,
            MAX(salary) AS max_salary
        FROM employees
        GROUP BY dept
    ),
    high_value_depts AS (
        SELECT dept
        FROM dept_stats
        WHERE avg_salary > 70000
    )
    SELECT e.name, e.salary, d.avg_salary
    FROM employees e
    JOIN dept_stats d ON e.dept = d.dept
    WHERE e.dept IN (SELECT dept FROM high_value_depts)
    ORDER BY e.salary DESC
""").show()
```

#### Subqueries

```python
spark.sql("""
    -- Correlated subquery: employees earning above their dept average
    SELECT name, dept, salary
    FROM employees e1
    WHERE salary > (
        SELECT AVG(salary)
        FROM employees e2
        WHERE e2.dept = e1.dept
    )
    ORDER BY dept, salary DESC
""").show()

spark.sql("""
    -- IN subquery
    SELECT name, dept
    FROM employees
    WHERE dept IN (
        SELECT dept_name
        FROM departments
        WHERE location = 'Bangalore'
    )
""").show()

spark.sql("""
    -- EXISTS subquery
    SELECT name, dept
    FROM employees e
    WHERE EXISTS (
        SELECT 1 FROM departments d
        WHERE d.dept_name = e.dept AND d.budget > 1000000
    )
""").show()
```

#### String Functions in SQL

```python
spark.sql("""
    SELECT
        UPPER(name)                    AS name_upper,
        LENGTH(name)                   AS name_len,
        SUBSTRING(name, 1, 3)          AS name_prefix,
        CONCAT(name, ' (', dept, ')')  AS full_label,
        REPLACE(dept, 'Engineering', 'Eng') AS dept_short,
        SPLIT(name, ' ')[0]            AS first_name,
        TRIM(name)                     AS trimmed_name,
        LPAD(CAST(emp_id AS STRING), 6, '0') AS emp_id_padded
    FROM employees
""").show()
```

#### Date Functions in SQL

```python
spark.sql("""
    SELECT
        name,
        hire_date,
        YEAR(hire_date)                         AS hire_year,
        MONTH(hire_date)                        AS hire_month,
        DATEDIFF(CURRENT_DATE, hire_date)       AS days_employed,
        DATEDIFF(CURRENT_DATE, hire_date) / 365 AS years_employed,
        DATE_ADD(hire_date, 90)                 AS probation_end,
        DATE_FORMAT(hire_date, 'MMMM yyyy')     AS hire_month_name,
        CASE
            WHEN DATEDIFF(CURRENT_DATE, hire_date) / 365 >= 10 THEN 'Veteran'
            WHEN DATEDIFF(CURRENT_DATE, hire_date) / 365 >= 5  THEN 'Senior'
            ELSE 'Junior'
        END AS seniority
    FROM employees
""").show()
```

#### NULL Handling

```python
spark.sql("""
    SELECT
        name,
        COALESCE(phone, email, 'No contact')   AS contact,
        NVL(bonus, 0)                          AS bonus,
        NULLIF(dept, 'Unassigned')             AS dept_clean,
        IF(salary IS NULL, 'Missing', 'Known') AS salary_status
    FROM employees
""").show()

# DataFrame API
df.withColumn("contact", F.coalesce(col("phone"), col("email"), lit("No contact"))) \
  .withColumn("bonus",   F.coalesce(col("bonus"), lit(0))) \
  .fillna({"salary": 0, "dept": "Unknown"}) \
  .dropna(subset=["name"]) \
  .show()
```

### 5.8 Writing Data

#### Writing to Files

```python
# ── Write as Parquet (recommended) ─────────────────────────────

df.write \
  .mode("overwrite") \           # overwrite | append | ignore | error (default)
  .parquet("hdfs:///output/employees/")

# With partitioning
df.write \
  .mode("overwrite") \
  .partitionBy("dept", "hire_year") \
  .parquet("hdfs:///output/employees_partitioned/")

# ── Write as CSV ────────────────────────────────────────────────

df.write \
  .mode("overwrite") \
  .option("header", "true") \
  .option("delimiter", ",") \
  .csv("hdfs:///output/employees.csv")

# ── Write as JSON ───────────────────────────────────────────────

df.write \
  .mode("overwrite") \
  .json("hdfs:///output/employees.json")

# ── Write as ORC ────────────────────────────────────────────────

df.write \
  .mode("overwrite") \
  .orc("hdfs:///output/employees.orc")

# ── Control number of output files ─────────────────────────────

# Default: one file per partition (can be many small files)
df.coalesce(1).write.parquet("output/single_file/")    # Exactly 1 file
df.repartition(10).write.parquet("output/10_files/")   # Exactly 10 files
```

#### Writing to Hive

```python
# Save as Hive table (requires enableHiveSupport)
df.write \
  .mode("overwrite") \
  .saveAsTable("analytics_db.employees_processed")

# Write with partitioning
df.write \
  .mode("overwrite") \
  .partitionBy("dept") \
  .format("orc") \
  .saveAsTable("analytics_db.employees_orc")

# Insert into existing Hive table
df.write \
  .mode("append") \
  .insertInto("analytics_db.employees")
```

#### Writing to JDBC

```python
df.write \
  .format("jdbc") \
  .option("url", "jdbc:mysql://host:3306/mydb") \
  .option("dbtable", "employees_result") \
  .option("user", "root") \
  .option("password", "secret") \
  .option("driver", "com.mysql.jdbc.Driver") \
  .mode("overwrite") \
  .save()
```

#### Write Modes

| Mode | Behavior |
|------|---------|
| `overwrite` | Overwrite existing data |
| `append` | Append to existing data |
| `ignore` | Do nothing if data exists |
| `error` (default) | Raise error if data exists |

---

## Summary — Key Concepts

### RDD Summary

| Concept | Description |
|---------|-------------|
| **Immutable** | RDDs never change; transformations create new RDDs |
| **Lazy** | Transformations build a DAG; execution triggered by actions |
| **Partitioned** | Data split across cluster nodes; one task per partition |
| **Fault-tolerant** | Lineage allows automatic recomputation of lost partitions |
| **Narrow transformation** | No shuffle; map, filter, flatMap |
| **Wide transformation** | Shuffle required; groupByKey, join, sort |
| **Action** | Triggers execution; collect, count, save |
| **Cache/Persist** | Store RDD in memory to avoid recomputation across actions |
| **Broadcast** | Read-only variable sent to all executors (once per executor) |
| **Accumulator** | Write-only counter/aggregator across tasks |

### Spark SQL Summary

| Concept | Description |
|---------|-------------|
| **SparkSession** | Unified entry point to Spark SQL, RDDs, and Streaming |
| **DataFrame** | Distributed table with schema (named columns, types) |
| **Dataset** | Typed DataFrame (Scala/Java only) |
| **Catalyst** | Query optimizer — constant folding, predicate pushdown, join reordering |
| **Tungsten** | Physical execution engine — off-heap memory, code generation |
| **Temp View** | Register DataFrame as SQL table (session-scoped) |
| **Broadcast Join** | Small table sent to all executors to avoid shuffle |
| **Window Function** | Row-level computation over a partition (RANK, LAG, LEAD, running sum) |
| **CTE** | WITH clause for reusable named subqueries |
| **Partitioned Write** | Write data organized by column values into subdirectories |

### Spark SQL Functions Quick Reference

| Category | Functions |
|----------|-----------|
| **String** | `upper`, `lower`, `length`, `substring`, `concat`, `split`, `trim`, `replace`, `regexp_replace`, `like` |
| **Math** | `abs`, `round`, `floor`, `ceil`, `sqrt`, `pow`, `mod`, `rand` |
| **Date** | `current_date`, `year`, `month`, `day`, `datediff`, `date_add`, `date_format`, `to_date`, `unix_timestamp` |
| **Aggregate** | `count`, `sum`, `avg`, `max`, `min`, `stddev`, `collect_list`, `collect_set`, `count_distinct` |
| **Conditional** | `when/otherwise`, `coalesce`, `nvl`, `nullif`, `if`, `isnull`, `isnan` |
| **Window** | `row_number`, `rank`, `dense_rank`, `ntile`, `lag`, `lead`, `first_value`, `last_value`, `percent_rank` |
| **Array** | `array`, `array_contains`, `size`, `explode`, `sort_array`, `array_distinct`, `flatten` |
| **Map** | `map`, `map_keys`, `map_values`, `map_from_arrays` |
| **Struct** | `struct`, `named_struct` |
| **JSON** | `get_json_object`, `json_tuple`, `from_json`, `to_json`, `schema_of_json` |
| **Type** | `cast`, `col`, `lit`, `expr` |

---

*End of Unit 2 — Big Data Analytics*

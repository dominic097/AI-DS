# Answer Sheet – Unit 3 & 4 (20 Marks Each)

---

## Module 3: Spark MLlib and Spark Structured Streaming

---

### Q1. (Understand – L2)

# Outline the programming model of Spark MLlib using PySpark. Describe how it facilitates scalable machine learning pipelines for big data.

#### Introduction

Spark MLlib is Apache Spark's built-in machine learning library. It is designed to run machine learning algorithms on distributed datasets at scale, eliminating the need to move large volumes of data to a dedicated ML server. It integrates seamlessly with Spark's DataFrames API, making it a natural choice for big data ML workflows.

#### Core Programming Model

The programming model of Spark MLlib revolves around three key abstractions:

**1. Transformer**
A Transformer takes a DataFrame as input, applies a transformation, and produces a new DataFrame. For example, a trained model acts as a Transformer: it takes raw feature data and outputs a column of predictions.

Examples:
- `VectorAssembler` — combines multiple feature columns into a single vector column
- `StandardScaler` — normalizes features
- A trained `LogisticRegressionModel` — produces prediction and probability columns

**2. Estimator**
An Estimator is an algorithm that can be fit (trained) on a DataFrame. When you call `.fit()` on an Estimator, it returns a Transformer (the trained model).

Examples:
- `LogisticRegression` — trains a classifier
- `KMeans` — trains a clustering model
- `RandomForestClassifier` — trains an ensemble model

**3. Pipeline**
A Pipeline chains multiple Transformers and Estimators into a single, reproducible workflow. When you call `.fit()` on a Pipeline, it trains each stage sequentially. The output is a `PipelineModel` (a series of Transformers) that can be applied to new data.

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression

assembler = VectorAssembler(inputCols=["age", "income", "credit_score"], outputCol="features")
scaler    = StandardScaler(inputCol="features", outputCol="scaled_features")
lr        = LogisticRegression(featuresCol="scaled_features", labelCol="default")

pipeline = Pipeline(stages=[assembler, scaler, lr])
model    = pipeline.fit(train_df)       # Trains all stages
predictions = model.transform(test_df)  # Predicts on new data
```

#### How MLlib Facilitates Scalability

| Feature | Benefit |
|---------|---------|
| Distributed DataFrames | Training data is partitioned across nodes; computation runs in parallel |
| In-memory Processing | Avoids repeated disk I/O across iterations (unlike MapReduce) |
| Lazy Evaluation | DAG-based execution — operations are only executed when an action is called |
| Pipeline API | Reproducible, reusable ML workflows; prevents data leakage in cross-validation |
| Built-in Cross-Validation | `CrossValidator` and `TrainValidationSplit` support hyperparameter tuning at scale |
| Integration | Works directly with Spark SQL, Kafka, HDFS — no data movement needed |

#### Key MLlib Algorithms

- **Classification**: Logistic Regression, Random Forest, Gradient Boosted Trees, Naive Bayes
- **Regression**: Linear Regression, Decision Tree Regression
- **Clustering**: K-Means, Bisecting K-Means, Gaussian Mixture
- **Feature Engineering**: TF-IDF, Word2Vec, PCA, MinMaxScaler
- **Recommendation**: ALS (Alternating Least Squares) for collaborative filtering

#### Real-World Use Case: Credit Scoring

A bank processes 50 million loan applications per year stored in HDFS. The traditional single-machine ML approach takes 8 hours to retrain the model daily.

**With Spark MLlib:**
1. Application data is loaded as a Spark DataFrame from HDFS.
2. A Pipeline assembles features (income, debt ratio, credit history), scales them, and trains a `GBTClassifier`.
3. The trained `PipelineModel` is applied in batch to score all new applications.
4. The entire process runs across a 20-node Spark cluster and completes in under 20 minutes.

The Pipeline ensures the same preprocessing applied during training is automatically applied during prediction — eliminating one of the most common sources of production ML bugs.

#### Conclusion

Spark MLlib's Pipeline-based programming model, combined with Spark's distributed execution engine, makes it a production-grade ML framework for big data. It abstracts distributed computing complexity away from data scientists while delivering the scalability that enterprise workloads demand.

---

### Q2. (Apply – L3)

# Explain the basic concepts of Spark Structured Streaming and its APIs. Apply these to a use case involving continuous monitoring of website traffic logs for detecting unusual spikes.

#### Introduction

Spark Structured Streaming is a scalable, fault-tolerant stream processing engine built on the Spark SQL engine. Unlike traditional stream processing where you think about records flowing through pipelines, Structured Streaming lets you think of a stream as an **unbounded table** that keeps growing. You write the same DataFrame/SQL code you would for batch — Spark handles the continuous execution under the hood.

#### Core Concept: The Streaming as a Table Model

```
Time    → t1  t2  t3  t4  ...
Events  →  [row1, row2] [row3] [row4, row5] ...

Modelled as an unbounded table:
+--------+------+---------+
| url    | user | timestamp|
+--------+------+---------+
| /home  |  u1  |  t1     |
| /login |  u2  |  t1     |
| /home  |  u3  |  t2     |
| ...    | ...  | ...     |
```

Every time new data arrives, Spark processes the new rows incrementally and updates the result.

#### Two Execution Modes

1. **Micro-batch Mode** (default): Spark collects incoming data into small batches and processes them at a set trigger interval (e.g., every 5 seconds). Offers exactly-once fault tolerance.
2. **Continuous Mode**: Very low latency (~1 ms), but limited in the operations it supports. Suitable for simple map/filter pipelines.

#### Core APIs

**Reading a Stream — `readStream`**
```python
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "web-traffic") \
    .load()
```

**Writing a Stream — `writeStream`**
```python
query = result_df.writeStream \
    .outputMode("update")       # Only write changed rows
    .format("console")
    .trigger(processingTime="10 seconds")
    .option("checkpointLocation", "/checkpoints/traffic")
    .start()
query.awaitTermination()
```

**Output Modes:**
| Mode | Description |
|------|-------------|
| `append` | Only new rows added to the result table are written out |
| `complete` | Entire result table is written after every trigger |
| `update` | Only rows that were updated since last trigger are written |

**Windowed Aggregation:**
Structured Streaming supports time-based windowing — grouping events by event time into fixed-duration windows.

```python
from pyspark.sql.functions import window, col

windowed = df.groupBy(
    window(col("event_time"), "1 minute", "30 seconds"),  # 1-min window, slides every 30s
    col("url")
).count()
```

**Watermarking:**
Watermarks tell Spark how long to wait for late-arriving data before finalizing a window:
```python
df.withWatermark("event_time", "2 minutes")
```

#### Applied Use Case: Detecting Traffic Spikes on a Website

**Problem:** A web analytics company wants to detect unusual spikes in page hits (e.g., DDoS attack, viral content) in real time.

**Architecture:**
```
Web Servers → Kafka Topic "web-logs" → Spark Structured Streaming → Alert Sink (DB / Dashboard)
```

**Implementation:**

```python
# 1. Read raw logs from Kafka
raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "web-logs") \
    .load()

# 2. Parse the JSON payload
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StringType, TimestampType

schema = StructType() \
    .add("url", StringType()) \
    .add("ip", StringType()) \
    .add("event_time", TimestampType())

logs = raw.select(from_json(col("value").cast("string"), schema).alias("data")) \
          .select("data.*")

# 3. Windowed count per URL
traffic = logs.withWatermark("event_time", "1 minute") \
    .groupBy(window("event_time", "1 minute"), "url") \
    .count()

# 4. Filter for spikes (more than 10,000 hits per minute on any URL)
spikes = traffic.filter(col("count") > 10000)

# 5. Write alerts
spikes.writeStream \
    .outputMode("update") \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://alerts-db/spikes") \
    .option("checkpointLocation", "/checkpoints/spikes") \
    .start()
```

In this design, every 30 seconds Spark processes the latest batch of log events, counts hits per URL within 1-minute windows, and writes any URLs exceeding 10,000 hits directly into an alerts database — enabling near-real-time DDoS or viral-traffic detection.

#### Conclusion

Spark Structured Streaming unifies batch and stream processing through a familiar DataFrame API. Its windowing, watermarking, and fault-tolerant checkpointing make it production-ready for continuous workloads like website traffic monitoring, fraud detection, and IoT sensor analysis.

---

### Q3. (Analyze – L4)

# Compare the operations supported on Streaming DataFrames in Spark with those on static DataFrames. Analyze their implications for handling unbounded data streams.

#### Introduction

Spark exposes a unified DataFrame API for both batch (static) and streaming (unbounded) data. While the syntax is largely identical, the semantics and supported operations differ significantly — because streaming data is infinite, stateful, and time-sensitive in ways that static data is not.

#### Static DataFrames

A static DataFrame represents a finite, fixed dataset loaded from HDFS, S3, a database, or a CSV file. It supports the full range of Spark SQL operations:

- All types of joins (inner, outer, cross)
- Arbitrary aggregations (groupBy, agg)
- Sorting and ordering
- Distinct and deduplication
- Windowing functions (rank, lead, lag)
- Full random access to any row

Since the data is finite and known at the time of the query, Spark can optimise the entire execution plan before running it.

#### Streaming DataFrames

A Streaming DataFrame represents data arriving continuously from a source (Kafka, socket, files). Since the table is unbounded, Spark cannot know all the data upfront. This introduces constraints:

| Operation | Static DataFrame | Streaming DataFrame |
|-----------|-----------------|---------------------|
| `filter`, `map`, `select` | Supported | Supported (stateless) |
| `groupBy` + aggregation | Supported | Supported only with watermark |
| `count()`, `sum()` | Supported | Supported (stateful — requires state store) |
| Sort (`orderBy`) | Supported | **NOT supported** (data is unbounded) |
| Distinct | Supported | Partially (with watermark) |
| Stream-to-stream joins | Not applicable | Supported with watermark |
| Stream-to-static join | Not applicable | Supported (broadcast static side) |
| Cross join | Supported | **NOT supported** |
| Arbitrary nested queries | Supported | Limited |

#### Key Concepts Unique to Streaming DataFrames

**1. Stateful Aggregation**
Operations like running counts, sums, or averages require Spark to maintain state across micro-batches. This state is stored in an in-memory state store (backed by checkpoints on disk) and grows as more data arrives.

**2. Windowing**
Since you cannot aggregate an infinite stream meaningfully without bounds, streaming aggregations are performed over time windows:
- **Tumbling window**: Non-overlapping fixed-duration windows (e.g., count per minute)
- **Sliding window**: Overlapping windows (e.g., count in every 1-minute window, sliding every 30 seconds)

**3. Watermarking**
Watermarks define how long Spark waits for late-arriving events before finalising a window. Without watermarks, Spark must keep state for all windows indefinitely — causing unbounded memory growth.

```python
df.withWatermark("event_time", "5 minutes")
  .groupBy(window("event_time", "10 minutes"))
  .count()
```
Here, Spark discards state for windows older than 5 minutes beyond the latest event time.

**4. Output Modes**
Static DataFrames always produce complete results. Streaming DataFrames must specify how results are emitted (append, update, complete), which restricts which aggregations are valid for each mode.

#### Implications for Unbounded Data

| Challenge | Implication |
|-----------|------------|
| Infinite data | Cannot sort, distinct, or perform operations requiring full dataset visibility |
| Late data | Must use watermarks to bound state size; some late records may be dropped |
| Memory management | Stateful operations consume heap/state-store memory; watermarks are essential for cleanup |
| Fault tolerance | Streaming queries must use checkpointing to recover from failures mid-stream |
| Ordering | Event-time ordering (not processing-time) is used via watermarking to correctly assign events to windows |

#### Practical Example: Count of API Calls vs. Running Total

Static:
```python
# Fine — operates on a known dataset
df.groupBy("endpoint").count().orderBy("count", ascending=False)
```

Streaming (equivalent intent):
```python
# orderBy is NOT allowed on a streaming DataFrame
# Correct approach: windowed count without sorting
df.withWatermark("ts", "2 minutes") \
  .groupBy(window("ts", "1 minute"), "endpoint") \
  .count() \
  .writeStream.outputMode("update").format("console").start()
```

#### Conclusion

Streaming DataFrames impose operational constraints that directly reflect the nature of unbounded data. Sorting is impossible, aggregations require windowing, and state must be bounded by watermarks to prevent memory exhaustion. Understanding these differences is essential for designing correct and efficient real-time pipelines in Spark.

---

### Q4. (Evaluate – L5)

# Evaluate the strengths and potential drawbacks of using Spark MLlib for building machine learning models in a distributed cluster environment.

#### Introduction

Spark MLlib has become a widely adopted library for large-scale machine learning. As with any technology, its adoption must be evaluated against both its capabilities and its limitations, particularly when deployed in distributed cluster environments.

#### Strengths of Spark MLlib

**1. True Distributed Training**
MLlib distributes data across cluster nodes and performs parallel computation natively using Spark's execution engine. Training a model on billions of rows is feasible without any special infrastructure beyond a Spark cluster.

**2. In-Memory Processing**
Unlike Hadoop MapReduce, which writes intermediate results to disk after every step, Spark keeps data in memory across iterations. This is critical for ML algorithms that are inherently iterative (e.g., gradient descent), resulting in 10–100x speed improvements over MapReduce-based ML.

**3. Pipeline API — Reproducibility and Correctness**
The Pipeline abstraction ensures that the same preprocessing steps (scaling, encoding, imputation) are applied identically during training and inference. This eliminates a major class of production ML bugs caused by inconsistent feature engineering.

**4. Unified Ecosystem**
MLlib operates directly on Spark DataFrames. This means the same cluster and codebase handles data ingestion (from HDFS, Kafka, S3), preprocessing, training, evaluation, and batch scoring — without data movement between systems.

**5. Scalable Hyperparameter Tuning**
`CrossValidator` and `TrainValidationSplit` APIs distribute hyperparameter grid search across cluster nodes, reducing tuning time that would take hours on a single machine.

**6. Integration with Streaming**
Models trained with MLlib can be applied inside `foreachBatch` of Structured Streaming queries, enabling real-time inference on live data streams.

#### Drawbacks of Spark MLlib

**1. Not Optimised for Deep Learning**
MLlib provides only traditional ML algorithms. For neural networks (CNNs, Transformers, LSTMs), dedicated frameworks like TensorFlow, PyTorch, or HorovodRunner (a Spark-integrated DL runner) are significantly more capable. This is a critical gap as deep learning now dominates many domains.

**2. Memory-Intensive**
In-memory processing is a strength, but also a liability: large models, wide DataFrames, and complex Pipelines can exhaust cluster memory. Spark requires careful tuning of executor memory, shuffle partitions, and caching to avoid out-of-memory (OOM) errors.

**3. Micro-batch, Not True Real-Time**
Spark Structured Streaming (and thus streaming inference) is micro-batch — there is a minimum latency of hundreds of milliseconds. Applications requiring sub-millisecond inference (e.g., high-frequency trading) must use purpose-built systems.

**4. Debugging Complexity in Distributed Environments**
Stack traces in Spark are notoriously verbose. A bug in a UDF or a serialisation error can produce multi-page JVM stack traces that are difficult to interpret. Profiling performance bottlenecks across distributed executors adds further complexity.

**5. Limited Algorithm Coverage**
Compared to scikit-learn (which has 100+ algorithms), MLlib's algorithm library is more selective. Advanced techniques like XGBoost or LightGBM require third-party libraries (`xgboost4j-spark`, `synapse.ml`) rather than being built-in.

**6. Overhead for Small Datasets**
Spark's distributed overhead (cluster startup, DAG planning, shuffle operations) makes it inefficient for small datasets. A scikit-learn model trained on a single machine can outperform an MLlib pipeline on data that fits in RAM.

#### Balanced Evaluation Summary

| Dimension | Verdict |
|-----------|---------|
| Scale | Excellent — designed for petabyte-scale ML |
| Speed | Very good for batch; not suitable for ultra-low-latency |
| Ease of use | Moderate — Pipeline API is clean, but cluster tuning is hard |
| Algorithm breadth | Limited — best for classical ML; poor for deep learning |
| Ecosystem fit | Excellent — native Spark integration |
| Operational cost | High — requires skilled Spark engineers for production deployment |

#### Conclusion

Spark MLlib is an excellent choice for organisations that need to train and serve classical machine learning models on large, distributed datasets and already operate a Spark cluster. However, teams that require deep learning capabilities, ultra-low-latency inference, or have datasets that fit comfortably in a single machine's memory are better served by purpose-built alternatives like TensorFlow, PyTorch, or scikit-learn.

---

### Q5. (Create – L6)

# Design a theoretical framework for a real-time anomaly detection system using Spark Structured Streaming, detailing the flow from data ingestion to output generation in a financial fraud monitoring scenario.

#### Introduction

Real-time fraud detection requires processing high-velocity transaction data, applying learned patterns, and generating alerts within seconds. Spark Structured Streaming combined with Spark MLlib provides a unified platform to build such a system end-to-end.

#### System Architecture Overview

```
[Transaction Sources]
  ATM, POS, Online Banking
         |
         ▼
  [Apache Kafka]
  Topic: "transactions"
  Partitioned by card_id
         |
         ▼
  [Spark Structured Streaming]
  ┌──────────────────────────────────┐
  │  1. Ingest & Parse               │
  │  2. Feature Engineering          │
  │  3. MLlib Model Inference        │
  │  4. Anomaly Scoring & Filtering  │
  └──────────────────────────────────┘
         |
         ▼
  [Output Sinks]
  ┌──────────────┬────────────────┐
  │  Alert DB    │  Dashboard     │
  │  (PostgreSQL)│  (Grafana)     │
  └──────────────┴────────────────┘
         |
         ▼
  [Downstream Actions]
  Card Block API / Fraud Analyst Queue
```

#### Layer 1 — Data Ingestion

Every financial transaction (card swipe, online payment, ATM withdrawal) is published to a Kafka topic `transactions` by the core banking system. Each message is a JSON record:

```json
{
  "txn_id": "T9823",
  "card_id": "C4521",
  "amount": 4800.00,
  "merchant_category": "electronics",
  "location": "Dubai",
  "timestamp": "2026-04-17T14:32:10Z",
  "home_country": "India"
}
```

Kafka partitions messages by `card_id` — this ensures all transactions from the same card are processed in order by the same Spark task, enabling per-card stateful features.

#### Layer 2 — Stream Ingestion and Parsing (Spark)

```python
raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "transactions") \
    .load()

transactions = raw.select(from_json(col("value").cast("string"), txn_schema).alias("t")) \
                  .select("t.*")
```

#### Layer 3 — Feature Engineering

Raw transaction fields are insufficient for fraud detection. We compute:

- **Amount deviation**: How much does this transaction deviate from the card's 30-day average spend?
- **Location anomaly**: Is the transaction country different from the cardholder's home country?
- **Velocity**: How many transactions has this card made in the last 10 minutes?
- **Merchant risk**: Is the merchant category historically high-risk (e.g., crypto exchanges)?

Windowed features are computed using Structured Streaming's stateful operations:

```python
velocity = transactions \
    .withWatermark("timestamp", "2 minutes") \
    .groupBy(window("timestamp", "10 minutes", "1 minute"), "card_id") \
    .agg(count("txn_id").alias("txn_count_10m"), sum("amount").alias("total_amount_10m"))
```

#### Layer 4 — Model Inference (MLlib)

An `IsolationForest` or `GradientBoostedTreeClassifier` model is pre-trained offline on historical labeled fraud data and saved as a `PipelineModel`:

```python
fraud_model = PipelineModel.load("/models/fraud_detector_v3")
```

Inside `foreachBatch`, the model is applied to each micro-batch of enriched transactions:

```python
def score_batch(batch_df, batch_id):
    scored = fraud_model.transform(batch_df)
    alerts = scored.filter(col("prediction") == 1)   # 1 = fraudulent
    alerts.write.jdbc(url=db_url, table="fraud_alerts", mode="append")

transactions_enriched.writeStream \
    .foreachBatch(score_batch) \
    .option("checkpointLocation", "/checkpoints/fraud") \
    .trigger(processingTime="5 seconds") \
    .start()
```

#### Layer 5 — Output Generation and Actions

| Output Sink | Purpose |
|-------------|---------|
| PostgreSQL `fraud_alerts` table | Persistent record of all detected fraud events |
| Grafana Dashboard | Real-time visual monitoring of fraud rate by region |
| REST API call | Triggers card blocking via the bank's Card Management System |
| Kafka topic `fraud-notifications` | Downstream consumers: SMS alerts to customers, compliance logging |

#### Fault Tolerance

- **Checkpointing** saves the streaming query's progress (offsets and state) to HDFS. On failure, Spark restarts from the last checkpoint without reprocessing or missing events.
- **Kafka offset management** ensures exactly-once semantics when combined with idempotent writes to the output database.
- **Model versioning**: The model path is externalised so that a new model version can be hot-swapped by updating the path and restarting the streaming query without architectural changes.

#### Conclusion

This framework demonstrates that Spark Structured Streaming is well-suited for financial fraud detection: it handles high-velocity Kafka streams, applies stateful windowed feature engineering, integrates MLlib model inference within micro-batches, and delivers alerts to multiple sinks with end-to-end fault tolerance. The system can process millions of transactions per minute with sub-10-second detection latency.

---

---

## Module 4: Apache Kafka and Apache Airflow

---

### Q1. (Understand – L2)

# Describe the cluster architecture of Apache Kafka, including its messaging components and the role of brokers in data partitioning and replication.

#### Introduction

Apache Kafka is a distributed, fault-tolerant, high-throughput publish-subscribe messaging system originally developed at LinkedIn and later open-sourced by Apache. It is designed to handle real-time data feeds across large-scale distributed systems, acting as a durable, replayable message bus between data producers and consumers.

#### Core Architecture

```
                        ┌─────────────────────────────┐
                        │         ZooKeeper            │
                        │  (Leader Election, Metadata) │
                        └────────────┬────────────────-┘
                                     │
           ┌─────────────────────────┼──────────────────────────┐
           │                         │                          │
    ┌──────┴──────┐           ┌──────┴──────┐           ┌──────┴──────┐
    │  Broker 1   │           │  Broker 2   │           │  Broker 3   │
    │ Partition 0 │◄──────────│ Partition 0 │           │ Partition 1 │
    │ (Leader)    │  Replica  │ (Follower)  │           │ (Leader)    │
    └─────────────┘           └─────────────┘           └─────────────┘
           ▲                                                    ▲
           │ Produce                                            │ Produce
    ┌──────┴──────┐                                      ┌─────┴──────┐
    │  Producer A │                                      │ Producer B │
    └─────────────┘                                      └────────────┘
                              ▼ Consume
                     ┌────────────────────┐
                     │   Consumer Group   │
                     │  ┌────┐  ┌────┐   │
                     │  │ C1 │  │ C2 │   │
                     │  └────┘  └────┘   │
                     └────────────────────┘
```

#### Key Components

**1. Broker**
A Kafka broker is a server process that receives messages from producers, stores them on disk, and serves them to consumers. A Kafka cluster typically consists of 3 to hundreds of brokers. Brokers do not store messages indefinitely — retention is configurable (e.g., 7 days or 1 TB per topic).

Each broker handles:
- Message persistence (append-only log files on disk)
- Replication of partitions it leads
- Serving fetch requests from consumers

**2. Topic**
A Topic is a named category to which producers send messages and from which consumers read. Topics are the fundamental unit of data organisation in Kafka.

**3. Partition**
Each topic is divided into one or more partitions. A partition is an ordered, immutable sequence of records, each identified by a monotonically increasing offset.

- Partitions enable **parallelism**: multiple producers can write simultaneously to different partitions; multiple consumers can read simultaneously.
- Messages within a partition are always in order. Ordering across partitions is not guaranteed.
- The number of partitions determines the maximum parallelism of consumers in a group.

**4. Replication**
Each partition has one **leader** and zero or more **followers** (replicas):
- Producers always write to the partition leader.
- Followers continuously replicate from the leader.
- If a leader broker fails, ZooKeeper elects a new leader from the in-sync replicas (ISR).
- Replication factor is configurable (commonly 3 for production).

**5. Offset**
Every message within a partition has a unique, sequential offset. Consumers track their read position using offsets, enabling:
- **Replay**: Re-read messages from any historical offset.
- **Fault recovery**: Resume from the last committed offset after a consumer crash.

**6. ZooKeeper (Traditional) / KRaft (Modern)**
Traditionally, ZooKeeper manages Kafka's cluster metadata:
- Tracks which broker is the leader for each partition
- Stores consumer group offsets (in older versions)
- Performs leader election on broker failure

In newer versions (Kafka 3.x+), Kafka's own **KRaft** consensus protocol replaces ZooKeeper, simplifying deployment.

#### Data Partitioning Strategy

Producers control which partition a message is sent to using:
- **Key-based partitioning**: Messages with the same key always go to the same partition (ensures ordering per key — e.g., all events for `user_id=42` go to partition 2).
- **Round-robin**: No key; messages are distributed evenly across all partitions for load balancing.
- **Custom partitioner**: Application-defined logic.

#### Real-World Use Case: Netflix Event Streaming

Netflix uses Kafka to process 700 billion events per day. Each microservice (player, search, recommendation) publishes events to Kafka topics. Downstream services consume these streams for real-time dashboards, personalisation, and anomaly detection — all decoupled through Kafka's broker cluster.

#### Conclusion

Kafka's cluster architecture — with its distributed brokers, partitioned topics, replication for fault tolerance, and ZooKeeper-managed metadata — provides the durability, scalability, and resilience needed for mission-critical real-time data pipelines. The separation of producers, brokers, and consumers makes the system highly modular and independently scalable.

---

### Q2. (Apply – L3)

# Illustrate the concepts of Kafka producers and consumers, including consumer groups. Apply this to a scenario of building a real-time recommendation engine for an online streaming platform.

#### Introduction

In Kafka's messaging model, **Producers** are applications that publish messages to topics, and **Consumers** are applications that subscribe to topics and process those messages. The **Consumer Group** abstraction enables parallel, fault-tolerant consumption at scale.

#### Kafka Producer

A Kafka Producer is responsible for sending records (key-value pairs) to a Kafka topic. Key Producer behaviours:

**Sending modes:**
- **Fire-and-forget** (`acks=0`): Send and don't wait for acknowledgement — fastest, but may lose messages.
- **Synchronous** (`acks=1`): Wait for leader to acknowledge — moderate reliability.
- **Fully durable** (`acks=all`): Wait for all in-sync replicas to acknowledge — safest, slower.

**Key-based routing:**
If a message key is provided, Kafka hashes the key to determine the partition — ensuring all events with the same key land on the same partition in order.

```python
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'kafka:9092'})

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")

producer.produce(
    topic='user-events',
    key='user_42',           # All events for user_42 → same partition
    value='{"action":"play","content_id":"C101","ts":"2026-04-17T10:00:00Z"}',
    callback=delivery_report
)
producer.flush()
```

#### Kafka Consumer

A Kafka Consumer reads messages from one or more partitions of a topic. Each message is identified by its partition and offset.

**Offset management:**
- **Auto-commit**: Kafka commits the offset automatically at a regular interval.
- **Manual commit**: The consumer explicitly commits the offset after processing — provides exactly-once guarantees when combined with idempotent processing logic.

```python
from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id':          'recommendation-engine',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['user-events'])

while True:
    msg = consumer.poll(timeout=1.0)
    if msg and not msg.error():
        process_event(msg.value())
        consumer.commit()   # Manual commit after processing
```

#### Consumer Groups

A **Consumer Group** is a set of consumer instances that collectively consume all partitions of a subscribed topic. Kafka guarantees that each partition is assigned to exactly one consumer within a group at any time.

```
Topic: user-events (4 partitions)
Consumer Group: recommendation-engine (2 consumers)

Partition 0 → Consumer C1
Partition 1 → Consumer C1
Partition 2 → Consumer C2
Partition 3 → Consumer C2
```

**Key properties:**
- If a consumer in the group dies, its partitions are **automatically rebalanced** to the remaining consumers.
- Multiple independent consumer groups can read the same topic independently — each maintains its own offset. This allows the same stream to be consumed simultaneously by different systems (e.g., recommendations AND analytics AND logging) without interference.

#### Applied Use Case: Real-Time Recommendation Engine for a Streaming Platform

**Platform:** "StreamItNow" — an online video streaming service with 10 million concurrent users.

**Goal:** Update each user's content recommendations within 5 seconds of them completing an action (play, pause, like, search).

**Architecture:**

```
User Actions (Play, Like, Search)
        │
        ▼
[Producer: Frontend Service]
  Publishes to Kafka topic "user-events"
  Key = user_id (ensures per-user ordering)
        │
        ▼
[Kafka Topic: "user-events" — 20 partitions]
        │
   ┌────┴──────────────────────────┐
   │ Consumer Group 1              │ Consumer Group 2
   │ "recommendation-engine"       │ "analytics-pipeline"
   │ (10 consumers → Spark/Flink)  │ (5 consumers → ClickHouse)
   └───────────────────────────────┘
        │
        ▼
[Recommendation Service]
  - Retrieves user's watch history from Redis cache
  - Applies collaborative filtering model (MLlib / custom)
  - Pushes updated recommendations to user's session

        │
        ▼
[Consumer Group 2: Analytics]
  - Counts plays per content_id per minute
  - Updates trending charts independently
```

**Why separate consumer groups?**
The recommendation engine and the analytics pipeline need the same event data but process it differently and at different speeds. Consumer groups allow both to read from the same Kafka topic independently — the analytics group does not slow down or interfere with the recommendation group.

#### Conclusion

Kafka's producer-consumer model, enriched by consumer groups, provides a flexible and scalable foundation for real-time data pipelines. For a streaming platform, it decouples the event source from multiple downstream consumers, ensures per-user event ordering via key-based partitioning, and provides fault tolerance through automatic partition rebalancing on consumer failure.

---

### Q3. (Analyze – L4)

# Examine the Directed Acyclic Graph (DAG) structure in Apache Airflow. Analyze how it enables complex workflow orchestration compared to linear scripting approaches.

#### Introduction

Apache Airflow is an open-source platform for programmatically authoring, scheduling, and monitoring data workflows. The core abstraction in Airflow is the **DAG (Directed Acyclic Graph)** — a collection of tasks with well-defined execution dependencies, represented as a graph where edges point from one task to its dependent task.

#### What is a DAG?

A DAG in Airflow is defined as:
- **Directed**: Dependencies have a direction — Task A must finish before Task B starts.
- **Acyclic**: There are no cycles — you cannot have Task A depend on Task B and Task B depend on Task A. This guarantees the workflow always terminates.
- **Graph**: Tasks are nodes; dependencies are edges.

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG('etl_pipeline', start_date=datetime(2026, 1, 1), schedule_interval='@daily') as dag:

    extract   = PythonOperator(task_id='extract',   python_callable=extract_fn)
    transform = PythonOperator(task_id='transform', python_callable=transform_fn)
    load      = PythonOperator(task_id='load',      python_callable=load_fn)

    extract >> transform >> load  # Defines the dependency chain
```

Airflow renders this as a visual graph in its web UI, showing task status (running, success, failed, skipped) in real time.

#### Airflow Architecture

| Component | Role |
|-----------|------|
| **DAG File** | Python script defining tasks and dependencies |
| **Scheduler** | Parses DAG files, triggers tasks when their dependencies are met |
| **Executor** | Runs tasks (LocalExecutor, CeleryExecutor, KubernetesExecutor) |
| **Workers** | Processes that actually execute task code |
| **Metadata Database** | Stores DAG run history, task states, logs (PostgreSQL or MySQL) |
| **Web UI** | Visual interface to monitor, retry, and trigger DAG runs |

#### DAG Capabilities That Enable Complex Orchestration

**1. Parallel Execution**
Tasks without dependencies on each other can run simultaneously:

```python
# extract_A and extract_B run in parallel; transform waits for both
[extract_A, extract_B] >> transform >> load
```

In a linear script, all operations run sequentially — even independent ones. This can waste hours in a data pipeline with multiple independent data source extracts.

**2. Conditional Branching**
`BranchPythonOperator` allows the workflow to follow different paths based on runtime conditions:

```python
def choose_path(**ctx):
    if data_volume > threshold:
        return 'heavy_processing'
    return 'light_processing'

branch = BranchPythonOperator(task_id='branch', python_callable=choose_path)
branch >> [heavy_task, light_task]
```

**3. Retry Logic and Alerting**
Each task can be configured independently:
```python
PythonOperator(
    task_id='load_to_warehouse',
    retries=3,
    retry_delay=timedelta(minutes=5),
    on_failure_callback=send_slack_alert,
    ...
)
```
In a shell script, implementing retries and alerting requires error-prone manual boilerplate.

**4. Dynamic DAGs**
DAGs can be generated programmatically — for example, creating one DAG per country from a config file, enabling parameterised, reusable workflows without code duplication.

**5. Backfilling**
Airflow can re-run a DAG for past dates (`airflow dags backfill -s 2026-01-01 -e 2026-04-01 my_dag`), enabling historical reprocessing when a bug is fixed or a new transformation is added.

**6. XCom (Cross-task Communication)**
Tasks can pass small values to downstream tasks via XCom (key-value store in the metadata database), enabling data-driven decision-making within a DAG.

#### Linear Script vs. Airflow DAG

| Feature | Bash/Python Script | Airflow DAG |
|---------|-------------------|-------------|
| Parallelism | Manual (threads/subprocesses) | Built-in (task-level) |
| Retry on failure | Manual try/except | Per-task configuration |
| Scheduling | Cron (no history) | Built-in scheduler + full run history |
| Monitoring | Log files | Web UI with task-level status |
| Dependency management | Implicit (code order) | Explicit (graph edges) |
| Backfilling | Manual re-run | Built-in `backfill` command |
| Branching | if/else in code | `BranchPythonOperator` |
| Audit trail | None | Full run history in metadata DB |

#### Real-World Example: Daily Data Pipeline

An analytics company runs a daily ETL pipeline:
1. **Extract** from 4 source systems (Salesforce, MySQL, S3, Google Analytics)
2. **Transform** each source independently
3. **Join** all transformed datasets
4. **Load** into the data warehouse
5. **Notify** the data team on completion

In a script, this runs entirely sequentially. In an Airflow DAG, steps 1–2 for all four sources run in parallel (8 tasks simultaneously), reducing total pipeline time by 60%.

#### Conclusion

The DAG model in Airflow provides a fundamentally richer orchestration framework than linear scripts. Its explicit dependency graph enables parallel execution, conditional branching, per-task retries, visual monitoring, and historical backfilling — all of which are essential in production data engineering environments where reliability, observability, and efficiency are non-negotiable.

---

### Q4. (Evaluate – L5)

# Assess the integration of Apache Kafka with tools like Spark and Airflow. Evaluate the benefits for building end-to-end data pipelines in enterprise settings.

#### Introduction

Modern enterprise data pipelines require three core capabilities: real-time data transport, scalable data processing, and reliable workflow orchestration. Apache Kafka, Apache Spark, and Apache Airflow each excel in one of these areas, and their integration forms one of the most widely deployed enterprise data architectures in use today.

#### The Role of Each Component

| Tool | Role | Strength |
|------|------|----------|
| **Apache Kafka** | Message broker / event bus | High-throughput, durable, replayable data transport |
| **Apache Spark** | Distributed processing engine | Scalable batch and streaming computation |
| **Apache Airflow** | Workflow orchestrator | Dependency-aware scheduling and monitoring |

#### Kafka + Spark Integration

Spark Structured Streaming has native Kafka integration via the `spark-kafka` connector. Spark reads from Kafka topics as streaming DataFrames and processes them in micro-batches:

```python
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders") \
    .load()
```

**Benefits of this integration:**
1. **Decoupled ingestion and processing**: Kafka buffers data, meaning Spark can fall behind during a spike and catch up without losing data.
2. **Replay capability**: If a bug is found in the Spark processing logic, the Kafka topic can be replayed from offset zero to reprocess historical data.
3. **Backpressure handling**: Spark can slow down its consumption rate automatically if the cluster is under load — Kafka absorbs the backlog.
4. **Exactly-once semantics**: Using Kafka transactions and Spark checkpointing together, it is possible to guarantee that each message is processed exactly once — critical for financial applications.

#### Kafka + Airflow Integration

Airflow uses Kafka-specific operators and sensors to incorporate Kafka into orchestrated workflows:

- **`KafkaProducerOperator`**: Publishes a message to a Kafka topic as part of a DAG (e.g., trigger a downstream system by publishing an event).
- **`KafkaSensor`** / **`KafkaConsumerTrigger`**: Waits for a specific message to appear in a Kafka topic before proceeding with the next DAG task.

**Benefits:**
1. **Event-driven triggering**: An Airflow DAG can be triggered when a Kafka event arrives (e.g., "a new data file is available"), rather than relying on a fixed cron schedule.
2. **Bridging batch and streaming**: Airflow orchestrates batch Spark jobs that consume from Kafka — allowing hybrid architectures where real-time ingestion feeds periodic batch analytics.

#### End-to-End Enterprise Pipeline Example

**Use case:** A retail company wants to:
1. Ingest real-time sales transactions
2. Compute hourly revenue summaries
3. Load results into a data warehouse nightly
4. Alert the finance team if daily revenue drops below a threshold

**Architecture:**

```
[POS Systems & Web Store]
        │ (transactions in real-time)
        ▼
[Kafka — topic: "sales-events"]
        │
   ┌────┴─────────────────────────────────────┐
   │                                          │
   ▼                                          ▼
[Spark Structured Streaming]         [Airflow DAG — nightly]
  Windowed hourly aggregations          1. KafkaSensor: wait for
  → writes to PostgreSQL                   "daily-close" event
  (real-time dashboard)                 2. SparkSubmitOperator:
                                           Run batch Spark job
                                           (daily revenue roll-up)
                                        3. S3ToRedshiftOperator:
                                           Load to data warehouse
                                        4. EmailOperator:
                                           Alert if revenue < target
```

**Benefits delivered in this architecture:**

| Benefit | Description |
|---------|-------------|
| **Fault tolerance** | Kafka retains data; Spark checkpoints state; Airflow retries failed tasks |
| **Scalability** | Each component scales independently: add Kafka brokers, Spark executors, or Airflow workers separately |
| **Decoupling** | POS systems don't know about Spark or Airflow; Kafka is the single integration point |
| **Observability** | Airflow UI shows task-level execution history; Kafka consumer lag metrics reveal processing delays |
| **Hybrid processing** | Real-time streaming (Spark + Kafka) and batch orchestration (Airflow) coexist on the same data |

#### Potential Challenges

1. **Operational complexity**: Running three distributed systems (Kafka, Spark, Airflow) requires deep expertise in each. Incorrect configuration (e.g., wrong replication factor, Spark executor memory) can cascade into failures.
2. **Version compatibility**: Major versions of Kafka, Spark, and Airflow must be carefully matched. Breaking API changes are common across releases.
3. **Latency vs. correctness trade-off**: Achieving exactly-once semantics across all three systems simultaneously requires careful configuration that can reduce throughput.
4. **Cost**: Infrastructure for a production-grade deployment of all three systems (with HA and redundancy) is significant.

#### Conclusion

The integration of Kafka, Spark, and Airflow forms the backbone of modern enterprise data pipelines. Kafka provides durable, real-time data transport; Spark delivers scalable distributed processing for both streaming and batch; and Airflow ensures complex workflows are reliably orchestrated, monitored, and retried. Together, they enable organisations to build end-to-end, fault-tolerant, hybrid data architectures that serve both operational and analytical needs simultaneously.

---

### Q5. (Create – L6)

# Propose a conceptual architecture for a data ingestion system using multiple Kafka brokers, producers, and consumers, ensuring fault tolerance and scalability in a large-scale log aggregation platform.

#### Introduction

Large-scale log aggregation is one of the most demanding use cases for any messaging platform. At organisations like Google, Amazon, or any major SaaS provider, thousands of services generate billions of log lines per day. These logs must be ingested reliably, processed in near-real-time, and stored durably — with zero tolerance for data loss.

#### System Requirements

| Requirement | Target |
|-------------|--------|
| Throughput | 1 million log messages / second |
| Latency | Log available for consumption within 2 seconds of generation |
| Fault tolerance | No data loss if up to 2 brokers fail simultaneously |
| Scalability | Add capacity without downtime |
| Retention | Logs retained for 14 days for replay and audit |
| Consumer diversity | Multiple teams consume logs for different purposes |

#### Proposed Architecture

```
[ Services — Producers ]
Microservice-A  Microservice-B  Microservice-C  ... (1000s of services)
      │               │               │
      └───────────────┼───────────────┘
                      │  (structured JSON logs)
                      ▼
        ┌─────────────────────────────┐
        │  Kafka Cluster (9 Brokers)  │
        │                             │
        │  Topic: "app-logs"          │
        │    Partitions: 90           │
        │    Replication Factor: 3    │
        │                             │
        │  Topic: "error-logs"        │
        │    Partitions: 30           │
        │    Replication Factor: 3    │
        │                             │
        │  Topic: "audit-logs"        │
        │    Partitions: 30           │
        │    Replication Factor: 3    │
        └─────────────┬───────────────┘
                      │
     ┌────────────────┼────────────────────────────────┐
     │                │                                │
     ▼                ▼                                ▼
[Consumer Group 1]  [Consumer Group 2]      [Consumer Group 3]
"log-storage"       "log-analytics"         "error-alerting"
 (Spark → S3/HDFS)  (Elasticsearch)         (PagerDuty / Slack)
 Long-term storage  Full-text search         Immediate alerts
```

#### Layer 1 — Producers (Service-Side)

Every microservice runs an embedded **Kafka Producer client** (via a shared logging library) that:
- Serialises log records as structured JSON with `service_name`, `severity`, `message`, `timestamp`, `trace_id`.
- Routes to the appropriate topic based on log severity: `INFO/DEBUG` → `app-logs`; `ERROR/CRITICAL` → `error-logs`; business events → `audit-logs`.
- Uses **`acks=all`** (wait for all in-sync replicas) for `error-logs` and `audit-logs` to ensure no critical logs are lost.
- Uses **`acks=1`** for high-volume `app-logs` to maximise throughput (some loss tolerable for debug logs).
- Uses **`linger.ms=10`** and **`batch.size=65536`** to batch small messages, reducing broker request overhead.

#### Layer 2 — Kafka Cluster (Fault-Tolerant Core)

**Broker setup:**
- 9 brokers across 3 availability zones (3 brokers per zone)
- All topics use **replication factor = 3**, ensuring data survives loss of any single broker or any entire AZ
- **Rack-aware partition assignment** ensures replicas are distributed across AZs

**Fault tolerance mechanisms:**

| Mechanism | How it works |
|-----------|-------------|
| **In-Sync Replicas (ISR)** | Only replicas that are fully caught up are in the ISR. If a leader fails, the new leader is elected from ISR only — no data loss |
| **`min.insync.replicas=2`** | A produce request is only acknowledged if at least 2 replicas have written the message. Even with `acks=all`, a single replica going offline does not block writes |
| **ZooKeeper / KRaft** | Manages broker health, leader election, and cluster metadata. If a broker stops sending heartbeats, ZooKeeper triggers leader re-election within 30 seconds |
| **Log Compaction** | For `audit-logs`, log compaction retains the latest message per key — ensuring critical audit events are never evicted even after the retention period |
| **Producer Idempotence** | Enables exactly-once delivery per producer session by assigning sequence numbers to messages and deduplicating retries at the broker |

**Scalability:**
- Adding a new broker automatically triggers **partition rebalancing** — the cluster rebalances leadership across the new broker using Kafka's partition reassignment tool.
- Partitions are the unit of parallelism: `app-logs` has 90 partitions, allowing up to 90 simultaneous consumers in a single group.

#### Layer 3 — Consumer Groups

**Consumer Group 1 — Log Storage (Spark → Object Storage)**
- 30 Spark Structured Streaming tasks consume `app-logs` in parallel.
- Micro-batch every 30 seconds; writes Parquet files to S3/HDFS partitioned by `date/service/severity`.
- Checkpointing ensures no log is lost or duplicated even if Spark tasks fail mid-batch.
- After 14 days, old Kafka segments are deleted; S3/HDFS becomes the long-term archive.

**Consumer Group 2 — Search & Analytics (Elasticsearch)**
- 15 consumer instances index log records into Elasticsearch for full-text search and Kibana dashboards.
- This group consumes `app-logs` independently of Group 1 — Kafka serves both from the same partitions without duplication of data in the broker.

**Consumer Group 3 — Error Alerting**
- 5 lightweight consumers read exclusively from `error-logs`.
- Each `CRITICAL` log triggers a PagerDuty alert; `ERROR` logs above a threshold rate trigger a Slack notification.
- Because this group only reads `error-logs`, it is isolated from the high-volume `app-logs` traffic.

#### Handling Failures

| Failure Scenario | System Response |
|------------------|----------------|
| One broker fails | ZooKeeper elects new partition leaders from ISR within 30 seconds; producers retry automatically |
| One AZ goes down (3 brokers) | Remaining 6 brokers in 2 AZs continue operating; all partitions have replicas in the surviving AZs |
| Consumer crashes | Kafka remembers committed offsets; the replacement consumer resumes from the last committed offset — no data is lost or reprocessed |
| Producer spikes | Kafka absorbs backlog; consumers catch up at their own pace |

#### Scalability Path

| Growth Need | Action |
|-------------|--------|
| 2× message volume | Add 3 more brokers; increase `app-logs` partitions to 180 |
| New team needs logs | Create a new Consumer Group — zero impact on existing groups |
| Need lower consumer latency | Add more consumer instances to the group (up to one per partition) |
| Global expansion | Deploy a second Kafka cluster in a new region; use MirrorMaker 2 for cross-region replication |

#### Conclusion

This multi-broker Kafka architecture provides the throughput, fault tolerance, and scalability required for a large-scale log aggregation platform. Replication factor 3 with ISR guarantees no data loss across broker or AZ failures. Topic partitioning enables horizontal scaling of both producers and consumers independently. Multiple consumer groups allow diverse teams to consume the same log streams for storage, analytics, and alerting simultaneously — without interference and without duplicating broker-side data.

---

*End of Answer Sheet — Module 3 & 4*


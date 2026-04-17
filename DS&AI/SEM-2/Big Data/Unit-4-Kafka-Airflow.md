# Unit 4 – Apache Kafka & Apache Airflow Study Notes

---

## 1. Introduction to Apache Kafka

### Definition
Apache Kafka is an **open-source distributed event streaming platform** developed by LinkedIn and later donated to the Apache Software Foundation. It is designed to handle **high-throughput, fault-tolerant, real-time data streams**.

### Key Characteristics
- **Distributed**: Runs across multiple machines (brokers)
- **Durable**: Messages are persisted on disk
- **Scalable**: Handles millions of messages per second
- **Fault-tolerant**: Data is replicated across brokers
- **Decoupled**: Producers and consumers are independent

### Real-World Use Cases
- **Log aggregation**: Collecting logs from multiple services
- **Event streaming**: Real-time user activity tracking (e.g., Netflix, Uber)
- **Data pipelines**: Moving data between systems reliably
- **Fraud detection**: Streaming transactions for real-time analysis

### Important Points (Exam Focus)
- Kafka was originally built at **LinkedIn** to handle activity streams
- Kafka is **not a message queue** in the traditional sense — it is a **commit log / event log**
- Messages in Kafka are stored for a configurable **retention period** (default: 7 days)
- Kafka uses a **publish-subscribe** model

---

## 2. Kafka Cluster Architecture

### Definition
A **Kafka Cluster** is a group of one or more Kafka brokers (servers) working together to manage, store, and distribute message streams.

### Architecture Diagram (Text-Based)

```
Producers
   |
   v
+------------------------------------------+
|           Kafka Cluster                  |
|  +--------+  +--------+  +--------+     |
|  |Broker 1|  |Broker 2|  |Broker 3|     |
|  | Topics |  | Topics |  | Topics |     |
|  |Partition| |Partition| |Partition|    |
|  +--------+  +--------+  +--------+     |
|                                          |
|         ZooKeeper / KRaft                |
|   (Cluster Metadata & Coordination)      |
+------------------------------------------+
   |
   v
Consumers / Consumer Groups
```

### Key Components of Kafka Architecture

| Component | Role |
|-----------|------|
| **Broker** | A Kafka server that stores and serves messages |
| **Topic** | A named category/feed to which messages are published |
| **Partition** | A topic is split into partitions for parallelism |
| **Offset** | A unique sequential ID for each message within a partition |
| **Producer** | Sends/publishes messages to topics |
| **Consumer** | Reads/subscribes to messages from topics |
| **Consumer Group** | A set of consumers that jointly consume a topic |
| **ZooKeeper / KRaft** | Manages cluster metadata, leader election |
| **Replica** | Copy of a partition stored on another broker for fault tolerance |
| **Leader** | The broker that handles all reads/writes for a partition |
| **Follower** | Brokers that replicate the leader's data |

### Workflow / Working
1. **Producer** sends a message to a **Topic**
2. The topic is split into **Partitions** distributed across brokers
3. Each message gets an **Offset** (position number) within a partition
4. **Consumers** poll the topic and track their offset
5. **ZooKeeper** (or KRaft in newer versions) coordinates cluster metadata

### Important Points (Exam Focus)
- A **partition** is the unit of **parallelism** in Kafka
- Each partition has one **leader** and zero or more **followers**
- **Replication factor** determines how many copies exist (e.g., replication-factor=3 means 3 copies)
- **ZooKeeper** was traditionally used for coordination; newer Kafka uses **KRaft** (Kafka Raft)

---

## 3. Kafka Messaging System

### Definition
Kafka's messaging system is based on a **publish-subscribe model** where producers write messages to topics, and consumers read from those topics independently.

### Messaging Models
1. **Point-to-Point (Queue)**: One message → One consumer (traditional queuing)
2. **Publish-Subscribe (Kafka's model)**: One message → Multiple consumers can read independently

### Components in Messaging

| Component | Description |
|-----------|-------------|
| **Message** | The unit of data — a key-value pair with optional metadata |
| **Topic** | A logical channel/category to organize messages |
| **Partition** | Physical segment of a topic; enables parallel processing |
| **Offset** | Integer index uniquely identifying a message in a partition |
| **Broker** | Server that holds the messages |
| **Producer** | Application that publishes messages |
| **Consumer** | Application that subscribes and reads messages |

### Message Structure
```
Message = {
  Key:       (optional, used for partitioning)
  Value:     (the actual data/payload)
  Timestamp: (when the message was created)
  Headers:   (optional metadata)
}
```

### Important Points (Exam Focus)
- Messages in Kafka are **immutable** — once written, they cannot be changed
- Messages are **ordered within a partition** but not across partitions
- Kafka uses **zero-copy** mechanism for fast data transfer
- **Key-based partitioning**: messages with the same key always go to the same partition

---

## 4. Creating and Deleting Kafka Topics

### Definition
A **Kafka Topic** is a named stream of records (messages). Topics are the core abstraction in Kafka for organizing data.

### Topic Properties
- **Partitions**: Number of parallel segments
- **Replication Factor**: Number of copies of each partition
- **Retention Period**: How long messages are kept

### Creating a Topic (CLI)
```bash
# Create a topic named "orders" with 3 partitions and replication factor 1
kafka-topics.sh --create \
  --topic orders \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

### Listing Topics
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

### Describing a Topic
```bash
kafka-topics.sh --describe --topic orders --bootstrap-server localhost:9092
```

### Deleting a Topic
```bash
kafka-topics.sh --delete --topic orders --bootstrap-server localhost:9092
```
> Note: `delete.topic.enable=true` must be set in `server.properties` for deletion to work.

### Important Points (Exam Focus)
- More partitions = more parallelism but more overhead
- Replication factor should be **≤ number of brokers**
- Deleting a topic is **irreversible** — all data is lost
- Topics are identified by unique names (case-sensitive)

---

## 5. Creating Multiple Brokers

### Definition
Running **multiple brokers** in a Kafka cluster provides **fault tolerance** and **horizontal scalability**. Each broker is a separate Kafka server process with a unique ID.

### Conceptual Setup
- Each broker has a unique **broker.id** in its config file
- All brokers connect to the **same ZooKeeper** instance
- Partitions are distributed across brokers automatically

### Key Configuration per Broker (`server.properties`)
```properties
broker.id=1               # Unique ID for each broker
listeners=PLAINTEXT://:9093    # Different port per broker
log.dirs=/tmp/kafka-logs-1     # Different log dir per broker
zookeeper.connect=localhost:2181
```

### Broker Roles
- **Leader**: Handles all reads and writes for a partition
- **Follower**: Replicates data from the leader; takes over if leader fails
- **Controller**: Special broker that manages leader elections (one per cluster)

### Benefits of Multiple Brokers
- **High Availability**: If one broker fails, others continue serving
- **Load Distribution**: Partitions spread across brokers
- **Scalability**: Add more brokers as data grows

### Important Points (Exam Focus)
- **ISR (In-Sync Replicas)**: Set of replicas fully caught up with the leader
- If a leader fails, one of the ISR followers is elected as new leader
- Minimum recommended brokers for production: **3**

---

## 6. Kafka Producers

### Definition
A **Kafka Producer** is a client application that **publishes (writes) messages** to Kafka topics. The producer decides which partition to send each message to.

### How a Producer Works
1. Producer creates a `ProducerRecord` with topic, key, value
2. Serializer converts the key and value to bytes
3. **Partitioner** determines which partition to send to
4. Messages are batched and sent to the broker
5. Broker acknowledges receipt (based on `acks` config)

### Partitioning Strategy
- **With a key**: Messages with the same key always go to the same partition (consistent hashing)
- **Without a key**: Messages are distributed round-robin across partitions

### Producer Configuration (Key Parameters)
| Parameter | Description |
|-----------|-------------|
| `bootstrap.servers` | Kafka broker addresses |
| `key.serializer` | Serializer for message key |
| `value.serializer` | Serializer for message value |
| `acks` | Acknowledgment level (0, 1, all) |
| `retries` | Number of retry attempts on failure |
| `batch.size` | Size of message batches |
| `linger.ms` | Wait time before sending a batch |

### Acknowledgment Levels (`acks`)
| Value | Meaning |
|-------|---------|
| `0` | No acknowledgment (fastest, risk of data loss) |
| `1` | Leader acknowledges (default) |
| `all` | All in-sync replicas acknowledge (slowest, safest) |

### Producer API (Python – `kafka-python`)
```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)

producer.send('orders', value='order_001')
producer.flush()
producer.close()
```

### Important Points (Exam Focus)
- Producer is **asynchronous by default** — does not wait for broker response
- `acks=all` provides **strongest durability guarantee**
- **Idempotent producer** (`enable.idempotence=true`) prevents duplicate messages on retry

---

## 7. Three Ways to Send Kafka Messages

### Overview
There are three main strategies a producer can use to send messages:

---

### Method 1: Fire-and-Forget
- **What it does**: Sends the message and does NOT wait for acknowledgment
- **Use when**: Speed is critical and occasional data loss is acceptable
- **Risk**: If delivery fails, no error is raised; message may be lost

```python
producer.send('topic', value='message')
# No callback, no get() — just fire and forget
```

---

### Method 2: Synchronous Send
- **What it does**: Sends the message and **waits (blocks)** until a response is received
- **Use when**: Guaranteed delivery is required, and latency is acceptable
- **Risk**: Slower throughput; producer blocks until broker responds

```python
future = producer.send('topic', value='message')
result = future.get(timeout=10)  # Blocks until acknowledged
print(f"Sent to partition {result.partition}, offset {result.offset}")
```

---

### Method 3: Asynchronous Send (with Callback)
- **What it does**: Sends the message and provides a **callback function** for success/failure
- **Use when**: High throughput is needed with error handling
- **Best of both worlds**: Non-blocking but still handles errors

```python
def on_send_success(record_metadata):
    print(f"Partition: {record_metadata.partition}, Offset: {record_metadata.offset}")

def on_send_error(excp):
    print(f"Error: {excp}")

producer.send('topic', value='message') \
        .add_callback(on_send_success) \
        .add_errback(on_send_error)
```

### Summary Comparison

| Method | Blocking? | Error Handling | Speed |
|--------|-----------|----------------|-------|
| Fire-and-Forget | No | None | Fastest |
| Synchronous | Yes | Immediate | Slowest |
| Asynchronous (Callback) | No | Via callback | Fast |

---

## 8. Kafka Consumers

### Definition
A **Kafka Consumer** is a client application that **subscribes to topics and reads (polls) messages** from Kafka brokers. Consumers track their position using **offsets**.

### How a Consumer Works
1. Consumer subscribes to one or more topics
2. Consumer **polls** the broker for new messages
3. Each message has an **offset** (position) in a partition
4. After processing, the consumer **commits the offset** to track progress
5. On restart, consumer resumes from the last committed offset

### Consumer Configuration (Key Parameters)
| Parameter | Description |
|-----------|-------------|
| `bootstrap.servers` | Kafka broker addresses |
| `group.id` | Consumer group identifier |
| `key.deserializer` | Deserializer for message key |
| `value.deserializer` | Deserializer for message value |
| `auto.offset.reset` | Where to start if no offset exists (`earliest`/`latest`) |
| `enable.auto.commit` | Automatically commit offsets (default: true) |

### Offset Management
- **Auto Commit**: Kafka automatically commits offset at intervals
- **Manual Commit**: Consumer explicitly calls `commit()` after processing
  - `commitSync()`: Blocking commit
  - `commitAsync()`: Non-blocking commit

### Consumer API (Python – `kafka-python`)
```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='order-processor',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: m.decode('utf-8')
)

for message in consumer:
    print(f"Partition: {message.partition}, Offset: {message.offset}")
    print(f"Value: {message.value}")
```

### Important Points (Exam Focus)
- Consumer reads are **non-destructive** — messages remain after being read
- **`auto.offset.reset=earliest`**: Read from the beginning if no offset saved
- **`auto.offset.reset=latest`**: Start from newest messages only
- Consumers in the **same group** share partitions; consumers in **different groups** each get all messages

---

## 9. Consumer Groups

### Definition
A **Consumer Group** is a collection of consumers that work together to consume messages from a topic. Kafka distributes partitions among members of the group.

### How Consumer Groups Work

```
Topic: orders (3 partitions: P0, P1, P2)

Consumer Group A (3 consumers):
  Consumer-1 → P0
  Consumer-2 → P1
  Consumer-3 → P2

Consumer Group B (1 consumer):
  Consumer-1 → P0, P1, P2  (all partitions)
```

### Key Rules
- Each **partition** is assigned to **exactly one consumer** in a group
- If consumers > partitions: some consumers are **idle**
- If consumers < partitions: some consumers handle **multiple partitions**
- Different consumer groups are **independent** — they each maintain their own offsets

### Rebalancing
When a consumer joins or leaves a group, Kafka **rebalances** partition assignments automatically.

### Group Coordinator
- A designated broker (the **Group Coordinator**) manages group membership
- Tracks offsets for each consumer group in a special internal topic: `__consumer_offsets`

### Benefits of Consumer Groups
- **Parallel processing**: Multiple consumers process data concurrently
- **Fault tolerance**: If one consumer fails, its partitions are reassigned
- **Scalability**: Add more consumers to speed up processing

### Important Points (Exam Focus)
- Consumer groups enable **horizontal scaling** of consumers
- Offsets are stored **per group per partition** — enabling independent consumption
- A single topic can be consumed by **multiple groups simultaneously**

---

## 10. Kafka Integration with Apache Spark

### Definition
**Kafka + Spark Streaming** (or Spark Structured Streaming) allows real-time processing of Kafka event streams using Spark's distributed computing engine.

### Why Integrate?
- Kafka is excellent at **ingesting** high-volume streams
- Spark is excellent at **processing** streams with complex transformations
- Together they form a powerful **real-time data pipeline**

### Architecture

```
Data Sources → Kafka (Ingestion) → Spark Streaming (Processing) → Output (DB/Dashboard/Storage)
```

### How It Works
1. Spark subscribes to Kafka topics as a **streaming source**
2. Kafka delivers micro-batches of messages to Spark
3. Spark processes each batch (filter, aggregate, transform)
4. Results are written to sinks (HDFS, databases, dashboards)

### Spark Structured Streaming – Kafka Example
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaSparkIntegration") \
    .getOrCreate()

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .load()

# Process: decode value from bytes
from pyspark.sql.functions import col
messages = df.select(col("value").cast("string"))

# Write output to console
query = messages.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
```

### Use Cases
- Real-time fraud detection on financial transactions
- Live dashboard updates from IoT sensor streams
- Log analysis pipelines in distributed systems

### Important Points (Exam Focus)
- Spark consumes Kafka as a **structured streaming source**
- Kafka acts as the **message bus**; Spark does the **computation**
- Output modes: `append`, `complete`, `update`
- Integration uses the `spark-sql-kafka` connector package

---

## 11. Apache Airflow

### Definition
**Apache Airflow** is an open-source **workflow orchestration platform** used to programmatically **author, schedule, and monitor** data pipelines (workflows).

### Key Features
- Workflows are defined as **Python code**
- Uses a **DAG (Directed Acyclic Graph)** to define task dependencies
- Provides a **web UI** for monitoring and managing pipelines
- Supports **schedulers, executors, and workers**

### Core Components
| Component | Role |
|-----------|------|
| **DAG** | Defines the workflow (tasks + dependencies) |
| **Task** | Individual unit of work (e.g., run a script, call an API) |
| **Operator** | Template for a task (BashOperator, PythonOperator, etc.) |
| **Scheduler** | Triggers DAG runs based on schedules |
| **Executor** | Determines how tasks are executed (Local, Celery, K8s) |
| **Web Server** | Provides the Airflow UI |
| **Metadata Database** | Stores DAG and task state (PostgreSQL/MySQL) |
| **Worker** | Process that executes tasks |

### Real-World Use Cases
- ETL pipelines: Extract → Transform → Load data into a data warehouse
- ML pipelines: Trigger model training after new data arrives
- Daily report generation from databases
- Kafka + Airflow: Trigger Spark jobs when Kafka topics have new data

### Important Points (Exam Focus)
- Airflow is NOT a data streaming tool — it is a **pipeline orchestrator**
- Workflows in Airflow are defined in **Python files** placed in the `dags/` folder
- Each DAG has a **schedule interval** (e.g., daily, hourly, cron expression)
- Airflow is **idempotent** — the same DAG run should produce the same result

---

## 12. Directed Acyclic Graph (DAG)

### Definition
A **DAG (Directed Acyclic Graph)** is a mathematical structure consisting of **nodes (tasks)** and **directed edges (dependencies)** with **no cycles** (no task can depend on itself, directly or indirectly).

### Key Properties
- **Directed**: Arrows show the direction of dependency (A → B means B depends on A)
- **Acyclic**: No circular dependencies (prevents infinite loops)
- **Graph**: Multiple nodes connected by edges

### DAG in Airflow Context

```
[Extract Data] → [Validate Data] → [Transform Data] → [Load to DB]
                       |
                       └──→ [Send Alert Email]
```

### DAG Code Example
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load_task = BashOperator(
        task_id='load',
        bash_command='echo "Loading data..."'
    )

    # Define dependencies
    extract_task >> transform_task >> load_task
```

### Task Dependencies Syntax
```python
task_a >> task_b          # task_b runs after task_a
task_a >> [task_b, task_c]  # task_b and task_c run in parallel after task_a
[task_b, task_c] >> task_d  # task_d runs after both task_b and task_c
```

### Schedule Intervals
| Preset | Meaning |
|--------|---------|
| `@once` | Run once only |
| `@hourly` | Every hour |
| `@daily` | Once per day |
| `@weekly` | Once per week |
| `@monthly` | Once per month |
| `0 6 * * *` | Cron: every day at 6 AM |

### Common Operators
| Operator | Purpose |
|----------|---------|
| `PythonOperator` | Execute a Python function |
| `BashOperator` | Execute a bash command |
| `EmailOperator` | Send an email |
| `HttpSensor` | Wait for an HTTP endpoint to return success |
| `SparkSubmitOperator` | Submit a Spark job |

### Important Points (Exam Focus)
- **Acyclic** means no task can be its own ancestor — prevents infinite loops
- `>>` operator sets downstream dependency; `<<` sets upstream
- DAGs are **triggered** by the scheduler at the defined interval
- **Backfill**: Airflow can run historical DAG runs if `catchup=True`
- `start_date` is when Airflow begins scheduling; first run happens **after** the first interval

---

## 13. Kafka + Airflow Integration

### How They Work Together
- **Airflow** orchestrates the pipeline schedule and dependencies
- **Kafka** handles the real-time data transport between pipeline stages

### Integration Pattern
```
[Kafka Topic: raw-events]
        ↓
[Airflow DAG triggered by sensor or schedule]
        ↓
  [Task 1: Read from Kafka → Process with Spark]
        ↓
  [Task 2: Load results into Data Warehouse]
        ↓
  [Task 3: Send notification / trigger next pipeline]
```

### Use Case: Real-Time ETL Pipeline
1. Kafka collects events from web application
2. Airflow DAG runs every hour
3. DAG triggers a Spark job to read Kafka, aggregate data
4. Results are stored in a database
5. Airflow sends an email alert after completion

---

## 14. CLI Commands

### Kafka CLI Commands

#### Topic Management
```bash
# Start ZooKeeper
zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka broker
kafka-server-start.sh config/server.properties

# Create topic
kafka-topics.sh --create --topic my-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 --replication-factor 1

# List all topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Describe a topic
kafka-topics.sh --describe --topic my-topic \
  --bootstrap-server localhost:9092

# Delete a topic
kafka-topics.sh --delete --topic my-topic \
  --bootstrap-server localhost:9092
```

#### Producer Commands
```bash
# Start a console producer (type messages manually)
kafka-console-producer.sh --topic my-topic \
  --bootstrap-server localhost:9092
```

#### Consumer Commands
```bash
# Start a console consumer (read from beginning)
kafka-console-consumer.sh --topic my-topic \
  --bootstrap-server localhost:9092 \
  --from-beginning

# Read with consumer group
kafka-console-consumer.sh --topic my-topic \
  --bootstrap-server localhost:9092 \
  --group my-group
```

#### Consumer Group Commands
```bash
# List consumer groups
kafka-consumer-groups.sh --list \
  --bootstrap-server localhost:9092

# Describe a consumer group (shows lag)
kafka-consumer-groups.sh --describe \
  --group my-group \
  --bootstrap-server localhost:9092

# Reset offsets for a group
kafka-consumer-groups.sh --reset-offsets \
  --group my-group --topic my-topic \
  --to-earliest --execute \
  --bootstrap-server localhost:9092
```

---

### Airflow CLI Commands

```bash
# Initialize the Airflow metadata database
airflow db init

# Start the web server (default port 8080)
airflow webserver --port 8080

# Start the scheduler
airflow scheduler

# List all DAGs
airflow dags list

# Trigger a DAG run manually
airflow dags trigger etl_pipeline

# Pause a DAG
airflow dags pause etl_pipeline

# Unpause a DAG
airflow dags unpause etl_pipeline

# List tasks in a DAG
airflow tasks list etl_pipeline

# Test a specific task
airflow tasks test etl_pipeline extract 2024-01-01

# Check DAG run state
airflow dags state etl_pipeline 2024-01-01
```

---

## Quick Revision Summary

| Topic | Key Point |
|-------|-----------|
| Kafka | Distributed event streaming platform (publish-subscribe) |
| Broker | Kafka server — stores and serves messages |
| Topic | Named feed/category for messages |
| Partition | Splits a topic for parallelism; messages ordered within partition |
| Offset | Unique sequential ID of a message in a partition |
| Producer | Publishes messages; uses fire-and-forget / sync / async |
| Consumer | Reads messages; tracks position via offsets |
| Consumer Group | Set of consumers sharing topic partitions |
| ZooKeeper/KRaft | Manages cluster metadata and leader elections |
| ISR | In-Sync Replicas — replicas fully caught up with leader |
| Kafka + Spark | Kafka ingests; Spark processes in real-time |
| Airflow | Workflow orchestration via Python-defined DAGs |
| DAG | Directed Acyclic Graph — tasks + dependencies, no cycles |
| Operator | Template for Airflow tasks (Python, Bash, Spark, etc.) |
| Scheduler | Triggers DAG runs at defined intervals |
| `>>` in Airflow | Sets downstream task dependency |

---

*End of Unit 4 Study Notes*

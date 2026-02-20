# Unit 1: Big Data Analytics using Artificial Intelligence Technologies
## Hadoop, HDFS, MapReduce, YARN, Hive

> **References:** Tom White – *Hadoop: The Definitive Guide* | Raj Kamal & Preethi Saxena – *Big Data Analytics*, TMH

---

## Table of Contents

1. [Overview of Hadoop](#1-overview-of-hadoop)
2. [HDFS Architecture](#2-hdfs-architecture)
3. [Hadoop MapReduce](#3-hadoop-mapreduce)
4. [Processing Data with MapReduce](#4-processing-data-with-mapreduce)
5. [YARN Architecture](#5-yarn-architecture)
6. [Anatomy of File Read and Write in Hadoop](#6-anatomy-of-file-read-and-write-in-hadoop)
7. [Hadoop Shell Commands](#7-hadoop-shell-commands)
8. [Overview of Hadoop Ecosystem](#8-overview-of-hadoop-ecosystem)
9. [Apache Hive](#9-apache-hive)
10. [Hive Data Types](#10-hive-data-types)
11. [Create, Alter and Drop Commands](#11-create-alter-and-drop-commands)
12. [Built-in Operators and Functions](#12-built-in-operators-and-functions)
13. [Views](#13-views)
14. [Interaction with Hadoop Framework](#14-interaction-with-hadoop-framework)

---

## 1. Overview of Hadoop

### 1.1 What is Hadoop?

**Apache Hadoop** is an open-source software framework for **distributed storage** and **distributed processing** of very large datasets on computer clusters built from commodity (off-the-shelf) hardware.

It was originally developed by **Doug Cutting** and **Mike Cafarella** in 2005, inspired by Google's **MapReduce** paper (2004) and **Google File System (GFS)** paper (2003). The name "Hadoop" comes from Doug Cutting's son's toy elephant.

### 1.2 Why Hadoop? The Big Data Problem

Traditional relational databases (RDBMS) fail at scale because:

| Problem | Traditional RDBMS | Hadoop Solution |
|---------|------------------|-----------------|
| **Volume** | Scales vertically (bigger server) | Scales horizontally (more nodes) |
| **Variety** | Structured data only | Structured + semi-structured + unstructured |
| **Velocity** | Batch, limited throughput | Distributed parallel batch |
| **Cost** | Expensive hardware + licenses | Commodity hardware + open-source |
| **Fault Tolerance** | Single point of failure | Built-in replication |

### 1.3 Core Principles of Hadoop

1. **Data Locality** — Move computation to where data lives, not the other way around. Reduces network traffic dramatically.
2. **Fault Tolerance** — Hardware failure is expected, not exceptional. Data is automatically replicated (default: 3 copies).
3. **Horizontal Scalability** — Add commodity nodes to increase storage and processing power linearly.
4. **Distributed Processing** — Break large jobs into smaller tasks executed simultaneously across nodes.
5. **Commodity Hardware** — Runs on standard x86 servers (no special hardware needed).

### 1.4 Hadoop Versions

| Version        | Key Feature                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| **Hadoop 1.x** | HDFS + MapReduce (JobTracker/TaskTracker model)                                               |
| **Hadoop 2.x** | Introduced YARN (decoupled resource management); supports non-MapReduce workloads             |
| **Hadoop 3.x** | Erasure coding (reduces storage overhead), YARN Timeline Service v2, support for >2 NameNodes |

### 1.5 Core Components of Hadoop

```
+-----------------------------------------------+
|               HADOOP FRAMEWORK                |
|                                               |
|  +------------------+  +------------------+  |
|  |      HDFS        |  |      YARN        |  |
|  | (Distributed     |  | (Resource Mgmt + |  |
|  |  Storage)        |  |  Job Scheduling) |  |
|  +------------------+  +------------------+  |
|                                               |
|  +------------------+  +------------------+  |
|  |   MapReduce      |  |  Hadoop Common   |  |
|  | (Batch Processing|  |  (Utilities &    |  |
|  |  Framework)      |  |   Libraries)     |  |
|  +------------------+  +------------------+  |
+-----------------------------------------------+
```

- **HDFS** (Hadoop Distributed File System) – Storage layer
- **YARN** (Yet Another Resource Negotiator) – Resource management and job scheduling
- **MapReduce** – Programming model for batch data processing
- **Hadoop Common** – Shared Java libraries, utilities, and OS-level abstractions

### 1.6 Hadoop Cluster

A Hadoop cluster has two types of machines:

- **Master Nodes**: Run management daemons (NameNode, ResourceManager)
- **Worker/Slave Nodes**: Store data and run computation (DataNode, NodeManager)

```
         MASTER NODES
   +---------------------+
   |  NameNode           |   ← HDFS metadata management
   |  ResourceManager    |   ← YARN resource allocation
   |  Secondary NameNode |   ← FsImage/EditLog checkpointing
   +---------------------+

         WORKER NODES (many)
   +---------+ +---------+ +---------+
   |DataNode | |DataNode | |DataNode |
   |NodeMgr  | |NodeMgr  | |NodeMgr  |
   +---------+ +---------+ +---------+
```

---

## 2. HDFS Architecture

### 2.1 What is HDFS?

**HDFS (Hadoop Distributed File System)** is the primary storage system of Hadoop. It is modeled after the **Google File System (GFS)** and designed to:

- Store **very large files** (gigabytes to terabytes per file)
- Provide **high throughput** access (optimized for streaming reads, not low-latency random access)
- Run on **commodity hardware** with automatic fault recovery
- Support **write-once, read-many** access patterns

### 2.2 HDFS Design Assumptions

- Hardware failure is the **norm**, not the exception
- Files are **large** (100 MB to GB) — small file problem exists
- Data access is **streaming** (MapReduce reads sequentially, not randomly)
- **Write-once, read-many** — no in-place edits (append supported in Hadoop 2.x+)
- **Moving computation is cheaper than moving data** — data locality

### 2.3 HDFS Architecture Diagram

```
                     CLIENT
                       |
              +--------+--------+
              |                 |
         (Metadata)          (Data)
              |                 |
    +---------+----------+      |
    |       NameNode     |      |
    |  - File namespace  |      |
    |  - Block → DN map  |      |
    |  - FsImage         |      |
    |  - EditLog         |      |
    +---------+----------+      |
              |                 |
       Heartbeat &              |
       Block Reports            |
              |                 |
    +---------+-------+---------+---------+
    |                 |                   |
+---+-------+  +------+----+  +-----------+---+
| DataNode 1 |  | DataNode 2|  |  DataNode 3   |
| Block A(1) |  | Block A(2)|  |  Block A(3)   |
| Block B(1) |  | Block C(2)|  |  Block B(3)   |
+------------+  +-----------+  +---------------+
   Rack 1           Rack 1          Rack 2
```

### 2.4 HDFS Components

#### 2.4.1 NameNode (Master)

The **NameNode** is the master daemon of HDFS. It manages the **filesystem namespace** and **metadata**.

**Responsibilities:**
- Maintains the directory tree (like an inode table in a traditional filesystem)
- Tracks the mapping of file → blocks → DataNode locations
- Records metadata in two files:
  - **FsImage**: A snapshot of the filesystem at a point in time (persisted to disk)
  - **EditLog**: Journal of recent filesystem changes (append-only log)
- Handles all client requests for metadata (open, close, rename, delete)
- Does **NOT** store actual file data

**Limitation:** Single NameNode = Single Point of Failure (resolved in Hadoop 2.x with HA NameNode)

#### 2.4.2 Secondary NameNode

**NOT a backup NameNode.** Its role is to:
- Periodically merge **FsImage + EditLog** into a new FsImage
- Prevent EditLog from growing too large (which would slow NameNode restarts)
- Can be used as a warm standby in emergencies

> In Hadoop 2.x HA setups, the **Standby NameNode** replaces the Secondary NameNode for true automatic failover.

#### 2.4.3 DataNode (Slave)

DataNodes are the **worker daemons** that actually store file blocks.

**Responsibilities:**
- Store file data as blocks on local disk
- Serve read/write requests from clients
- Send **heartbeats** to the NameNode every 3 seconds (to signal they are alive)
- Send **block reports** to the NameNode periodically (list of all blocks stored)
- Perform block replication as instructed by the NameNode

#### 2.4.4 Blocks

HDFS splits files into fixed-size **blocks**:

| Version | Default Block Size |
|---------|--------------------|
| Hadoop 1.x | 64 MB |
| Hadoop 2.x+ | **128 MB** |

**Why large blocks?**
- Reduces the number of blocks → less metadata in NameNode
- Minimizes seek time as a fraction of transfer time
- Enables high-throughput sequential reads

**Example:** A 512 MB file with 128 MB blocks = 4 blocks. Each block is replicated 3 times → 12 block copies stored across DataNodes.

### 2.5 Replication

HDFS replicates each block (default **replication factor = 3**) across multiple DataNodes:

**Rack-Aware Replica Placement:**
```
1st replica  →  Local DataNode (same as writer, or random)
2nd replica  →  Different DataNode on a different rack
3rd replica  →  Different DataNode on the same rack as the 2nd
```

This placement:
- Tolerates a single node failure (2 replicas remain)
- Tolerates an entire rack failure (1 replica on different rack remains)
- Limits cross-rack bandwidth use (only 1 inter-rack write per block)

### 2.6 HDFS High Availability (HA)

Hadoop 2.x introduced **HA NameNode** using:
- **Active NameNode**: Handles all client requests
- **Standby NameNode**: Synced with Active via a shared edit log (stored in **JournalNodes**)
- **ZooKeeper**: Provides automatic failover — detects Active NameNode failure and promotes Standby

```
Active NameNode ←→ JournalNodes ←→ Standby NameNode
        ↑                                  ↑
        +---------- ZooKeeper ZKFC ---------+
                  (Failover Controller)
```

### 2.7 HDFS Federation (Hadoop 2.x+)

Multiple independent NameNodes each managing a **namespace volume** (subset of the HDFS namespace), sharing the same pool of DataNodes. This:
- Removes NameNode scalability bottleneck
- Allows horizontal scaling of namespace

---

## 3. Hadoop MapReduce

### 3.1 What is MapReduce?

**MapReduce** is a programming model and software framework for processing **large datasets** in parallel across a Hadoop cluster. It was invented by Google (Jeffrey Dean & Sanjay Ghemawat, 2004) and implemented in open-source Hadoop.

It abstracts the complexity of distributed computing by providing two simple functions the programmer implements:
- **Map** – Transform input key-value pairs into intermediate key-value pairs
- **Reduce** – Aggregate intermediate values with the same key

### 3.2 MapReduce Data Flow

```
Input Data (HDFS)
       ↓
  [Input Format]  ← Splits data into InputSplits
       ↓
  [RecordReader]  ← Reads records as key-value pairs
       ↓
   MAP PHASE      ← User-defined map() function
  (map tasks)       emits (intermediate key, value)
       ↓
   SHUFFLE &      ← Framework sorts/groups by key
   SORT PHASE       transfers data to Reducers
       ↓
  REDUCE PHASE    ← User-defined reduce() function
  (reduce tasks)    aggregates values per key
       ↓
  [Output Format] ← Writes results to HDFS
       ↓
  Output (HDFS)
```

### 3.3 Key Concepts

| Term | Definition |
|------|-----------|
| **Job** | A complete MapReduce program (one Map phase + one Reduce phase) |
| **Task** | Individual unit of Map or Reduce work |
| **InputSplit** | A chunk of input data processed by one Map task (≈ one HDFS block) |
| **RecordReader** | Reads data from an InputSplit and converts to key-value pairs |
| **Mapper** | Class containing user-defined `map()` function |
| **Reducer** | Class containing user-defined `reduce()` function |
| **Combiner** | Optional "mini-reducer" on the map side to reduce shuffle data |
| **Partitioner** | Determines which reducer receives which key |
| **Driver** | Main class that configures and submits the job |

### 3.4 MapReduce Architecture (Hadoop 1.x)

```
CLIENT → JobTracker (Master)
              |
    +---------+---------+
    |         |         |
TaskTracker TaskTracker TaskTracker  (Workers)
  [Map][Map]  [Map][Reduce]  [Reduce]
```

**JobTracker:** Master daemon that:
- Accepts job submissions from clients
- Divides jobs into map and reduce tasks
- Assigns tasks to TaskTrackers
- Monitors task progress and handles failures

**TaskTracker:** Worker daemon that:
- Runs on each DataNode (data locality)
- Executes map and reduce tasks in separate JVMs
- Sends progress updates to JobTracker

> **Note:** In Hadoop 2.x, the JobTracker/TaskTracker model is replaced by **YARN + MRAppMaster**.

### 3.5 Phases of MapReduce in Detail

#### Map Phase
- Each map task processes one InputSplit
- Reads records as `(key, value)` pairs via RecordReader
- Calls the user's `map()` function for each record
- Output: intermediate `(key, value)` pairs written to local disk (not HDFS)

#### Shuffle and Sort Phase (Framework-managed)
- **Partitioning**: Each map output is partitioned by key using the Partitioner (default: hash of key % num_reducers)
- **Spilling**: Map outputs are buffered in RAM (io.sort.mb = 100 MB default). When buffer is 80% full, data is spilled to disk.
- **Merging**: Multiple spill files on the map side are merged into one sorted file per partition
- **Copying**: Reducers fetch their partition's data from all map outputs (over the network)
- **Sorting**: Reducer sorts and merges all fetched map outputs by key

#### Reduce Phase
- Reducer receives `(key, Iterable<values>)` — all values for the same key
- Calls the user's `reduce()` function
- Output is written directly to HDFS

### 3.6 Combiner (Optional)

A **Combiner** is a local aggregation step that runs on the Map node's output before shuffle:

```
Map Output:  (word, 1), (word, 1), (word, 1), (the, 1), (the, 1)
After Combiner: (word, 3), (the, 2)   ← Reduces shuffle data significantly
```

- Must be **commutative and associative** (like addition, max, min — not average)
- Behaves like a Reducer but runs locally after each Map task
- Can reduce network transfer by up to 90% for certain jobs
---

### 3.7 MapReduce vs Spark

| Aspect | MapReduce | Apache Spark |
|--------|-----------|--------------|
| **Processing** | Disk-based (writes after every stage) | In-memory |
| **Speed** | Slower for iterative | 10–100x faster |
| **Ease of Use** | Verbose Java API | Concise Python/Scala |
| **Workloads** | Batch only | Batch, streaming, ML, SQL |
| **Fault Tolerance** | Block replication | RDD lineage |
| **Real-time** | No | Yes (Structured Streaming) |

---

## 5. YARN Architecture

### 5.1 Why YARN?

Hadoop 1.x's **JobTracker** was a monolith that handled:
- Resource management (tracking available slots)
- Job scheduling (assigning work)
- Task monitoring and failure handling

This created:
- **Scalability bottleneck**: ~4,000 nodes max
- **Single point of failure**: JobTracker crash = all jobs lost
- **MapReduce-only**: No other frameworks (Spark, Tez) could run natively

**YARN** (Yet Another Resource Negotiator), introduced in **Hadoop 2.0**, solves all these problems by separating resource management from application logic.

### 5.2 YARN Architecture

```
+----------------------------------------------------------+
|                    ResourceManager                       |
|  +------------------------+  +------------------------+  |
|  |      Scheduler         |  |  ApplicationsManager   |  |
|  | (Resource Allocation)  |  | (App Lifecycle Mgmt)   |  |
|  +------------------------+  +------------------------+  |
+---------------------------+------------------------------+
                            |
          +-----------------+------------------+
          |                                    |
+---------+---------+              +-----------+---------+
|    NodeManager 1  |              |    NodeManager 2    |
|  +-------------+  |              |  +-------------+    |
|  | Container 1 |  |              |  | Container 3 |    |
|  | (App task)  |  |              |  | (App task)  |    |
|  +-------------+  |              |  +-------------+    |
|  +-------------+  |              |  +-------------+    |
|  | Container 2 |  |              |  | AppMaster   |    |
|  | (App task)  |  |              |  | Container   |    |
|  +-------------+  |              |  +-------------+    |
+-------------------+              +---------------------+
```

### 5.3 YARN Components

#### 5.3.1 ResourceManager (RM)

The **global master** of the cluster. Has two sub-components:

**a) Scheduler:**
- Pure resource allocator — allocates containers (CPU + memory) to running applications
- Does NOT monitor tasks or restart failed application tasks
- Pluggable scheduling policies:
  - **FIFO Scheduler**: First-come, first-served (simple, inefficient for mixed workloads)
  - **Capacity Scheduler**: Multiple queues with guaranteed capacities (default in most distros)
  - **Fair Scheduler**: Equal share of resources for all applications over time

**b) ApplicationsManager (AsM):**
- Accepts job submissions
- Negotiates the first container (for the ApplicationMaster) from the Scheduler
- Restarts the ApplicationMaster container on failure

#### 5.3.2 NodeManager (NM)

Runs on **every worker node**:
- Manages resources (CPU cores, memory, disk, network) on that node
- Launches and monitors **Containers**
- Reports resource availability and container status to ResourceManager
- Kills containers that exceed their allocated resources

#### 5.3.3 ApplicationMaster (AM)

One **ApplicationMaster per submitted application** (one per Spark job, one per MapReduce job):
- Negotiates with ResourceManager for resource containers
- Instructs NodeManagers to launch application tasks
- Monitors task progress and restarts failed tasks
- Reports application completion to ResourceManager

> This is what enables Spark, Tez, MapReduce, and other frameworks to all run on YARN simultaneously — each has its own AM that understands its framework's needs.

#### 5.3.4 Container

The **fundamental unit of resource allocation** in YARN:
- A bundle of: `vCores (CPU) + Memory (MB)`
- Every task (Map task, Spark executor, etc.) runs inside a Container
- Provides resource isolation between tasks on the same node

### 5.4 YARN Job Submission Workflow

```
Step 1: Client submits application to ResourceManager
Step 2: RM's AsM finds resources for ApplicationMaster
Step 3: RM's Scheduler allocates a Container for the AM on some NodeManager
Step 4: NodeManager launches the ApplicationMaster in the Container
Step 5: AM registers with RM and requests additional Containers for tasks
Step 6: RM's Scheduler allocates Containers; AM gets container assignments
Step 7: AM instructs NodeManagers to launch task Containers
Step 8: Tasks run, report progress to AM
Step 9: AM reports completion to RM; Containers are released
Step 10: RM reclaims resources; application entry removed
```

### ~~5.5 YARN vs Hadoop 1.x~~

| Feature | Hadoop 1.x | Hadoop 2.x (YARN) |
|---------|-----------|-------------------|
| Resource Management | JobTracker | ResourceManager |
| Task Execution | TaskTracker | NodeManager + Containers |
| Application Logic | JobTracker | ApplicationMaster (per app) |
| Frameworks Supported | MapReduce only | MapReduce, Spark, Tez, MPI, etc. |
| Scalability | ~4,000 nodes | 10,000+ nodes |
| Fault Tolerance | JobTracker = SPOF | RM HA + AM restart |
| Resource Model | Fixed slots | Dynamic containers (CPU + RAM) |

### 5.6 ~~YARN Resource Scheduling~~

**Capacity Scheduler** (most common):

```
Root Queue (100%)
  ├── production-queue (60%)
  │    ├── batch-jobs (30%)
  │    └── etl-jobs (30%)
  └── development-queue (40%)
       ├── interactive (25%)
       └── testing (15%)
```

Each queue has:
- **Guaranteed capacity**: Always available
- **Maximum capacity**: Can borrow from idle queues
- **Preemption**: Can reclaim resources from lower-priority apps

---

## 6. Anatomy of File Read and Write in Hadoop

### 6.1 HDFS File Write (Client → HDFS)

When a client writes a file to HDFS:

```
Step 1: Client calls DistributedFileSystem.create()
        → NameNode creates a new file entry in namespace
        → NameNode returns an output stream (FSDataOutputStream → DFSOutputStream)

Step 2: Client writes data to DFSOutputStream
        → Data is split into packets (64 KB)
        → Packets go into a data queue

Step 3: DataStreamer thread picks packets from queue
        → Asks NameNode to allocate a new block
        → NameNode returns list of 3 DataNodes (e.g., DN1, DN2, DN3)
        → DataStreamer sets up a pipeline: Client → DN1 → DN2 → DN3

Step 4: Data flows through the pipeline
        → Client sends packet to DN1
        → DN1 forwards to DN2
        → DN2 forwards to DN3
        → Each DN writes packet to disk

Step 5: Acknowledgments flow back: DN3 → DN2 → DN1 → Client
        → Client advances to next packet only after ACK received

Step 6: When block is full, pipeline is closed
        → Client requests next block from NameNode (new DN list)
        → Process repeats for each block

Step 7: Client calls close()
        → All remaining packets are flushed
        → Client notifies NameNode that write is complete
        → NameNode marks file as complete
```

**Write Pipeline Diagram:**
```
Client → [DN1] → [DN2] → [DN3]    (data flows left to right)
       ←  ACK  ←  ACK  ←  ACK    (acknowledgments flow right to left)
```

**Fault Handling During Write:**
- If a DataNode fails mid-pipeline:
  1. Pipeline is closed
  2. Good packets (not yet ACKed by failed DN) are re-added to the data queue
  3. Remaining healthy DataNodes are reconnected in a new pipeline
  4. NameNode is informed of the under-replicated block and schedules re-replication later

### 6.2 HDFS File Read (HDFS → Client)

When a client reads a file from HDFS:

```
Step 1: Client calls DistributedFileSystem.open()
        → Client contacts NameNode with filename
        → NameNode returns list of blocks + DataNode locations for each block
          (sorted by network proximity to client using rack topology)
        → Returns FSDataInputStream (wrapping DFSInputStream)

Step 2: Client calls read() on DFSInputStream
        → DFSInputStream connects to the nearest DataNode for Block 1
        → Data is streamed from DataNode to client

Step 3: When Block 1 is fully read, DFSInputStream closes that connection
        → Contacts nearest DataNode for Block 2
        → Repeats for all blocks

Step 4: Client calls close() when all data is read

During Read: Checksums are verified for every packet
             If checksum fails → try next replica of that block
             If DataNode fails → transparent failover to next replica
```

**Read Diagram:**
```
                         NameNode
                        /
Client ←──metadata──── /
  |
  |───Block 1 request──→ DN3 (nearest)
  |←──Block 1 data──────
  |
  |───Block 2 request──→ DN1 (nearest for this block)
  |←──Block 2 data──────
```

### 6.3 Coherency Model

HDFS has a **relaxed coherency model**:
- After a write, the data is not immediately visible to readers (current block being written is not visible)
- `hflush()` forces all buffered data to DataNodes (visible to new readers)
- `hsync()` forces data to disk on DataNodes (durable)
- After `close()`, the complete file is fully visible

### 6.4 Key Points Summary

| Operation | Key Mechanism |
|-----------|--------------|
| **Write** | Pipeline replication (Client → DN1 → DN2 → DN3) |
| **Read** | Direct from nearest DataNode (rack-aware selection) |
| **Fault in Write** | Pipeline reconstruction, NameNode re-replicates |
| **Fault in Read** | Transparent failover to next replica |
| **Integrity** | Checksums on every block (CRC32) |
| **Visibility** | New data visible only after `hflush()`/`close()` |

---

## 7. Hadoop Shell Commands

Hadoop provides a shell interface for interacting with HDFS using the `hadoop fs` or `hdfs dfs` commands.

**Syntax:**
```
hadoop fs -<command> [arguments]
hdfs dfs -<command> [arguments]    ← preferred in Hadoop 2.x+
```

### 7.1 File System Commands

#### Listing and Navigation

```bash
# List files in HDFS root
hdfs dfs -ls /

# List files in a specific directory
hdfs dfs -ls /user/hadoop/

# List recursively
hdfs dfs -ls -R /user/hadoop/

# Print working directory
hdfs dfs -pwd
```

#### Creating Directories

```bash
# Create directory
hdfs dfs -mkdir /user/hadoop/data

# Create directory with parents (like mkdir -p)
hdfs dfs -mkdir -p /user/hadoop/project/input
```

#### Uploading Files (Local → HDFS)

```bash
# Copy from local to HDFS
hdfs dfs -put /local/path/file.txt /hdfs/path/

# Copy from local to HDFS (alias for put)
hdfs dfs -copyFromLocal /local/file.txt /hdfs/path/

# Move from local to HDFS (deletes local file)
hdfs dfs -moveFromLocal /local/file.txt /hdfs/path/
```

#### Downloading Files (HDFS → Local)

```bash
# Copy from HDFS to local
hdfs dfs -get /hdfs/path/file.txt /local/path/

# Copy from HDFS to local (alias for get)
hdfs dfs -copyToLocal /hdfs/path/file.txt /local/path/

# Merge multiple HDFS files and download as one
hdfs dfs -getmerge /hdfs/output/ /local/merged.txt
```

#### Viewing File Content

```bash
# Print file content to stdout
hdfs dfs -cat /hdfs/path/file.txt

# Print first n lines
hdfs dfs -cat /hdfs/path/file.txt | head -20

# Print end of file
hdfs dfs -tail /hdfs/path/file.txt
```

#### Copying and Moving

```bash
# Copy within HDFS
hdfs dfs -cp /hdfs/source/file.txt /hdfs/dest/

# Move within HDFS (rename)
hdfs dfs -mv /hdfs/old/path /hdfs/new/path
```

#### Deleting Files and Directories

```bash
# Delete a file
hdfs dfs -rm /hdfs/path/file.txt

# Delete directory and contents (recursive)
hdfs dfs -rm -r /hdfs/path/directory/

# Delete, skipping trash
hdfs dfs -rm -skipTrash /hdfs/path/file.txt

# Delete empty directory only
hdfs dfs -rmdir /hdfs/path/emptydir/
```

#### File Information

```bash
# Show file size (human-readable)
hdfs dfs -du -h /hdfs/path/

# Show total size of directory
hdfs dfs -du -s -h /hdfs/path/

# Show block count and file count
hdfs dfs -count /hdfs/path/

# Show detailed file info (block size, replication)
hdfs dfs -stat %b,%r,%n /hdfs/path/file.txt
```

### 7.2 Permissions and Ownership

```bash
# Change permissions (Unix-style)
hdfs dfs -chmod 755 /hdfs/path/file.txt
hdfs dfs -chmod -R 755 /hdfs/path/directory/

# Change owner
hdfs dfs -chown user:group /hdfs/path/file.txt
hdfs dfs -chown -R user:group /hdfs/path/directory/

# Change group
hdfs dfs -chgrp groupname /hdfs/path/file.txt
```

### 7.3 Replication

```bash
# Set replication factor for a file
hdfs dfs -setrep 2 /hdfs/path/file.txt

# Set replication recursively
hdfs dfs -setrep -R 2 /hdfs/path/directory/

# Check replication status
hdfs fsck /hdfs/path/ -files -blocks -locations
```

### 7.4 HDFS Admin Commands

```bash
# Show HDFS filesystem usage summary
hdfs dfsadmin -report

# Enter/exit safe mode (NameNode)
hdfs dfsadmin -safemode enter
hdfs dfsadmin -safemode leave
hdfs dfsadmin -safemode get

# Refresh NameNode with new DataNodes
hdfs dfsadmin -refreshNodes

# Run HDFS health check
hdfs fsck /

# Balance data across DataNodes
hdfs balancer -threshold 10
```

### 7.5 Trash Management

By default, deleted files go to `.Trash` directory (retention period configurable):

```bash
# Restore from trash
hdfs dfs -mv /user/hadoop/.Trash/Current/file.txt /user/hadoop/

# Expunge trash (permanently delete)
hdfs dfs -expunge
```

### 7.6 Quick Reference Table

| Command | Description |
|---------|-------------|
| `-ls` | List directory contents |
| `-mkdir` | Create directory |
| `-put` / `-copyFromLocal` | Upload local file to HDFS |
| `-get` / `-copyToLocal` | Download HDFS file to local |
| `-cat` | Print file content |
| `-tail` | Print last KB of file |
| `-cp` | Copy within HDFS |
| `-mv` | Move/rename within HDFS |
| `-rm` | Delete file |
| `-rm -r` | Delete directory recursively |
| `-du` | Show file/dir size |
| `-count` | Count files/blocks |
| `-chmod` | Change permissions |
| `-chown` | Change ownership |
| `-setrep` | Change replication factor |
| `-getmerge` | Merge HDFS files to local |
| `-expunge` | Empty HDFS trash |

---

## 8. Overview of Hadoop Ecosystem

The Hadoop ecosystem is a collection of frameworks and tools built around or complementary to Hadoop's core components (HDFS and YARN).

### 8.1 Ecosystem Map

```
+-------------------------------------------------------------------+
|                       USER INTERFACES                             |
|  HBase Shell | Hive CLI | Pig Grunt | Sqoop | Flume | Oozie UI  |
+-------------------------------------------------------------------+
|                       QUERY / PROCESSING                          |
|   Hive (SQL)  |  Pig (Scripting)  |  Spark (In-Memory)          |
|   HBase (NoSQL DB)  |  Mahout (ML)  |  Impala (Real-time SQL)   |
+-------------------------------------------------------------------+
|                   DATA INGESTION / TRANSFER                       |
|   Sqoop (RDBMS ↔ HDFS)  |  Flume (Log ingestion)               |
|   Kafka (Stream ingestion)  |  NiFi (Data flows)                |
+-------------------------------------------------------------------+
|                   COORDINATION / WORKFLOW                         |
|   ZooKeeper (Coordination)  |  Oozie (Workflow scheduler)       |
|   Ambari (Cluster management)  |  Ranger (Security)             |
+-------------------------------------------------------------------+
|                  CORE: HDFS + YARN + MapReduce                   |
+-------------------------------------------------------------------+
```

### 8.2 Key Ecosystem Tools

#### Data Storage
| Tool | Purpose |
|------|---------|
| **HDFS** | Distributed file system (primary storage) |
| **HBase** | Distributed NoSQL column-family database (real-time reads/writes on HDFS) |
| **Kudu** | Columnar storage for fast analytics and updates |

#### Data Processing
| Tool | Purpose |
|------|---------|
| **MapReduce** | Batch processing framework (disk-based) |
| **Apache Spark** | In-memory distributed processing (batch, streaming, ML, SQL) |
| **Apache Tez** | DAG-based execution engine (faster than MapReduce, used by Hive) |
| **Apache Flink** | Stream-first processing with batch support |

#### Data Query
| Tool | Purpose |
|------|---------|
| **Apache Hive** | SQL-like querying on HDFS (translates HiveQL → MapReduce/Tez) |
| **Apache Pig** | High-level dataflow scripting language (Pig Latin) |
| **Impala** | Low-latency, real-time SQL queries directly on HDFS/HBase (Cloudera) |
| **Presto/Trino** | Distributed SQL query engine for large-scale analytics |
| **Drill** | Schema-free SQL for Hadoop, NoSQL, and cloud storage |

#### Data Ingestion
| Tool | Purpose |
|------|---------|
| **Apache Sqoop** | Bulk data transfer between HDFS and RDBMS (MySQL, Oracle, etc.) |
| **Apache Flume** | Collecting, aggregating, and moving large amounts of log data into HDFS |
| **Apache Kafka** | Distributed real-time messaging / streaming platform |
| **Apache NiFi** | Visual data flow management and routing |

#### Workflow & Coordination
| Tool | Purpose |
|------|---------|
| **Apache Oozie** | Workflow scheduler for Hadoop jobs (XML/DAG-based) |
| **Apache ZooKeeper** | Distributed coordination service (leader election, config management, locks) |
| **Apache Airflow** | Modern workflow orchestration (Python DAGs) |

#### Machine Learning
| Tool | Purpose |
|------|---------|
| **Apache Mahout** | Scalable ML algorithms on Hadoop (classification, clustering, CF) |
| **Spark MLlib** | ML library integrated with Apache Spark |
| **H2O** | In-memory ML platform that integrates with HDFS/Spark |

#### Cluster Management & Security
| Tool | Purpose |
|------|---------|
| **Apache Ambari** | Web-based Hadoop cluster provisioning, management, and monitoring |
| **Apache Ranger** | Centralized security and policy management for Hadoop |
| **Apache Knox** | REST API gateway for Hadoop cluster security |
| **Kerberos** | Authentication protocol used to secure Hadoop clusters |

---

## 9. Apache Hive

### 9.1 What is Apache Hive?

**Apache Hive** is a **data warehousing** and **SQL-like query** framework built on top of Hadoop. Developed by Facebook (2008) and donated to Apache, it allows users who know SQL to interact with data stored in HDFS without writing MapReduce programs.

Hive provides:
- **HiveQL (HQL)**: An SQL dialect for querying HDFS data
- **Metastore**: A relational database (Derby/MySQL/PostgreSQL) that stores schema/metadata
- **Execution**: Translates HiveQL queries into **MapReduce, Tez, or Spark** jobs

### 9.2 When to Use Hive

| Use Hive | Don't Use Hive |
|----------|---------------|
| Batch ETL on large datasets | Low-latency queries (<1 sec) |
| Data warehousing / BI reporting | OLTP (frequent small updates) |
| Ad-hoc analysis by SQL users | Real-time streaming |
| Joining large HDFS datasets | Frequent random read/write |

### 9.3 Hive Architecture

```
+-----------------------------------------------------------+
|           Hive Clients                                    |
|  CLI (Beeline/HiveCLI)  |  JDBC/ODBC  |  Web UI (HWI)   |
+-----------------------------------------------------------+
              |
+-----------------------------------------------------------+
|           Hive Driver                                     |
|  Compiler → Optimizer → Executor                         |
|  (HQL → Logical Plan → Physical Plan → MapReduce/Tez)   |
+-----------------------------------------------------------+
      |                           |
+-----+------+           +--------+-------+
| Metastore  |           |  HDFS / YARN   |
| (MySQL/    |           |  (Storage +    |
|  Derby)    |           |   Execution)   |
+------------+           +----------------+
```

**Components:**

| Component | Role |
|-----------|------|
| **Driver** | Receives queries, orchestrates compilation and execution |
| **Compiler** | Parses HQL, generates logical plan using Metastore info |
| **Optimizer** | Transforms logical plan into optimized physical plan |
| **Executor** | Submits physical plan as MapReduce/Tez/Spark job to YARN |
| **Metastore** | Stores schema metadata (DB names, table names, column types, partition info, SerDe info) |
| **Thrift Server** | Enables JDBC/ODBC connections (HiveServer2) |

### 9.4 Hive Data Model

Hive organizes data in a hierarchy:

```
Database
  └── Table
        ├── Partition (optional, sub-divides table by column value)
        │     └── Bucket (optional, hash-partitions partition data)
        └── (Data stored in HDFS as files)
```

| Level | Description | HDFS Location Example |
|-------|-------------|----------------------|
| **Database** | Namespace for tables | `/user/hive/warehouse/mydb.db/` |
| **Table** | Collection of rows with schema | `/user/hive/warehouse/mydb.db/employees/` |
| **Partition** | Sub-directory by partition column | `/user/hive/warehouse/mydb.db/employees/dept=Sales/` |
| **Bucket** | Hashed sub-files within partition | `000000_0`, `000001_0`, ... |

### 9.5 Internal vs External Tables

| Aspect | Internal (Managed) Table | External Table |
|--------|--------------------------|---------------|
| **Data ownership** | Hive owns the data | User owns the data |
| **On DROP TABLE** | Metadata + HDFS data deleted | Only metadata deleted; HDFS data preserved |
| **Use when** | Hive manages full lifecycle | Data shared with other tools |
| **Location** | Default Hive warehouse | Custom HDFS path |

```sql
-- Internal table (Hive owns data)
CREATE TABLE employees ( ... );

-- External table (data lives elsewhere)
CREATE EXTERNAL TABLE sales_data ( ... )
LOCATION '/data/sales/';
```

### 9.6 Partitioning

Partitioning stores data in separate subdirectories, enabling **partition pruning** (reading only relevant partitions):

```sql
CREATE TABLE logs (
    user_id  INT,
    event    STRING,
    ts       TIMESTAMP
)
PARTITIONED BY (log_date STRING, region STRING);

-- Inserting with partitions
INSERT INTO TABLE logs PARTITION (log_date='2024-01-15', region='APAC')
SELECT user_id, event, ts FROM raw_logs WHERE region='APAC';
```

Query using partition filter (reads only 2024-01-15 / APAC files):
```sql
SELECT * FROM logs WHERE log_date='2024-01-15' AND region='APAC';
```

### 9.7 Bucketing

Bucketing distributes data across fixed number of files based on **hash of a column**:

```sql
CREATE TABLE orders (
    order_id  BIGINT,
    customer  STRING,
    amount    DECIMAL(10,2)
)
CLUSTERED BY (customer) INTO 32 BUCKETS
STORED AS ORC;
```

Benefits:
- Enables **Bucketed Map Join** (avoid expensive shuffle when joining bucketed tables)
- Efficient **TABLESAMPLE** (sampling a fraction of the table quickly)

### 9.8 File Formats in Hive

| Format | Type | Compression | Best For |
|--------|------|-------------|----------|
| **TextFile** (default) | Row | None | Human-readable, simple |
| **SequenceFile** | Row | Optional | Splittable binary |
| **RCFile** | Column | Yes | Column reads |
| **ORC** (Optimized Row Columnar) | Column | Yes (Zlib/Snappy/LZO) | Best for Hive — predicate pushdown, ACID |
| **Parquet** | Column | Yes | Best for Spark/Impala interop |
| **Avro** | Row | Optional | Schema evolution, Kafka |

**ORC** is the recommended format for Hive tables due to:
- Column pruning (reads only needed columns)
- Predicate pushdown (skips irrelevant row groups)
- Built-in compression (typically 75% space savings)
- ACID transaction support

---

## 10. Hive Data Types

### 10.1 Primitive Data Types

#### Numeric Types

| Data Type | Size | Range | Example |
|-----------|------|-------|---------|
| `TINYINT` | 1 byte | -128 to 127 | `age TINYINT` |
| `SMALLINT` | 2 bytes | -32,768 to 32,767 | `code SMALLINT` |
| `INT` / `INTEGER` | 4 bytes | -2.1B to 2.1B | `id INT` |
| `BIGINT` | 8 bytes | Very large integers | `record_id BIGINT` |
| `FLOAT` | 4 bytes | Single-precision float | `score FLOAT` |
| `DOUBLE` | 8 bytes | Double-precision float | `price DOUBLE` |
| `DECIMAL(p,s)` | Variable | Arbitrary precision | `amount DECIMAL(10,2)` |
| `NUMERIC(p,s)` | Variable | Alias for DECIMAL | — |

#### String Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `STRING` | Variable-length string (no size limit) | `name STRING` |
| `VARCHAR(n)` | Variable-length, max n characters | `code VARCHAR(10)` |
| `CHAR(n)` | Fixed-length, padded with spaces | `state CHAR(2)` |

#### Date and Time Types

| Data Type | Format | Example |
|-----------|--------|---------|
| `DATE` | `YYYY-MM-DD` | `dob DATE` |
| `TIMESTAMP` | `YYYY-MM-DD HH:MM:SS[.fractional]` | `created_at TIMESTAMP` |
| `INTERVAL` | Time intervals | `INTERVAL 7 DAYS` |

#### Boolean and Binary Types

| Data Type | Description |
|-----------|-------------|
| `BOOLEAN` | `TRUE` / `FALSE` |
| `BINARY` | Byte array (raw binary data) |

### 10.2 Complex Data Types

Hive supports complex/collection types — unique to Hive among SQL systems:

#### ARRAY

An ordered collection of elements of the **same type**.

```sql
-- Definition
skills ARRAY<STRING>

-- Example value
['Java', 'Python', 'SQL']

-- Accessing elements (0-indexed)
SELECT skills[0] FROM employees;       -- 'Java'

-- Checking membership
SELECT * FROM employees WHERE array_contains(skills, 'Python');
```

#### MAP

A collection of **key-value pairs**. Keys and values each have a specified type.

```sql
-- Definition
attributes MAP<STRING, INT>

-- Example value
{'age': 30, 'experience': 5, 'projects': 12}

-- Accessing values
SELECT attributes['age'] FROM employees;    -- 30
```

#### STRUCT

A **record** with named fields of different types (like a C struct or Python named tuple).

```sql
-- Definition
address STRUCT<street:STRING, city:STRING, zip:INT>

-- Example value
{'street':'123 Main St', 'city':'Mumbai', 'zip':400001}

-- Accessing fields
SELECT address.city FROM employees;    -- 'Mumbai'
```

#### UNIONTYPE

Holds a value that can be one of several different types (rarely used):

```sql
-- Definition
data UNIONTYPE<INT, STRING, BOOLEAN>
```

### 10.3 Type Casting

```sql
-- Implicit casting (lower precision → higher precision)
SELECT 10 + 3.5;    -- Result: DOUBLE

-- Explicit casting
SELECT CAST('2024-01-15' AS DATE);
SELECT CAST(price AS INT) FROM products;
SELECT CAST(id AS STRING) FROM orders;
```

### 10.4 Type Summary Table

| Category | Types |
|----------|-------|
| **Integer** | TINYINT, SMALLINT, INT, BIGINT |
| **Floating Point** | FLOAT, DOUBLE, DECIMAL |
| **String** | STRING, VARCHAR, CHAR |
| **Date/Time** | DATE, TIMESTAMP, INTERVAL |
| **Boolean** | BOOLEAN |
| **Binary** | BINARY |
| **Collection** | ARRAY\<T\>, MAP\<K,V\>, STRUCT\<...\>, UNIONTYPE |

---

## 11. Create, Alter and Drop Commands

### 11.1 Database (Schema) Commands

#### CREATE DATABASE

```sql
-- Simple
CREATE DATABASE mydb;

-- With checks and properties
CREATE DATABASE IF NOT EXISTS analytics_db
COMMENT 'Analytics data warehouse'
LOCATION '/user/hive/warehouse/analytics_db.db'
WITH DBPROPERTIES ('owner'='dataeng', 'created'='2024-01-01');
```

#### USE DATABASE

```sql
USE analytics_db;
```

#### ALTER DATABASE

```sql
ALTER DATABASE analytics_db
SET DBPROPERTIES ('owner'='admin', 'version'='2.0');
```

#### DROP DATABASE

```sql
DROP DATABASE analytics_db;                  -- Fails if tables exist
DROP DATABASE IF EXISTS analytics_db CASCADE; -- Drops all tables first
```

#### SHOW / DESCRIBE DATABASE

```sql
SHOW DATABASES;
SHOW DATABASES LIKE 'ana*';
DESCRIBE DATABASE analytics_db;
DESCRIBE DATABASE EXTENDED analytics_db;
```

---

### 11.2 Table Commands

#### CREATE TABLE (Internal/Managed)

```sql
CREATE TABLE IF NOT EXISTS employees (
    emp_id      INT,
    name        STRING,
    department  STRING,
    salary      DECIMAL(10,2),
    hire_date   DATE,
    skills      ARRAY<STRING>,
    address     STRUCT<city:STRING, zip:INT>
)
COMMENT 'Employee master table'
ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    COLLECTION ITEMS TERMINATED BY '|'
    MAP KEYS TERMINATED BY ':'
    LINES TERMINATED BY '\n'
STORED AS ORC
TBLPROPERTIES ('orc.compress'='SNAPPY');
```

#### CREATE EXTERNAL TABLE

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sales_raw (
    txn_id    BIGINT,
    product   STRING,
    amount    DOUBLE,
    txn_date  STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/raw/sales/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

#### CREATE TABLE with Partitions

```sql
CREATE TABLE web_logs (
    ip_address  STRING,
    url         STRING,
    status_code INT,
    bytes       BIGINT
)
PARTITIONED BY (log_year INT, log_month INT, log_day INT)
STORED AS ORC;
```

#### CREATE TABLE AS SELECT (CTAS)

```sql
-- Create new table from query result
CREATE TABLE top_customers
STORED AS ORC AS
SELECT customer_id, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id
HAVING total_spend > 10000;
```

#### CREATE TABLE LIKE

```sql
-- Copy table schema (not data)
CREATE TABLE employees_backup LIKE employees;
```

---

#### ALTER TABLE

##### Rename Table
```sql
ALTER TABLE employees RENAME TO staff;
```

##### Add Columns
```sql
ALTER TABLE employees ADD COLUMNS (
    email   STRING COMMENT 'Employee email',
    phone   VARCHAR(15)
);
```

##### Change Column (rename/type/position)
```sql
-- Rename and change type
ALTER TABLE employees CHANGE COLUMN emp_id employee_id BIGINT;

-- Rename and move to specific position
ALTER TABLE employees CHANGE COLUMN salary base_salary DECIMAL(12,2) AFTER name;
```

##### Replace Columns (redefine all columns)
```sql
ALTER TABLE employees REPLACE COLUMNS (
    id      BIGINT,
    name    STRING,
    dept    STRING,
    salary  DECIMAL(12,2)
);
```

##### Set Table Properties
```sql
ALTER TABLE employees SET TBLPROPERTIES (
    'comment'='Updated employee table',
    'last_modified'='2024-01-15'
);
```

##### Convert to External / Internal
```sql
-- Internal → External
ALTER TABLE employees SET TBLPROPERTIES ('EXTERNAL'='TRUE');

-- External → Internal
ALTER TABLE employees SET TBLPROPERTIES ('EXTERNAL'='FALSE');
```

##### Add/Drop Partitions
```sql
-- Add partition manually
ALTER TABLE web_logs ADD PARTITION (log_year=2024, log_month=1, log_day=15)
LOCATION '/data/logs/2024/01/15/';

-- Add multiple partitions at once
ALTER TABLE web_logs ADD
    PARTITION (log_year=2024, log_month=1, log_day=16)
    PARTITION (log_year=2024, log_month=1, log_day=17);

-- Drop partition (removes metadata + data for managed tables)
ALTER TABLE web_logs DROP PARTITION (log_year=2023, log_month=12, log_day=31);

-- Rename partition
ALTER TABLE web_logs PARTITION (log_year=2024, log_month=1)
RENAME TO PARTITION (log_year=2024, log_month=01);
```

##### Change Storage Format
```sql
ALTER TABLE employees SET FILEFORMAT ORC;
ALTER TABLE employees SET SERDEPROPERTIES ('field.delim'='\t');
```

---

#### DROP TABLE

```sql
-- Drop table (removes metadata; for external tables, data in HDFS preserved)
DROP TABLE IF EXISTS employees;

-- Drop and purge (bypass trash, immediate delete)
DROP TABLE employees PURGE;
```

---

### 11.3 SHOW and DESCRIBE Commands

```sql
-- List all tables in current database
SHOW TABLES;
SHOW TABLES IN analytics_db LIKE 'emp*';

-- List partitions
SHOW PARTITIONS web_logs;
SHOW PARTITIONS web_logs PARTITION (log_year=2024);

-- Describe table schema
DESCRIBE employees;
DESC employees;

-- Describe with detailed info (location, partition info, SerDe, etc.)
DESCRIBE EXTENDED employees;
DESCRIBE FORMATTED employees;

-- Describe a specific column
DESCRIBE employees name;

-- Describe a partition
DESCRIBE FORMATTED web_logs PARTITION (log_year=2024, log_month=1);
```

---

### 11.4 Loading Data into Tables

```sql
-- Load local file into table (moves file to Hive warehouse)
LOAD DATA LOCAL INPATH '/local/path/data.csv' INTO TABLE employees;

-- Overwrite existing data
LOAD DATA LOCAL INPATH '/local/path/data.csv' OVERWRITE INTO TABLE employees;

-- Load from HDFS (moves file, no copy)
LOAD DATA INPATH '/hdfs/path/data.csv' INTO TABLE employees;

-- Load into specific partition
LOAD DATA LOCAL INPATH '/local/path/jan.csv'
INTO TABLE web_logs PARTITION (log_year=2024, log_month=1, log_day=1);

-- Insert from query
INSERT INTO TABLE employees
SELECT id, name, dept, salary FROM raw_employees WHERE dept != 'Temp';

-- Insert overwrite
INSERT OVERWRITE TABLE employees
SELECT id, name, dept, salary FROM raw_employees WHERE active = 1;

-- Insert into partition
INSERT INTO TABLE web_logs PARTITION (log_year=2024, log_month=2)
SELECT ip, url, status, bytes FROM raw_logs WHERE month='2024-02';

-- Multi-table insert (one query, multiple outputs)
FROM raw_employees
INSERT INTO TABLE active_emp   SELECT * WHERE status = 'active'
INSERT INTO TABLE inactive_emp SELECT * WHERE status = 'inactive';
```

---

## 12. Built-in Operators and Functions

### 12.1 Relational Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal | `WHERE dept = 'Sales'` |
| `<>` or `!=` | Not equal | `WHERE status != 'inactive'` |
| `<` | Less than | `WHERE age < 30` |
| `>` | Greater than | `WHERE salary > 50000` |
| `<=` | Less than or equal | `WHERE score <= 100` |
| `>=` | Greater than or equal | `WHERE years >= 5` |
| `IS NULL` | Null check | `WHERE email IS NULL` |
| `IS NOT NULL` | Non-null check | `WHERE phone IS NOT NULL` |
| `LIKE` | Pattern match (`%` = wildcard, `_` = single char) | `WHERE name LIKE 'A%'` |
| `RLIKE` | Regex match | `WHERE email RLIKE '.*@gmail\\.com'` |
| `IN` | Value in list | `WHERE dept IN ('HR','IT')` |
| `BETWEEN` | Range check | `WHERE age BETWEEN 25 AND 35` |

### 12.2 Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `salary + bonus` |
| `-` | Subtraction | `price - discount` |
| `*` | Multiplication | `quantity * unit_price` |
| `/` | Division | `total / count` |
| `%` | Modulo | `id % 10` |
| `DIV` | Integer division | `15 DIV 4` → `3` |
| `&` | Bitwise AND | `flags & 1` |
| `\|` | Bitwise OR | `flags \| 2` |
| `^` | Bitwise XOR | `a ^ b` |
| `~` | Bitwise NOT | `~flag` |

### 12.3 Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `AND` / `&&` | Logical AND | `age > 18 AND salary > 30000` |
| `OR` / `\|\|` | Logical OR | `dept='HR' OR dept='IT'` |
| `NOT` / `!` | Logical NOT | `NOT (status = 'inactive')` |

### 12.4 String Functions

```sql
-- Length
LENGTH('Hadoop')             -- 6
CHAR_LENGTH('Hive')          -- 4

-- Case
UPPER('hive')                -- 'HIVE'
LOWER('HIVE')                -- 'hive'
INITCAP('hello world')       -- 'Hello World'

-- Trimming
TRIM('  hello  ')            -- 'hello'
LTRIM('  hello  ')           -- 'hello  '
RTRIM('  hello  ')           -- '  hello'

-- Padding
LPAD('5', 4, '0')            -- '0005'
RPAD('Hi', 5, '!')           -- 'Hi!!!'

-- Substring
SUBSTR('Hadoop', 2, 4)       -- 'adoo'
SUBSTRING('Hadoop', 1, 3)    -- 'Had'

-- Find position
INSTR('Hadoop', 'do')        -- 3

-- Replace
REPLACE('Hadoop', 'do', 'X') -- 'HaXop'
REGEXP_REPLACE('abc123', '[0-9]+', '') -- 'abc'

-- Concatenate
CONCAT('Big', ' ', 'Data')   -- 'Big Data'
CONCAT_WS('-', '2024', '01', '15') -- '2024-01-15'  (with separator)

-- Repeat
REPEAT('ab', 3)              -- 'ababab'

-- Reverse
REVERSE('Hadoop')            -- 'poodaH'

-- Split (returns ARRAY)
SPLIT('a,b,c,d', ',')       -- ['a','b','c','d']

-- Convert to/from hex
HEX('A')                    -- '41'
UNHEX('41')                 -- 'A'
```

### 12.5 Numeric/Math Functions

```sql
ABS(-5)            -- 5
ROUND(3.567, 2)    -- 3.57
FLOOR(3.9)         -- 3
CEIL(3.1)          -- 4
SQRT(16)           -- 4.0
POWER(2, 10)       -- 1024.0
EXP(1)             -- 2.718...
LOG(10, 100)       -- 2.0       (log base 10 of 100)
LOG2(8)            -- 3.0
LOG10(1000)        -- 3.0
MOD(17, 5)         -- 2
SIGN(-5)           -- -1
POSITIVE(-3)       -- -3
NEGATIVE(3)        -- -3
RAND()             -- Random float between 0.0 and 1.0
RAND(42)           -- Seeded random (reproducible)
PI()               -- 3.14159...
SIN(PI()/2)        -- 1.0
COS(0)             -- 1.0
TAN(PI()/4)        -- ~1.0
```

### 12.6 Date and Time Functions

```sql
-- Current date/time
CURRENT_DATE                  -- '2024-01-15'  (DATE)
CURRENT_TIMESTAMP             -- '2024-01-15 10:30:00' (TIMESTAMP)
NOW()                         -- Alias for CURRENT_TIMESTAMP
UNIX_TIMESTAMP()              -- Current Unix epoch seconds

-- Conversion
FROM_UNIXTIME(1705312200)     -- '2024-01-15 10:30:00'
UNIX_TIMESTAMP('2024-01-15', 'yyyy-MM-dd') -- epoch int
TO_DATE('2024-01-15 10:30:00')-- '2024-01-15'
DATE_FORMAT(CURRENT_DATE, 'yyyyMMdd')  -- '20240115'

-- Extraction
YEAR('2024-01-15')            -- 2024
MONTH('2024-01-15')           -- 1
DAY('2024-01-15')             -- 15
HOUR('2024-01-15 10:30:00')   -- 10
MINUTE('2024-01-15 10:30:00') -- 30
SECOND('2024-01-15 10:30:00') -- 0
WEEKOFYEAR('2024-01-15')      -- 3
DAYOFWEEK('2024-01-15')       -- 2  (1=Sunday, 2=Monday, ...)
QUARTER('2024-04-01')         -- 2

-- Arithmetic
DATE_ADD('2024-01-15', 10)    -- '2024-01-25'
DATE_SUB('2024-01-15', 10)    -- '2024-01-05'
DATEDIFF('2024-01-25', '2024-01-15') -- 10
ADD_MONTHS('2024-01-15', 3)   -- '2024-04-15'
MONTHS_BETWEEN('2024-04-15', '2024-01-15') -- 3.0

-- Last day of month
LAST_DAY('2024-02-10')        -- '2024-02-29'

-- Truncate to unit
TRUNC('2024-01-15', 'MM')     -- '2024-01-01'  (start of month)
TRUNC('2024-01-15', 'YYYY')   -- '2024-01-01'  (start of year)
```

### 12.7 Aggregate Functions

```sql
COUNT(*)                 -- Count all rows (including NULLs)
COUNT(column)            -- Count non-NULL values
COUNT(DISTINCT column)   -- Count distinct non-NULL values
SUM(salary)              -- Sum of values
AVG(salary)              -- Average (ignores NULLs)
MIN(salary)              -- Minimum value
MAX(salary)              -- Maximum value
STDDEV(salary)           -- Standard deviation
VARIANCE(salary)         -- Variance

-- String aggregation (Hive 2.0+)
COLLECT_LIST(name)       -- Returns ARRAY (with duplicates)
COLLECT_SET(dept)        -- Returns ARRAY (distinct values)

-- Example: comma-separated skills per department
SELECT dept, CONCAT_WS(',', COLLECT_LIST(name)) AS member_names
FROM employees
GROUP BY dept;
```

### 12.8 Conditional Functions

```sql
-- IF (ternary)
IF(salary > 50000, 'High', 'Low')

-- CASE WHEN (multi-condition)
CASE
    WHEN salary < 30000 THEN 'Entry'
    WHEN salary < 60000 THEN 'Mid'
    WHEN salary < 100000 THEN 'Senior'
    ELSE 'Executive'
END AS salary_band

-- Simple CASE (equality)
CASE dept
    WHEN 'IT'      THEN 'Technology'
    WHEN 'HR'      THEN 'Human Resources'
    WHEN 'Finance' THEN 'Finance'
    ELSE 'Other'
END

-- COALESCE (return first non-NULL)
COALESCE(phone, email, 'N/A')   -- Returns first non-NULL of the three

-- NVL (return default if NULL)
NVL(bonus, 0)                   -- Returns 0 if bonus is NULL

-- NVL2 (if not null: value1, else: value2)
NVL2(bonus, 'Has Bonus', 'No Bonus')

-- NULLIF (return NULL if values are equal)
NULLIF(total, 0)                -- Returns NULL if total=0 (avoids divide-by-zero)

-- IIF (Hive 2.0+)
IIF(active = 1, 'Active', 'Inactive')
```

### 12.9 Collection Functions

```sql
-- ARRAY functions
SIZE(skills)                         -- Number of elements: 3
ARRAY_CONTAINS(skills, 'Python')     -- TRUE/FALSE
SORT_ARRAY(skills)                   -- Sorted array
skills[0]                            -- First element

-- MAP functions
SIZE(attributes)                     -- Number of key-value pairs
MAP_KEYS(attributes)                 -- Array of keys
MAP_VALUES(attributes)               -- Array of values
attributes['age']                    -- Value for key 'age'

-- STRUCT functions
address.city                         -- Access struct field

-- EXPLODE (converts array/map row to multiple rows)
SELECT EXPLODE(skills) AS skill FROM employees;
-- Produces one row per skill

-- LATERAL VIEW (joins EXPLODE output back with original table)
SELECT emp_id, name, skill
FROM employees
LATERAL VIEW EXPLODE(skills) skill_table AS skill;

-- POSEXPLODE (with index)
SELECT pos, skill
FROM employees
LATERAL VIEW POSEXPLODE(skills) st AS pos, skill;
```

### 12.10 Window Functions

Window functions operate over a **window** (set of rows related to the current row) without collapsing rows (unlike GROUP BY).

```sql
-- Syntax
function() OVER (
    [PARTITION BY column1, column2, ...]
    [ORDER BY column3 [ASC|DESC], ...]
    [ROWS | RANGE BETWEEN ... AND ...]
)

-- Ranking Functions
ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
RANK()       OVER (PARTITION BY dept ORDER BY salary DESC) AS rank
DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dense_rank
PERCENT_RANK() OVER (ORDER BY salary)   AS pct_rank
CUME_DIST()  OVER (ORDER BY salary)    AS cume_dist
NTILE(4)     OVER (ORDER BY salary)    AS quartile

-- Lead / Lag (access other rows)
LAG(salary, 1, 0)  OVER (PARTITION BY dept ORDER BY hire_date) AS prev_salary
LEAD(salary, 1, 0) OVER (PARTITION BY dept ORDER BY hire_date) AS next_salary

-- First / Last value
FIRST_VALUE(salary) OVER (PARTITION BY dept ORDER BY hire_date) AS first_salary
LAST_VALUE(salary)  OVER (PARTITION BY dept ORDER BY hire_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_salary

-- Running totals / moving averages
SUM(salary)  OVER (PARTITION BY dept ORDER BY hire_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
AVG(salary)  OVER (PARTITION BY dept ORDER BY hire_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)         AS moving_avg_3

-- Example: Rank employees by salary within each department
SELECT
    emp_id, name, dept, salary,
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_salary_rank
FROM employees;
```

### 12.11 Table-Generating Functions (UDTF)

| Function | Description | Example |
|----------|-------------|---------|
| `EXPLODE(array)` | One row per array element | `EXPLODE(skills)` |
| `EXPLODE(map)` | One row per key-value pair | `EXPLODE(attrs)` |
| `POSEXPLODE(array)` | Like EXPLODE but with position index | `POSEXPLODE(items)` |
| `INLINE(array<struct>)` | Expands array of structs | `INLINE(order_items)` |
| `JSON_TUPLE(json, k1, k2)` | Extract JSON fields | `JSON_TUPLE(data, 'name', 'age')` |
| `PARSE_URL_TUPLE(url, p1, p2)` | Parse URL components | `PARSE_URL_TUPLE(url, 'HOST', 'PATH')` |
| `STACK(n, v1, v2, ...)` | Stack n values into rows | `STACK(2, 'a', 1, 'b', 2)` |

---

## 13. Views

### 13.1 What is a View?

A **View** in Hive is a **named query** stored in the Metastore. It is a **virtual table** — it does not store data itself; it is computed from the underlying tables every time it is queried.

**Key Properties:**
- Read-only (cannot INSERT/UPDATE/DELETE through a view)
- Query is evaluated fresh each time the view is used
- Can reference other views (nestable)
- Can simplify complex queries for users
- Provides an abstraction layer

### 13.2 Creating Views

```sql
-- Simple view
CREATE VIEW IF NOT EXISTS high_earners AS
SELECT emp_id, name, dept, salary
FROM employees
WHERE salary > 80000;

-- View with column aliases
CREATE VIEW dept_summary (department, headcount, avg_salary, max_salary) AS
SELECT
    dept,
    COUNT(*),
    AVG(salary),
    MAX(salary)
FROM employees
GROUP BY dept;

-- View joining multiple tables
CREATE VIEW employee_details AS
SELECT
    e.emp_id,
    e.name,
    e.salary,
    d.dept_name,
    d.location,
    m.name AS manager_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- View with window function
CREATE VIEW salary_rankings AS
SELECT
    emp_id, name, dept, salary,
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### 13.3 Querying Views

Views are queried exactly like tables:

```sql
-- Query the view
SELECT * FROM high_earners;

SELECT department, avg_salary
FROM dept_summary
WHERE avg_salary > 60000
ORDER BY avg_salary DESC;

-- View used in a join
SELECT e.name, s.dept_rank
FROM employees e
JOIN salary_rankings s ON e.emp_id = s.emp_id
WHERE s.dept_rank <= 3;
```

### 13.4 Altering Views

```sql
-- Redefine view query (does not affect underlying data)
ALTER VIEW high_earners AS
SELECT emp_id, name, dept, salary, hire_date
FROM employees
WHERE salary > 100000;   -- Updated threshold

-- Rename view
ALTER VIEW high_earners RENAME TO top_earners;

-- Set view properties
ALTER VIEW top_earners SET TBLPROPERTIES ('owner'='dataeng');
```

### 13.5 Dropping Views

```sql
DROP VIEW IF EXISTS high_earners;
```

**Note:** Dropping a view does NOT affect the underlying tables or their data.

### 13.6 Showing and Describing Views

```sql
-- List views (views appear in SHOW TABLES output)
SHOW TABLES;
SHOW VIEWS;                              -- Hive 2.2.0+
SHOW VIEWS IN analytics_db LIKE 'emp*'; -- Filter by pattern

-- Describe view structure
DESCRIBE high_earners;
DESCRIBE EXTENDED high_earners;
DESCRIBE FORMATTED high_earners;

-- Show the view definition (CREATE statement)
SHOW CREATE TABLE high_earners;
```

### 13.7 Advantages and Limitations of Views

| Advantages | Limitations |
|-----------|------------|
| Simplify complex queries | Read-only (no DML through view) |
| Provide data abstraction/security | No performance benefit (no materialization) |
| Reusable query logic | View query re-executed every time |
| Decouple app from schema | Cannot create index on view |
| Restrict column access | Circular view references not allowed |

### 13.8 Materialized Views (Hive 3.0+)

Unlike regular views, **Materialized Views** pre-compute and store query results:

```sql
-- Create materialized view (stores data)
CREATE MATERIALIZED VIEW mv_dept_summary AS
SELECT dept, COUNT(*) AS cnt, AVG(salary) AS avg_sal
FROM employees
GROUP BY dept;

-- Query uses cached results (fast)
SELECT * FROM mv_dept_summary;

-- Rebuild when source data changes
ALTER MATERIALIZED VIEW mv_dept_summary REBUILD;

-- Drop materialized view
DROP MATERIALIZED VIEW mv_dept_summary;
```

**Benefits:**
- Query rewriting: Hive can automatically use the materialized view to answer queries against the base table
- Significant speedup for repeated aggregations

---

## 14. Interaction with Hadoop Framework

### 14.1 How Hive Interacts with Hadoop

Hive sits on top of Hadoop and uses its storage and processing capabilities:

```
HiveQL Query
     ↓
Hive Driver (Compiler + Optimizer)
     ↓
Execution Plan (MapReduce / Tez / Spark Jobs)
     ↓
YARN (Resource Management)
     ↓
DataNodes (HDFS Data Read/Write)
     ↓
Result returned to Client
```

### 14.2 Execution Engines

Hive supports multiple execution engines, configurable via `hive.execution.engine`:

| Engine | Configuration Value | Characteristics |
|--------|---------------------|-----------------|
| **MapReduce** | `mr` (default, legacy) | Disk-based, slow, highly stable |
| **Tez** | `tez` | DAG-based, faster (2–5x), preferred in Hortonworks/CDP |
| **Spark** | `spark` | In-memory, fastest for iterative, uses Spark cluster |

```sql
-- Set execution engine per session
SET hive.execution.engine=tez;
SET hive.execution.engine=spark;
SET hive.execution.engine=mr;
```

### 14.3 Hive Metastore

The **Metastore** is the central metadata repository:

| Mode | Description | Use Case |
|------|-------------|----------|
| **Embedded (Derby)** | Default, single-user, in-process | Development/testing only |
| **Local** | External DB (MySQL/PostgreSQL), same JVM | Small teams |
| **Remote** | External DB + Thrift server (separate process) | Production, multi-user |

Other tools (Spark, Impala, Presto) can share the same Hive Metastore — enabling a unified schema across the ecosystem.

### 14.4 HiveServer2 and Beeline

**HiveServer2** is a service that enables multiple clients to submit queries to Hive concurrently:

```bash
# Start HiveServer2
hiveserver2 &

# Connect using Beeline (JDBC client)
beeline -u "jdbc:hive2://localhost:10000/default" -n hadoop

# Run a query in Beeline
0: jdbc:hive2://localhost:10000/default> SELECT COUNT(*) FROM employees;
```

**Beeline vs HiveCLI:**
| Aspect | HiveCLI (old) | Beeline (new) |
|--------|--------------|--------------|
| Connection | Direct to Hive | Via HiveServer2 (Thrift) |
| Multi-user | No | Yes |
| Security | Limited | Kerberos, LDAP |
| Recommended | Deprecated | Yes |

### 14.5 JDBC/ODBC Connectivity

BI tools (Tableau, Power BI, DBeaver) connect to Hive via JDBC/ODBC through HiveServer2:

```java
// Java JDBC example
Class.forName("org.apache.hive.jdbc.HiveDriver");
Connection conn = DriverManager.getConnection(
    "jdbc:hive2://hiveserver:10000/analytics_db", "hadoop", "");
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM employees LIMIT 10");
while (rs.next()) {
    System.out.println(rs.getString("name") + "\t" + rs.getDouble("salary"));
}
```

### 14.6 Hive and HDFS Data Storage

All Hive table data lives in HDFS:

```bash
# Default warehouse location
/user/hive/warehouse/

# Database location
/user/hive/warehouse/analytics_db.db/

# Table location
/user/hive/warehouse/analytics_db.db/employees/

# Partitioned table
/user/hive/warehouse/analytics_db.db/web_logs/
  log_year=2024/
    log_month=1/
      log_day=15/
        000000_0     ← actual data files (ORC/Parquet/etc.)
        000001_0
```

```bash
# View HDFS files for a Hive table
hdfs dfs -ls /user/hive/warehouse/analytics_db.db/employees/

# Check file format and size
hdfs dfs -du -h /user/hive/warehouse/analytics_db.db/employees/
```

### 14.7 SerDe (Serializer/Deserializer)

**SerDe** defines how Hive reads (deserializes) data from storage and writes (serializes) it back:

| SerDe | Used For | Example |
|-------|----------|---------|
| `LazySimpleSerDe` | Delimited text (CSV/TSV) | Default for TEXTFILE |
| `OpenCSVSerde` | Proper CSV with quoting | CSV with commas in fields |
| `JsonSerDe` | JSON files | Semi-structured JSON logs |
| `RegexSerDe` | Regex-parsed text | Apache access logs |
| `OrcSerde` | ORC files | ORC format |
| `ParquetHiveSerDe` | Parquet files | Parquet format |
| `AvroSerDe` | Avro files | Avro format |

```sql
-- JSON SerDe example
CREATE EXTERNAL TABLE events (
    user_id  INT,
    event    STRING,
    ts       TIMESTAMP
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE
LOCATION '/data/events/';

-- Regex SerDe for Apache access logs
CREATE EXTERNAL TABLE access_logs (
    ip_address  STRING,
    request     STRING,
    status_code INT,
    bytes       BIGINT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
    'input.regex' = '(\\S+) \\S+ \\S+ \\[.*\\] "(.*)" (\\d{3}) (\\d+|-)'
)
STORED AS TEXTFILE
LOCATION '/data/access_logs/';
```

### 14.8 Hive Query Optimization Tips

| Technique | How | Benefit |
|-----------|-----|---------|
| **Partitioning** | Filter on partition column | Reads only relevant files |
| **Bucketing** | Cluster by join key | Enables bucket map join |
| **ORC/Parquet** | Use columnar format | Column pruning + compression |
| **Vectorized Execution** | `SET hive.vectorized.execution.enabled=true` | Batch row processing |
| **Tez Engine** | `SET hive.execution.engine=tez` | Faster than MapReduce |
| **Map Join** | Small table broadcast | Avoids shuffle for small table joins |
| **Cost-Based Optimizer** | `SET hive.cbo.enable=true` | Auto join reordering, predicate pushdown |
| **Parallel Execution** | `SET hive.exec.parallel=true` | Independent stages run simultaneously |
| **Compression** | Snappy/LZO/Zlib on ORC | Reduces I/O and storage |

### 14.9 HCatalog

**HCatalog** (part of Hive) exposes Hive's Metastore as a REST API (`WebHCat`), enabling other Hadoop tools to work with Hive-managed schemas:

- **MapReduce jobs** can read Hive tables without knowing file format/location
- **Pig** can read and write Hive-managed tables
- **Sqoop** can import data directly into Hive-managed table format

### 14.10 Common Hive Configuration Settings

```sql
-- Enable local mode (for small datasets, runs in single JVM)
SET hive.exec.mode.local.auto=true;
SET hive.exec.mode.local.auto.inputbytes.max=67108864;   -- 64 MB

-- Set number of reducers
SET mapred.reduce.tasks=20;
SET hive.exec.reducers.bytes.per.reducer=67108864;

-- Enable dynamic partition mode
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;

-- Map join (broadcast small tables)
SET hive.auto.convert.join=true;
SET hive.mapjoin.smalltable.filesize=25000000;   -- 25 MB

-- Fetch task (for simple queries, skip MapReduce entirely)
SET hive.fetch.task.conversion=more;

-- Enable vectorization
SET hive.vectorized.execution.enabled=true;
SET hive.vectorized.execution.reduce.enabled=true;

-- Parallel execution
SET hive.exec.parallel=true;
SET hive.exec.parallel.thread.number=8;
```

---

## Summary Table

| Topic | Key Points |
|-------|-----------|
| **Hadoop** | Open-source distributed storage + processing; HDFS + YARN + MapReduce; horizontal scale on commodity hardware |
| **HDFS** | Master-slave; NameNode (metadata) + DataNodes (data blocks); 128 MB blocks; 3x replication; rack-aware placement |
| **MapReduce** | Map → Shuffle/Sort → Reduce; data locality; combiner for optimization; fault-tolerant via task retry |
| **YARN** | ResourceManager (Scheduler + AsM) + NodeManager + ApplicationMaster + Containers; supports multiple frameworks |
| **File Read** | NameNode returns block locations (rack-nearest); client reads directly from DataNode; automatic failover |
| **File Write** | Client → DN1 → DN2 → DN3 pipeline; ACK flows back; NameNode records metadata; block replicated automatically |
| **Shell** | `hdfs dfs -ls/put/get/rm/mkdir/cat/mv/cp/chmod/chown/setrep` |
| **Ecosystem** | Hive, Pig, Spark, HBase, Sqoop, Flume, Kafka, Oozie, ZooKeeper, Ambari |
| **Hive** | SQL on HDFS; HiveQL → MapReduce/Tez/Spark; Metastore stores schema; internal vs external tables |
| **Hive Data Types** | TINYINT to BIGINT; FLOAT/DOUBLE/DECIMAL; STRING/VARCHAR/CHAR; DATE/TIMESTAMP; ARRAY/MAP/STRUCT |
| **DDL** | CREATE/ALTER/DROP DATABASE, TABLE; ADD/DROP COLUMNS; ADD/DROP PARTITION; LOAD DATA; CTAS |
| **Functions** | String, Math, Date, Aggregate, Conditional (CASE/COALESCE), Collection (EXPLODE), Window (RANK/LAG) |
| **Views** | Virtual tables (named queries); read-only; simplify complex queries; Materialized Views store results |
| **Hive-Hadoop** | HiveServer2 (JDBC); Metastore (MySQL); HDFS storage; Tez/Spark engines; SerDe for format parsing |

---

*End of Unit 1 — Big Data Analytics*

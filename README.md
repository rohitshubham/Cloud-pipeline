# Cloud-pipeline

---
[![Build Status](https://travis-ci.com/rohitshubham/Cloud-pipeline.svg?branch=master)](https://travis-ci.com/rohitshubham/Cloud-pipeline)

---

### About the tool

---
### Different components

---
### Running the Kafka
To run the cloud pipeline service, we need to perform the follwing:

#### 1. Starting Kafka

To start Kakfa, first run zookeeper:

```bash
$ docker-compose up -d zookeeper
```

Next start the Kafka brokers by:
```bash
$ docker-compose up --scale kafka=NUMBER_OF_BROKERS
```
#### 2. Start Mongo Databse
To start MongoDB, just run the command:

```bash
$ docker-compose up -d database
```

#### 3. Start the database-consumer:
To start the Kafka consumer service, run the following command while Kafka is running:

```bash
$ docker-compose up  --scale kafka=NUMBER_OF_BROKERS  database-processor
```

Note: The Kafka Consumer requires a comma seperated list of Kafka brokers. It has to be provided in the `entrypoint` config of the `docker-compose.yml` file.
Example: `entrypoint: ["python3", "MongoIngestor.py", "192.168.1.12:32812,192.168.1.12:32814", "kafka-database-consumer-group-2"]`

#### 4. Start Apache Spark
To start spark, run the following docker-compose command

* Start master/controller node
```bash
$ docker-compose up spark
```
* Start multiple instances of worker/resposender node
```bash
$ docker-compose scale spark-worker=2
```
#### 5. Start the stream-processor application
To start the stream-processor application, use the following command:

```bash
$ docker-compose up --scale kafka=2 stream-processor
```
#### 6. Start the database-ingestion application
Start this using:

```bash
$ docker-compose up --scale kafka=2 database-processor
```

Note: The `database-processor` and `stream-processor` applications both belong to separate consumer groups in Kafka. As such, running both of them will provide simultaneous stream ingestion and processing capability.
---

### Monitoring the application
---

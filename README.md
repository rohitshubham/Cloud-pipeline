# Cloud-pipeline- Work in progress  :)

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

#### 2. Start the consumer:
To start the Kafka consumer service, run the following command while Kafka is running:

```bash
$ docker-compose up  --scale kafka=NUMBER_OF_BROKERS  kafka-consumer
```

Note: The Kafka Consumer requires a comma seperated list of Kafka brokers. It has to be provided in the `entrypoint` config of the `docker-compose.yml` file.
Example: `entrypoint: ["python3", "KafkaConsumer.py", "192.168.1.12:32780,192.168.1.12:32779"]`

---
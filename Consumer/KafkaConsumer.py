from kafka import KafkaConsumer
import msgpack
import logging
import sys

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger("mini-batcher-application")
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.DEBUG)
rootLogger.addHandler(consoleHandler)

class KafkaMessageConsumer:
    def __init__(self, servers):
        super().__init__()
        self.consumer = KafkaConsumer(bootstrap_servers = servers, value_deserializer=msgpack.unpackb)
        self.consumer.subscribe(pattern="sensors.temperature.edge_1")
        rootLogger.info("Connected to Kafka broker")

    def consume(self):
        for message in self.consumer:
            rootLogger.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

kafka_brokers=sys.argv[1].split(',')
running = True

kafka_consumer = KafkaMessageConsumer(kafka_brokers)

kafka_consumer.consume()
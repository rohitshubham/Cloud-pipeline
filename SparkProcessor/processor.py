from kafka import KafkaConsumer
import msgpack
import logging
import sys
import json


logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger("mini-batcher-application")
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.DEBUG)
rootLogger.addHandler(consoleHandler)


class KafkaMessageConsumer:
    def __init__(self, servers, group_name):
        super().__init__()
        self.consumer = KafkaConsumer(bootstrap_servers = servers, group_id = group_name, value_deserializer=msgpack.unpackb)
        self.consumer.subscribe(pattern="sensors.temperature.*")
        rootLogger.info("Connected to Kafka broker")

    def consume(self):
        for message in self.consumer:
            rootLogger.info("Message Topic:%s, Partition:%d, Offset:%d" % (message.topic, message.partition,
                                          message.offset))
            
            metadata={
                "topic": message.topic,
                "partition" : message.partition,
                "offset" : message.offset
            }

            data= {
                "metadata_id": result.inserted_id,
                "topic" : message.topic,
                "message" : message.value
                }

            
kafka_brokers=sys.argv[1].split(',')
group_name = sys.argv[2]
running = True

kafka_consumer = KafkaMessageConsumer(kafka_brokers, group_name)


kafka_consumer.consume()
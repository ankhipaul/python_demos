"""
Produces messages and publishes into Kafka topic (ankhitest2).
A series of numbers from 1-100 are being published into the topic.
"""
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['dev-cloudera-kafka.data.giltaws.com:9092'],
                         value_serializer=lambda x:dumps(x).encode('utf-8'))

for e in range(100):
    data = {'number' : e}
    producer.send('ankhitest2', value=data)
    sleep(5)

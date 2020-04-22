from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'ankhitest2',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('consumer data:{}'.format(message))
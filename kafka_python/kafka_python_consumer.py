from kafka import KafkaConsumer
from json import loads
import csv

f2 = r'/home/apaul/pythonconsumer.csv'

consumer = KafkaConsumer(
    'ankhitest2',
    bootstrap_servers=['dev-cloudera-kafka.data.giltaws.com:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

msg_buffer = []
buffer_size = 100

for msg in consumer:
        msg_buffer.append(msg[6])
        if len(msg_buffer) >= buffer_size:
            with open(f2, "w+") as file:
                filewriter = csv.writer(file)
                for _msg in msg_buffer:
                    filewriter.writerow(["consumer data:{}".format(_msg)])
                msg_buffer = []
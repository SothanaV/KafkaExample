from kafka import KafkaConsumer
import json
consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))

# for msg in consumer:
#     print(msg)

print(consumer)
from kafka import KafkaProducer

import json
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda m: json.dumps(m).encode('ascii'))

r = producer.send('my-topic', {'key': 'value'}).get()

# print(producer)
print(r)
# for i in r:
#     print(i)
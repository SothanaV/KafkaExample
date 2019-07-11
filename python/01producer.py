from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
r = producer.send('my-topic', key=b'key',value=b'value').get()
for i in r:
    print(i)
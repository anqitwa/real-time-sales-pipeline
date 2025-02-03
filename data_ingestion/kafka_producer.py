from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_sales():
    return {
        "transaction_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10.5, 1000.99), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

while True:
    data = generate_sales()
    producer.send('sales_topic', data)
    print(f"Sent: {data}")
    time.sleep(2)

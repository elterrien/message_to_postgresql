import random

import pika
from time import sleep

url = 'amqp://user:password@localhost:5672/default_vhost'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare('temperature')
channel.queue_bind('temperature', 'amq.direct', 'temperature_routing_key')
while True:
    sleep(3)
    channel.basic_publish('amq.direct', 'temperature_routing_key', body=str(random.uniform(0, 100)))

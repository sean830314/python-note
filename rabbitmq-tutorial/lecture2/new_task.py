#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)     # message durability

message = ' '.join(sys.argv[1:]) or "Hello World!"
"""
The empty string denotes the default or nameless exchange: 
messages are routed to the queue with the name specified by routing_key, if it exists.
"""
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
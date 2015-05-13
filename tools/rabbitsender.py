#!/usr/bin/env python
import pika
import logging
import time

logging.basicConfig()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', virtual_host='/', credentials = credentials))

channel = connection.channel()

channel.queue_declare(queue='gnq')
channel.basic_publish(exchange='',
                      routing_key='',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"

connection.close()

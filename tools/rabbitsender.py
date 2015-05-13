#!/usr/bin/env python
import pika
import logging
logging.basicConfig()

credentials = pika.PlainCredentials('gn', 'gn')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', virtual_host='gn', credentials = credentials))
channel = connection.channel()

channel.queue_declare(queue='my-queue')
channel.basic_publish(exchange='',
                      routing_key='my-queue',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()

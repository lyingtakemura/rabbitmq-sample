from uuid import uuid4

import pika


def on_message(ch, method, properties, body):
    print(f"REPLY_FROM_SERVER: {body}")


connection_parameters = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
reply_queue = channel.queue_declare(queue="")
channel.basic_consume(
    queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_message
)

channel.queue_declare(queue="requests")
channel.basic_publish(
    exchange="",
    routing_key="requests",
    body="REQUESTING_REPLY",
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue, correlation_id=str(uuid4())
    ),
)

channel.start_consuming()

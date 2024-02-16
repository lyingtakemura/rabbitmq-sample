import pika


def on_message(ch, method, properties, body):
    print(f"CONSUMER_1: {body}")


connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
queue = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(exchange="pubsub", queue=queue.method.queue)

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message
)

print("START_CONSUMER_1")

channel.start_consuming()

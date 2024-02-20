import pika
from pika.exchange_type import ExchangeType


def on_message(ch, method, properties, body):
    print(f"PAYMENTS_CONSUMER: {body}")


connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)
queue = channel.queue_declare(queue="", exclusive=True)
channel.queue_bind(exchange="routing", queue=queue.method.queue, routing_key="payments")

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message
)

print("PAYMENTS_CONSUMER_START")

channel.start_consuming()

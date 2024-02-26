import pika


def on_message(ch, method, properties, body):
    print(f"REQUEST: {properties.correlation_id}")
    ch.basic_publish(
        "",
        routing_key=properties.reply_to,
        body=f"SERVERE_REPLY: {properties.correlation_id}",
    )


connection_parameters = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.queue_declare(queue="requests")
channel.basic_consume(queue="requests", auto_ack=True, on_message_callback=on_message)
print("START_SERVER")
channel.start_consuming()

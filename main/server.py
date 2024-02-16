import pika

connection_parameters = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange="logs_exchange", exchange_type="fanout")
channel.queue_declare(queue="logs_queue")
channel.queue_bind(exchange="logs_exchange", queue="logs_queue")


def callback(channel, method, properties, body):
    print("CHANNEL", channel)
    print("METHOD", method)
    print("PROPERTIES", dir(properties))
    print("BODY", body.decode("utf-8"))


channel.basic_consume(queue="logs_queue", on_message_callback=callback, auto_ack=True)

try:
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

while True:
    try:
        message = channel.basic_publish(
            exchange="logs_exchange", routing_key="logs_queue", body=input("> ")
        )
    except KeyboardInterrupt:
        break
connection.close()

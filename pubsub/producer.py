import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)
channel.basic_publish(exchange="pubsub", routing_key="", body="FANOUT_NOTIFICATION")

connection.close()

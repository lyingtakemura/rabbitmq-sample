import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host="localhost")
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)
channel.basic_publish(exchange="routing", routing_key="payments", body="ROUNTER_MESSAGE")

connection.close()

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="test", durable=True)

message = input("tell us what you want to say")

while (message != "exit") :
	channel.basic_publish(exchange='test_exchange', routing_key='', body=message)
	print("message sent")
	message = input("tell us what you want to say")
connection.close()

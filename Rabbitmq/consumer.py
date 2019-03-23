import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue="test", durable=True)

def callback(ch, method, properties, body) :
	print(body)

channel.basic_consume(callback, queue="test", no_ack=True)

print("Waiting for a message\n")

channel.start_consuming()

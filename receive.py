import pika


credentials = pika.PlainCredentials('username', 'password')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='your_host', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='queue_name')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='queue_name', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

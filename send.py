import pika


credentials = pika.PlainCredentials('username', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='your_host',
        credentials=credentials))
channel = connection.channel()

sample_obj = {
    "name": "your_name",
    "age": 00,
    "sex": "MALE"
}

channel.queue_declare(queue='queue_name')


channel.basic_publish(
    exchange='', routing_key='queue_name', body="{}".format(sample_obj))
print(" [x] Sent 'User Object!'")
connection.close()

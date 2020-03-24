import pika


credentials = pika.PlainCredentials('msd', 'MSDField1234')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='196.192.73.42',
        credentials=credentials))
channel = connection.channel()

send_obj = {
    "name": "Lawrance Massanja",
    "age": 34,
    "sex": "MALE"
}

channel.queue_declare(queue='mrc-distribution-queue')


channel.basic_publish(
    exchange='', routing_key='mrc-distribution-queue', body="{}".format(send_obj))
print(" [x] Sent 'User Object!'")
connection.close()

# import pika


# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()

# channel.queue_declare(queue='mrc.msd.distribution')

# send_obj = {
#     "name": "Lawrance Massanja",
#     "age": 34,
#     "sex": "MALE"
# }

# channel.basic_publish(exchange='', routing_key='hello',
#                       body='{}'.format(send_obj))
# print(" [x] Sent '{}'".format(send_obj))
# connection.close()



# import pika

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()

# send_obj = {
#     "name": "Lawrance Massanja",
#     "age": 34,
#     "sex": "MALE",
#     "checkNumber": 1233123123
# }

# channel.queue_declare(queue='mrc.msd.distribution')

# channel.basic_publish(
#     exchange='', routing_key='mrc.msd.distribution', body='{}'.format(send_obj))
# print(" [x] Sent '{}'".format(send_obj))
# connection.close()

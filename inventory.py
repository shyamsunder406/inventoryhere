import pika, json

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Received order: {order['orderId']} - Decreasing inventory")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='order_exchange', exchange_type='topic', durable=True)
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='order_exchange', queue=queue_name, routing_key='order.*')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for orders...')
channel.start_consuming()

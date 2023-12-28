import pika


class Consumer:
    def __init__(self, url, queue, postgre_connector):
        self.url = url
        self.queue = queue
        self.params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.postgre_connector = postgre_connector

    def start_consuming(self):
        self.postgre_connector.connect()
        self.channel.basic_consume(self.queue, self.callback, auto_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.channel.close()
        self.connection.close()
        self.postgre_connector.disconnect()

    def callback(self, ch, method, properties, body):
        body = body.decode()
        self.postgre_connector.execute_query("INSERT INTO temperature (value) VALUES (%s)", (body,))



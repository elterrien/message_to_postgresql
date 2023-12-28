from postgre_connector import PostgreSQLConnector
from consummer import Consumer

connector = PostgreSQLConnector("postgres_db",
                                "postgres_user",
                                "password",
                                host="localhost",
                                port=5432)

consumer = Consumer("amqp://user:password@localhost:5672/default_vhost", "temperature", connector)

consumer.start_consuming()

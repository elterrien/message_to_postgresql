import psycopg2


class PostgreSQLConnector:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL successfully!")
        except Exception as e:
            print(f"Error: Unable to connect to PostgreSQL - {e}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("Disconnected from PostgreSQL.")
        except Exception as e:
            print(f"Error: Unable to disconnect from PostgreSQL - {e}")

    def execute_query(self, query, params=None):
        try:
            print(query)
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except Exception as e:
            self.connection.rollback()
            print(f"Error: Unable to execute query - {e}")

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error: Unable to fetch data - {e}")
            return None
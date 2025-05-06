import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host='localhost',
                    database='atm_management',
                    user='root',
                    password='3396404y',
                    port=3306
                )
                print("Successfully connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            raise

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            raise

    def fetch_one(self, query, params=None):
        cursor = self.execute_query(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result 
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import unittest

# Load environment variables
load_dotenv()

class DatabaseTest(unittest.TestCase):
    def setUp(self):

        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        cluster_url = os.getenv('MONGODB_CLUSTER_URL')
        db_name = os.getenv('MONGODB_DB_NAME')

        self.connection_uri = f'mongodb+srv://{username}:{password} @cluster0.xogyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

        
        self.mongo_client = MongoClient(self.connection_uri)
        self.database = self.mongo_client[db_name]

    def test_database_connection(self):

        connection_successful = False
        try:
            self.database.command('ping')
            connection_successful = True
        except Exception as error:
            print(f"Connection failed: {error}")
        
        self.assertTrue(connection_successful, "Database connection test failed.")

if __name__ == "__main__":
    unittest.main()

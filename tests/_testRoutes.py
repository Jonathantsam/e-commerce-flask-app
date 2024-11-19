import os
from pymongo import MongoClient
from dotenv import load_dotenv
import unittest
from app import app

load_dotenv()

class ProductAPITest(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.test_client.testing = True

        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        cluster_url = os.getenv('MONGODB_CLUSTER_URL')
        db_name = os.getenv('MONGODB_DB_NAME')

        self.mongo_connection_uri = ('mongodb+srv://{username}:{password} @cluster0.xogyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

        self.mongo_client = MongoClient(self.mongo_connection_uri)
        self.database = self.mongo_client[db_name]
        self.collection = self.database.get_collection('products')

    def test_document_insertion(self):
        sample_data = {'name': 'Sample Product', 'price': 15.99}
        insertion_result = self.collection.insert_one(sample_data)

        self.assertIsNotNone(insertion_result.inserted_id, "Failed to insert document into the collection.")

    def test_invalid_http_method(self):
        response = self.test_client.post('/products')  
        self.assertEqual(
            response.status_code, 405, "Endpoint did not return 405 for an invalid HTTP method."
        )

if __name__ == "__main__":
    unittest.main()

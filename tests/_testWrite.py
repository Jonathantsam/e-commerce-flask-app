import os
from pymongo import MongoClient
from dotenv import load_dotenv
import unittest

load_dotenv()

class MongoDBTestCase(unittest.TestCase):
    def setUp(self):
        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        cluster_url = os.getenv('MONGODB_CLUSTER_URL')
        db_name = os.getenv('MONGODB_DB_NAME')

        self.mongo_uri = f'mongodb+srv://{username}:{password}@{cluster_url}@cluster0.xogyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

        self.client = MongoClient(self.mongo_uri)
        self.database = self.client[db_name]
        self.products_collection = self.database.products

    def test_insert_product(self):
        product_data = {'name': 'Sample Product', 'price': 20}
        result = self.products_collection.insert_one(product_data)

        self.assertIsNotNone(result.inserted_id, "The product was not inserted successfully.")

if __name__ == "__main__":
    unittest.main()

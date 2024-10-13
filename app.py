from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://shopUser:<db_password>@cluster0.xogyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

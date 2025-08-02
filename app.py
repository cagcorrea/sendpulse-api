from Flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    products = [
        {'id': 1, 'name': "Headphone pro", 'preco': 3500.00},
        {'id': 2, 'name': "Smartphone Corporation", 'preco': 2500.00},
        {'id': 3, 'name': "Tablet Executive", 'preco': 1500.00}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run()                

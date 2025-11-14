from flask import Flask, render_template, request
import json
import csv

#flask app
app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    
    # Passer la liste au template
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        products_data = read_json()
    else:
        products_data = read_csv()
    
    if product_id:
        product_id = int(product_id)
        products_data = [p for p in products_data if p['id'] == product_id]
        
        if not products_data:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
   app.run(debug=True, port=5000)

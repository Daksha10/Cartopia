from flask import Flask, request, jsonify, send_from_directory, render_template
from sql_connection import get_sql_connection
from flask_cors import CORS
import products_dao
import orders_dao
import uom_dao
import os
import json

# Initialize Flask app
app = Flask(__name__, static_folder="../ui", template_folder="../ui")
CORS(app) 
# Establish MySQL connection
connection = get_sql_connection()

@app.route('/api/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "Backend is working!"})

# Serve the main HTML page
@app.route('/')
def index():
    return render_template("index.html")

# Serve static files (CSS, JS, Images)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

# API Routes
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Main entry point
if __name__ == "__main__":
    print("Starting Python Flask Server for Cartopia")
    port = int(os.environ.get("PORT", 5000))  # Use environment variable for port if available
    app.run(debug=False, host="0.0.0.0", port=port)

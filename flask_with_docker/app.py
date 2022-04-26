from unicodedata import name
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{
        'name': 'my item',
        'price': 15.99
    }]
},{
    'name': 'Judahs Store',
    'items': [{
        'name': 'Satellite Mobile',
        'price': 259.99
    }]
}]

#welcome page for the web application
@app.route('/')
def hello_geek():
    return render_template('index.html')

#GET request which will return all of the stores
@app.route('/allstores')
def allstores():
    return jsonify({'stores':stores})

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': [],
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET request which will return the particular store information
@app.route('/store/<string:name>')
def get_store(name):
    for i in stores:
        if i['name'] == name:
            return jsonify(i)
        else:
            return jsonify({"message": "Store not found"})

@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': "store not found"})
#Add items to stores
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({"message": "Item successfully added"})
        else:
            return jsonify({'message': "store not found"})




if __name__ == '':
    app.run(debug=True)
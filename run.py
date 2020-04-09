import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'wt_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


listcoll = mongo.db.wt_collection
itemcoll = mongo.db.wt_listitems

@app.route("/")
def hello():
    return render_template('welcomepage.html')


@app.route("/test")
def test():
    return render_template('test.html',
    collection=mongo.db.wt_collection.find())


# Function to view lists
@app.route("/mylists")
def mylists():
    return render_template('mylists.html',
    collection=mongo.db.wt_collection.find())


# Function to create a new list
@app.route("/newlist", methods=["GET", "POST"])
def newlist():

    if request.method == 'GET':
        return render_template('newlist.html')

    if request.method == 'POST':
        list_name = request.form['list_name']
        list_category = request.form['list_category']
        list_description = request.form['list_description']

        newly_added_list = {'list_name': list_name,
                            'list_category': list_category,
                            'list_description': list_description}

        listcoll.insert_one(newly_added_list)

    return redirect(url_for('additem'))


# Function to edit a list
@app.route("/editlist")
def editlist():
    return render_template('editlist.html')


# Function to view all items in a list
@app.route("/listitems")
def listitems():
    return render_template('listitems.html',
    collection=mongo.db.wt_listitems.find())


# Function to add a new item to a list
@app.route("/additem", methods=["GET", "POST"])
def additem():

    if request.method == 'GET':
        return render_template('additem.html',
        list=mongo.db.wt_collection.find())

    if request.method == 'POST':
        list_name = request.form['list_name']
        product_link = request.form['product_link']
        brand_name = request.form['brand_name']
        product_type = request.form['product_type']
        item_description = request.form['item_description']
        item_price = request.form['item_price']
        need_rating = request.form['need_rating']

        newly_added_item = {'list_name': list_name,
                            'product_link': product_link,
                            'brand_name': brand_name,
                            'product_type': product_type,
                            'item_price': item_price,
                            'need_rating': need_rating}

        itemcoll.insert_one(newly_added_item)

    return redirect(url_for('listitems'))


@app.route("/create")
def create():
    new_list_item = {'brand': 'COS',
                     'type': 'Shirt',
                     'price': '250SEK',
                     'description': 'White oversized t-shirt'}

    mongo.db.wt_listitems.insert_one(new_list_item)

    return render_template('create.html', document=new_list_item)


# Function to edit an item
@app.route("/edititem/<item_id>")
def edititem(item_id):
    _item = mongo.db.wt_listitems.find_one({'_id': ObjectId(item_id)})
    print(_item)

    return render_template('edititem.html', item_info=_item)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
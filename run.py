import os
import operator
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'wt_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["TEMPLATES_AUTO_RELOAD"] = True


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


# Function to add item from Navbar
@app.route("/navbaradd")
def navbaradd():
    return render_template('welcomepage.html',
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
                            'list_description': list_description,
                            'items': []}

        listcoll.insert_one(newly_added_list)

    return redirect(url_for('mylists'))


# Function to edit a list
@app.route("/editlist/<list_id>", methods=["GET", "POST"])
def editlist(list_id):
    lists = mongo.db.wt_collection.find_one({'_id': ObjectId(list_id)})

    if request.method == 'POST':
        list_name = request.form['list_name']
        list_category = request.form['list_category']
        list_description = request.form['list_description']

        updated_list = {'list_name': list_name,
                        'list_category': list_category,
                        'list_description': list_description,
                        'items': []}

        mongo.db.wt_collection.update({'_id': ObjectId(list_id)}, updated_list)

        return redirect(url_for('mylists'))

    return render_template('editlist.html', list_info=lists)


# Function to delete a list
@app.route("/deletelist/<list_id>")
def deletelist(list_id):
    mongo.db.wt_collection.remove({'_id': ObjectId(list_id)})

    return redirect(url_for('mylists'))


# Function to view all items in a list
@app.route("/listitems/<list_id>")
def listitems(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})
    return render_template('listitems.html', list_items=list_items)


# Function to sort items by price
@app.route("/listitems_price/<list_id>")
def listitems_price(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})

    return render_template('listitems_price.html', list_items=list_items)


# Function to sort items by brand name
@app.route("/listitems_brand/<list_id>")
def listitems_brand(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})

    return render_template('listitems_price.html', list_items=list_items)

# Function to add a new item to a list
@app.route("/additem/<list_id>", methods=["GET", "POST"])
def additem(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})

    location_for_append = list_items.items
    print(list_items)

    if request.method == 'POST':
        list_name = request.form['list_name']
        product_link = request.form['product_link']
        brand_name = request.form['brand_name']
        product_type = request.form['product_type']
        item_description = request.form['item_description']
        item_price = request.form['item_price']
        need_rating = request.form['need_rating']

        appended_item = {'_id': ObjectId(),
                         'product_link': product_link,
                         'brand_name': brand_name,
                         'product_type': product_type,
                         'item_description': item_description,
                         'item_price': item_price,
                         'need_rating': need_rating}

        listcoll.update_one({'_id': ObjectId(list_id)}, {'$push': {'items':appended_item}})

        return redirect(url_for('mylists'))
        
    return render_template('additem.html',
                            list_items=list_items)


# Function to edit an item in a list
@app.route("/edititem/<list_id>/<item_id>", methods=["GET", "POST"])
def edititem(list_id, item_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})

    for item in _list['items']:
        print(item['_id'], item_id)

        if str(item['_id']) == str(item_id):
            print('hello')
            if request.method == 'POST':
                list_name = request.form['list_name']
                product_link = request.form['product_link']
                brand_name = request.form['brand_name']
                product_type = request.form['product_type']
                item_description = request.form['item_description']
                item_price = request.form['item_price']
                need_rating = request.form['need_rating']

                item = {'list_name': list_name,
                        'product_link': product_link,
                        'brand_name': brand_name,
                        'product_type': product_type,
                        'item_description': item_description,
                        'item_price': item_price,
                        'need_rating': need_rating}
                print(brand_name)
                print(item)

                mongo.db.wt_collection.update(
                    {"items._id": ObjectId(item_id)},
                    {"$set": {"items.$.list_name": list_name,
                              "items.$.product_link": product_link,
                              "items.$.brand_name": brand_name,
                              "items.$.product_type": product_type,
                              "items.$.item_description": item_description,
                              "items.$.item_price": item_price,
                              "items.$.need_rating": need_rating}})

                return redirect(url_for('itemedited'))

            return render_template('edititem.html', 
                                    item_info=item, 
                                    list=_list)


# Function to delete an item from a list
@app.route("/deleteitem/<list_id>/<item_id>")
def deleteitem(list_id, item_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})

    for item in _list['items']:

        if str(item['_id']) == str(item_id):
            mongo.db.wt_collection.update(
                {"items._id": ObjectId(item_id)},
                {"$pull": { 'items': {"_id": ObjectId(item_id)}}})
            print(item_id)

    return redirect(url_for('deleteconfirmation'))


# When an item has been added
@app.route("/itemadded")
def itemadded():
    return render_template('itemadded.html')


# When an item has been edited
@app.route("/itemedited")
def itemedited():
    return render_template('itemedited.html')


@app.route("/deleteconfirmation")
def deleteconfirmation():
    return render_template('deleteconfirmation.html')


# Test to check data can be sent to database
@app.route("/create")
def create():
    # new_list_item = {'brand': 'COS',
    #                  'type': 'Shirt',
    #                  'price': '250SEK',
    #                  'description': 'White oversized t-shirt'}

    # mongo.db.wt_listitems.insert_one(new_list_item)

    new_list_item = {'list_name': 'May clothes',
                     'list_description': 'Clothes I want to buy next month',
                     'list_item': [{
                         'type': 'shirt',
                         'brand': 'COS',
                         'price': '250'
                     }]
                     }

    mongo.db.wt_listitems.insert_one(new_list_item)

    return render_template('create.html', document=new_list_item)


@app.route("/mumsbirthday")
def mumsbirthday():
    # results = itemcoll.find({'list_name': 'Mums birthday'})

    # return render_template('testresults.html', results=results)

    for items in itemcoll.find({'list_name':'Mums birthday'}):
        return render_template('testresults.html',
                                results=items)


# To check query is correct
for items in itemcoll.find({'list_name': 'Mums birthday'}):
    print(items)

# How many documents use count_documents    
print(listcoll.count_documents({}))

print(listcoll.count_documents({'list_name': 'Holiday gear'}))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
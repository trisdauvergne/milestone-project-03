import os
import operator
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from operator import itemgetter
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


@app.route("/hello")
def hello():
    return render_template('welcomepage.html')


# View Lists
@app.route("/mylists")
def mylists():
    navbar_collection = mongo.db.wt_collection.find()
    return render_template('mylists.html',
                           collection=mongo.db.wt_collection.find(),
                           navbar_location=navbar_collection)


# Sort lists alphabetically
@app.route("/mylists_names")
def mylists_names():
    return render_template('mylists_names.html',
                           collection=mongo.db.wt_collection.find())


# To add to list after clicking on add an item in navbar
@app.route("/mylists_additem")
def mylists_additem():
    return render_template('mylists_additem.html',
                           collection=mongo.db.wt_collection.find())


# Create a brand new list
@app.route("/newlist", methods=["GET", "POST"])
def newlist():
    navbar_collection = mongo.db.wt_collection.find()
    if request.method == 'GET':
        return render_template('newlist.html',
                               navbar_location=navbar_collection)

    if request.method == 'POST':
        list_name = request.form['list_name']
        list_description = request.form['list_description']

        newly_added_list = {'list_name': list_name,
                            'list_description': list_description,
                            'items': []}

        listcoll.insert_one(newly_added_list)

    return render_template('listadded.html',
                           navbar_location=navbar_collection)


# Confirmation that a new list has been created
@app.route("/listadded")
def listadded():
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('listadded.html',
                           navbar_location=navbar_collection)


# Edit an existing list
@app.route("/editlist/<list_id>", methods=["GET", "POST"])
def editlist(list_id):
    lists = mongo.db.wt_collection.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    if request.method == 'POST':
        list_name = request.form['list_name']
        list_description = request.form['list_description']

        result = mongo.db.wt_collection.find_one({'_id': ObjectId(list_id)})

        updated_list = {'list_name': list_name,
                        'list_description': list_description,
                        'items': result['items']}

        mongo.db.wt_collection.update({'_id': ObjectId(list_id)}, updated_list)

        return redirect(url_for('listedited',
                                list_id=list_id))

    return render_template('editlist.html',
                           list_info=lists,
                           navbar_location=navbar_collection)


# Confirm that a list has been edited
@app.route("/listedited/<list_id>")
def listedited(list_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('listedited.html',
                           _list=_list,
                           navbar_location=navbar_collection)


# Delete a list
@app.route("/deletelist/<list_id>")
def deletelist(list_id):
    mongo.db.wt_collection.remove({'_id': ObjectId(list_id)})

    return redirect(url_for('deleteconfirmation_list'))


# View all items in a list
@app.route("/listitems/<list_id>")
def listitems(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()
    return render_template('listitems.html',
                           list_items=list_items,
                           navbar_location=navbar_collection)


# Display items in a list by price
@app.route("/listitems_price/<list_id>")
def listitems_price(list_id):
    navbar_collection = mongo.db.wt_collection.find()
    _list = listcoll.find_one({'_id': ObjectId(list_id)})

    list_items = listcoll.find_one({'_id': ObjectId(list_id)})

    list_of_items = list_items['items']

    for item in list_of_items:
        item['item_price'] = int(item['item_price'])
    newlist = sorted(list_of_items, key=itemgetter('item_price'))

    return render_template('listitems_price.html',
                           list_items=newlist,
                           _list=_list,
                           navbar_location=navbar_collection)


# Sort items by need rating (highest to lowest)
@app.route("/listitems_urgency/<list_id>")
def listitems_urgency(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('listitems_urgency.html',
                           list_items=list_items,
                           navbar_location=navbar_collection)


# Sort items by brand name (ascending order)
@app.route("/listitems_brand/<list_id>")
def listitems_brand(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('listitems_brand.html',
                           list_items=list_items,
                           navbar_location=navbar_collection)


# Add a new item to a list
@app.route("/additem/<list_id>", methods=["GET", "POST"])
def additem(list_id):
    list_items = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    if request.method == 'POST':
        product_link = request.form['product_link']
        image_link = request.form['image_link']
        brand_name = request.form['brand_name']
        product_type = request.form['product_type']
        item_description = request.form['item_description']
        item_price = request.form['item_price']
        need_rating = request.form['need_rating']

        appended_item = {'_id': ObjectId(),
                         'product_link': product_link,
                         'image_link': image_link,
                         'brand_name': brand_name,
                         'product_type': product_type,
                         'item_description': item_description,
                         'item_price': item_price,
                         'need_rating': need_rating}

        listcoll.update_one({'_id': ObjectId(list_id)},
                            {'$push': {'items': appended_item}})

        return redirect(url_for('itemadded',
                                list_id=list_id))

    return render_template('additem.html',
                           list_items=list_items,
                           navbar_location=navbar_collection)


# Edit an existing item in a list
@app.route("/edititem/<list_id>/<item_id>", methods=["GET", "POST"])
def edititem(list_id, item_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    for item in _list['items']:

        if str(item['_id']) == str(item_id):
            if request.method == 'POST':
                product_link = request.form['product_link']
                image_link = request.form['image_link']
                brand_name = request.form['brand_name']
                product_type = request.form['product_type']
                item_description = request.form['item_description']
                item_price = request.form['item_price']
                need_rating = request.form['need_rating']

                item = {'product_link': product_link,
                        'image_link': image_link,
                        'brand_name': brand_name,
                        'product_type': product_type,
                        'item_description': item_description,
                        'item_price': item_price,
                        'need_rating': need_rating}

                mongo.db.wt_collection.update(
                    {"items._id": ObjectId(item_id)},
                    {"$set": {
                              "items.$.product_link": product_link,
                              "items.$.image_link": image_link,
                              "items.$.brand_name": brand_name,
                              "items.$.product_type": product_type,
                              "items.$.item_description": item_description,
                              "items.$.item_price": item_price,
                              "items.$.need_rating": need_rating}})

                return redirect(url_for('itemedited', list_id=list_id))

            return render_template('edititem.html',
                                   item_info=item,
                                   list=_list,
                                   navbar_location=navbar_collection)


# Delete an existing item from a list
@app.route("/deleteitem/<list_id>/<item_id>")
def deleteitem(list_id, item_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})

    for item in _list['items']:

        if str(item['_id']) == str(item_id):
            mongo.db.wt_collection.update(
                {"items._id": ObjectId(item_id)},
                {"$pull": {'items': {"_id": ObjectId(item_id)}}})

    return render_template('deleteconfirmation.html',
                           _list=_list)


# Confirmation that an item has been added to an existing list
@app.route("/itemadded/<list_id>")
def itemadded(list_id):
    _list = listcoll.find_one({'_id': ObjectId(list_id)})
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('itemadded.html',
                           navbar_location=navbar_collection,
                           _list=_list)


# Confirmation that an item has been added to an existing list
@app.route("/itemedited/<list_id>")
def itemedited(list_id):
    navbar_collection = mongo.db.wt_collection.find()
    _list = listcoll.find_one({'_id': ObjectId(list_id)})

    return render_template('itemedited.html',
                           _list=_list,
                           navbar_location=navbar_collection)


# Confirmation when a list is deleted
@app.route("/deleteconfirmation_list")
def deleteconfirmation_list():
    navbar_collection = mongo.db.wt_collection.find()

    return render_template('deleteconfirmation_list.html',
                           navbar_location=navbar_collection)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")))

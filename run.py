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


coll = mongo.db.wt_collection

@app.route("/")
def hello():
    return render_template('welcomepage.html')


@app.route("/test")
def test():
    return render_template('test.html',
    collection=mongo.db.wt_collection.find())


@app.route("/mylists")
def mylists():
    return render_template('mylists.html',
    collection=mongo.db.wt_collection.find())


@app.route("/listitems")
def listitems():
    return render_template('listitems.html',
    collection=mongo.db.wt_collection.find())


@app.route("/additem", methods=["GET", "POST"])
def additem():

    if request.method == 'GET':
        return render_template('additem.html')

    if request.method == 'POST':
        additem_listname = request.form['additem_listname']
        additem_productlink = request.form['additem_productlink']
        additem_brandname = request.form['additem_brandname']
        additem_productcat = request.form['additem_productcat']
        additem_price = request.form['additem_price']
        additem_urgency = request.form['additem_urgency']

        newly_added_item = {'additem_listname': additem_listname,
                            'additem_productlink': additem_productlink,
                            'additem_brandname': additem_brandname,
                            'additem_productcat': additem_productcat,
                            'additem_price': additem_price,
                            'additem_urgency': additem_urgency}

        coll.insert_one(newly_added_item)

    return render_template('listitems.html')

@app.route("/create")
def create():
    new_list_item = {'brand': 'COS',
                     'type': 'Shirt',
                     'price': '250SEK',
                     'description': 'White oversized t-shirt'}

    mongo.db.wt_collection.insert_one(new_list_item)

    return render_template('create.html', document=new_list_item)


@app.route("/edititem")
def edititem():
    return render_template('edititem.html')


@app.route("/newlist")
def newlist():
    return render_template('newlist.html')


@app.route("/editlist")
def editlist():
    return render_template('editlist.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
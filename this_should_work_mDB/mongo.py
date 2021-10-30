from pymongo import MongoClient
import csv
import json
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

@app.route("/count")
def cun():
    client = MongoClient('mongodb://m_admin:m_admin@localhost:27017')
    with client:
        db = client.db
        count = db.res.count()
        k = db.res.find({'mesh_file': 'r0a0n200.xml' })
    return k

@app.route("/res")
def res():
    client = MongoClient('mongodb://m_admin:m_admin@localhost:27017')
    with client:
        db = client.db
        res = db.res.find()
        count = db.res.count()
    return render_template("my_template.html", data=res, count=count)

@app.route("/clear")
def clear():
    client = MongoClient('mongodb://m_admin:m_admin@localhost:27017')
    with client:
        db = client.db
        db.res.remove({})
    return redirect(url_for('res'))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5002)

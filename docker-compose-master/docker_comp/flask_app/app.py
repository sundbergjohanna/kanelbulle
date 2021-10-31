from celery import Celery
from flask import Flask, render_template, redirect, url_for
from celery.execute import send_task
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)
simple_app = Celery('worker',
                    broker='amqp://admin:admin@rabbit:5672',
                    backend='rpc://')

# ---- Flask Test ---- #
@app.route('/flasktest/<name>')
def proc(name):
    return name


# ---- Airfoil: worker ---- #
@app.route('/murtazo')
def mur_test():
    #res = test.delay()
    file = 'r0a0n200.xml'
    res = simple_app.send_task('cel_mur.calculate', [file])
    id = res.id
    #return res.get()
    #list = res.get()
    #return render_template("my_template.html", data=list)
    return res.get()

# ---------------------------- #

@app.route("/res")
def res():
    client = MongoClient('mongodb://m_admin:m_admin@mongo:27017')
    with client:
        db = client.db
        res = db.res.find()
        count = db.res.count()
    return render_template("res_template.html", data=res, count=count)

@app.route("/clear")
def clear():
    client = MongoClient('mongodb://m_admin:m_admin@mongo:27017')
    with client:
        db = client.db
        db.res.remove({})
    return redirect(url_for('res'))

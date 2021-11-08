from celery import Celery
from flask import Flask, render_template, redirect, url_for, request
from celery.execute import send_task
from pymongo import MongoClient
from bson import json_util
import json
from requests import get
import os

app = Flask(__name__)
simple_app = Celery('worker',
                    broker='amqp://admin:admin@rabbit:5672',
                    backend='rpc://')

@app.route("/home")
def home():
    return render_template("temp2.html")

@app.route('/home', methods=['POST'])
def home_post():
    text = request.form['text']
    num_of_files = text.upper()
 
    mesh_file_list = []
    folder = os.listdir('./xmls')
    for file in folder:
        if len(mesh_file_list) < int(num_of_files):
            mesh_file_list.append(file)

    for arg in mesh_file_list:
       simple_app.send_task('cel_mur.calculate', [arg])


    return redirect(url_for('home'))

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

# Flower
@app.route("/flower")
def flower():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return redirect("http://" + ip + ":8888", code=302)

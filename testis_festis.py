#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:35:18 2021
@author: johannasundberg
"""
import json
import os
from celery import Celery
from flask import Flask, jsonify
import runsh_script as airfoil


def make_celery(app):
    #from https://flask.palletsprojects.com/en/2.0.x/patterns/celery/
    celery = Celery(app.import_name, backend='rpc://',
                    broker='pyamqp://guest@localhost//')
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
  
  flask_app = Flask(__name__)
celery = make_celery(flask_app)

#Flask methods
@flask_app.route('/result', methods=['GET'] )
def one_airfoil_run():
    res = run_simulation.delay()
    result = res.get()
    return jsonify(result)

  
#Celery task normalized result
@celery.task(name='make_celery.')
def run_simulation():
    #MESH INPUT
    start = '0';     stop = '10';     nr = '2';        nodes = '50';    refine_levels = '1'
    #AIRFOIL INOUT
    s = '10';      nu = '0.01';       speed = '10.';     T = '1';        file = 'r0a0n50.xml' 

    if airfoil.run_mesh_script(start, stop, nr, nodes, refine_levels):
          print("*** Data generated :))) ***")

          if airfoil.run_airfoil(s, nu, speed, T, file):
                  print("*** AIRFOIL SIM SUCCEEDED ***")
                  airfoil.retrieve_results(file)
          else:
                  print("*** AIRFOIL FAIL ***")  

    airfoil_dir = "murtazo/navier_stokes_solver"
    cwd = os.getcwd()
    os.chdir(airfoil_dir)
    os.chdir('res_' + file)
    
    result_file = open('drag_ligt.m','r')
    
    contents = result_file.read()
    dictionary = ast.literal_eval(contents)

    result_file.close()
    
    return dictionary

  
  
if __name__ == '__main__':
  flask_app.run(host='0.0.0.0',debug=True)
  
  

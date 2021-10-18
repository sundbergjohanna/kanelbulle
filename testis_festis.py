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
@celery.task(name='make_celery.run_airfoil')
def run_airfoil(sample, nu, velocity, endtime, meshfile):
        # run_airfoil('10','0.0001', '10.', '1', 'r0a0n50.xml')
        # Inputs as string
        # run_airfoil(samples, viscosity nu, velocity speed, total time, mesh file)
        cwd = os.getcwd()
        print(cwd)
        os.chdir(airfoil_dir)
        print('meshfile =', meshfile)
        msh_dir = "../cloudnaca/msh/"
        print('msh_dir + mesfile=', msh_dir + meshfile)
        
        try:
                print("$ ./airfoil", sample, nu, velocity, endtime, msh_dir + meshfile)
                print("Starting airfoil executable simulation...")
                subprocess.check_call(["./airfoil", sample, nu, velocity, endtime, msh_dir + meshfile])
                os.chdir(cwd)
                retrieve_results(meshfile)
        except:
                print("Unexpected error:", sys.exc_info()[0])
                
        airfoil_dir = "murtazo/navier_stokes_solver"
        cwd = os.getcwd()
        os.chdir(airfoil_dir)
        os.chdir('res_' + meshfile)

        result_file = open('drag_ligt.m','r')

        contents = result_file.read()
        dictionary = ast.literal_eval(contents)

        result_file.close()
            
        return dictionary

def retrieve_results(meshfile):
        # Retrieves the result file and stores it in navier_stokes-folder in a folder named as the mesh-file used
        cwd = os.getcwd()
        print(cwd)
        os.chdir(airfoil_dir)
        try: 
                os.mkdir('res_' + meshfile)
                os.chdir('results')
                os.system('mv drag_ligt.m ../res_' + meshfile)
                os.chdir(cwd)
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False
        return True

  
  
if __name__ == '__main__':
  flask_app.run(host='0.0.0.0',debug=True)
  
  

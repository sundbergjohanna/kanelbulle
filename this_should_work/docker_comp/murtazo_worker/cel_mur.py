from celery import Celery
import os
import shutil

app = Celery('cel_mur',
             broker='amqp://admin:admin@rabbit:5672',
             backend='rpc://')

@app.task(name='cel_mur.calculate')
def calculate(xmlfile):
    os.system('./navier_stokes_solver/airfoil 5 1 5. 1 '+'./' +xmlfile)
    os.chdir("results")
    #file = open("drag_ligt.m", "r")
    #string = file.readline()
    with open("drag_ligt.m", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # Remove results folder after saving output
    os.chdir("..")
    shutil.rmtree("results")

    return lines

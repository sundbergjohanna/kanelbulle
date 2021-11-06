from pymongo import MongoClient
import os
import shutil
import json

app = Celery('cel_mur',
             broker='amqp://admin:admin@10.10.10.45:5672',
             backend='rpc://')

@app.task(name='cel_mur.calculate')
def calculate(xmlfile):
    # MongoDB client connection
    client = MongoClient('mongodb://m_admin:m_admin@10.10.10.45:27017')
    with client: # Check if result already exists
        db = client.db
        search = db.res.find({'mesh_file': xmlfile}, {"mesh_file" : 1}).limit(1)
        search = list(search)
    if search:
        return "Result already exists from file: " + xmlfile
    else:
        # Run airfoil on xml file
        os.system('./navier_stokes_solver/airfoil 5 1 5. 1 '+'./xmls/' +xmlfile)
        os.chdir("results")

        with open("drag_ligt.m", "r") as file:
            first = 0;
            time = []
            lift = []
            drag = []
            # ---- Turn result file into a dictionary ---- #
            for line in file:
                if not line.strip() == '':
                    if first == 0:
                        keys = line.split('\t')
                        #print(keys)
                        first = 1;
                    else:
                        values = line.split('\t')
                        #print(values)
                        time.append(values[0])
                        lift.append(values[1])
                        values[2] = values[2].strip('\n')
                        drag.append(values[2])

        res = {"mesh_file": xmlfile, keys[0]: time, keys[1]: lift, keys[2]: drag}

        # Insert result to database
        with client:
            db = client.db
            db.res.insert(res)

        # Remove results folder after saving output
        os.chdir("..")
        shutil.rmtree("results")

        return "Added to database."


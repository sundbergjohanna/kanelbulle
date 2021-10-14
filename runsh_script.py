
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  11 15:35:18 2021

@author: johannasundberg
"""
import os
import subprocess
import sys

script_dir = "murtazo/cloudnaca"
airfoil_dir = "murtazo/navier_stokes_solver"
msh_dir = "../cloudnaca/msh/"

def run_mesh_script(ang_0, ang_1, n_ang, n_nodes, n_lvl):
        #Input as strings:
        #run_mesh_script('0', '10', '5', '50', '1'):
        #Runs runme.sh script generating mesh files and then converts all msh files to xml using convert_xml.sh
        cwd = os.getcwd()
        print(cwd)
        os.chdir(script_dir)

        try:
                os.system("chmod +x runme.sh")
                print("$ ./runme.sh", ang_0, ang_1, n_ang, n_nodes, n_lvl)
                print("Loading...")
                subprocess.check_call(["./runme.sh", ang_0, ang_1, n_ang, n_nodes, n_lvl])
                os.chdir(cwd)
                os.system("ls -l")
                os.system("chmod +x convert_xml.sh")
                os.system("./convert_xml.sh") 
                
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False

        return True

def run_airfoil(sample, nu, velocity, endtime, meshfile):
        # run_airfoil('10','0.0001', '10.', '1', 'r0a0n50.xml'
        cwd = os.getcwd()
        print(cwd)
        os.chdir(airfoil_dir)
        print('meshfile =', meshfile)
        print('msh_dir + mesfile=', msh_dir + meshfile)
        
        try:
                print("$ ./airfoil", sample, nu, velocity, endtime, msh_dir + meshfile)
                print("Starting airfoil executable simulation...")
                subprocess.check_call(["./airfoil", sample, nu, velocity, endtime, msh_dir + meshfile])
                os.chdir(cwd)
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False
        return True

def retrieve_results(meshfile):
        cwd = os.getcwd()
        print(cwd)
        os.chdir(airfoil_dir)
        try: 
                os.mkdir('res_' + meshfile)
                os.system('cd results')
                os.system('mv drag_ligt.m ../res_' + meshfile)
                os.chdir(cwd)
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False
        return True  
  
#MESH INPUT
start = '0';     stop = '10';     nr = '2';        nodes = '50';    refine_levels = '1'
#AIRFOIL INOUT
s = '10';      nu = '0.01';       speed = '10.';     T = '1';        file = 'r0a0n50.xml'  


if run_mesh_script(start, stop, nr, nodes, refine_levels):
        print("*** Data generated :))) ***")
        
        if run_airfoil(s, nu, speed, T, file):
                print("*** AIRFOIL SIM SUCCEEDED ***")
                retrieve_results(file)
        else:
                print("*** AIRFOIL FAIL ***")
        
else:
        print("*** Failed ://// ***")
        
        

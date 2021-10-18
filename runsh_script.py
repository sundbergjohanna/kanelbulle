
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

def run_mesh_script(ang_0, ang_1, n_ang, n_nodes, n_lvl):
        #Input as strings:
        #run_mesh_script('0', '10', '5', '50', '1'):
        #run_mesh_script(angle 1, angle 2, number of angles in the span, number of nodes, number of refinement levels)
        #Runs runme.sh script generating mesh files, converst msh --> xml file using conver_xml.sh
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
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False
        return True

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

def run_airfoil_all(sample, nu, velocity, endtime, directory):
        #Does not work yet :////
        cwd = os.getcwd()
        print(cwd)
        
        all_files = os.listdir(directory)
        print(all_files)
        
        for file in all_files:
                print(file)
                run_airfoil(sample, nu, velocity, endtime, file)
                retrieve_results(file)
                
                
  
#MESH INPUT
start = '0';     stop = '10';     nr = '2';        nodes = '50';    refine_levels = '1'
#AIRFOIL INOUT
s = '10';      nu = '0.01';       speed = '10.';     T = '1';        file = 'r0a0n50.xml'  

#TESTRUN OF FUNCTIONS
if run_mesh_script(start, stop, nr, nodes, refine_levels):
        print("*** Data generated :))) ***")
else:
        print("*** Failed ://// ***")

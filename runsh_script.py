
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

def run_mesh_script(ang_0, ang_1, n_ang, n_nodes, n_lvl):
        #Input as strings:
        #run_mesh_script('0', '10', '5', '50', '1'):
        #Runs runme.sh script generating mesh files and then converts all msh files to xml using convert_xml.sh
        cwd = os.getcwd()
        print(cwd)
        os.chdir(script_dir)
        os.system("ls -l")

        try:
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


start = str(0);     stop = str(10);     nr = str(2);        nodes = str(50);    refine_levels = str(1)

if run_mesh_script(start, stop, nr, nodes, refine_levels):
        print("*** Data generated :))) ***")
else:
        print("*** Failed ://// ***")

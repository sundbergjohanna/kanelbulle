#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  11 15:35:18 2021
@author: johannasundberg
"""
import os
import subprocess
import sys

#Input variables for running the script
start = '0';     stop = '10';     nr = '2';        nodes = '50';    refine_levels = '1'

script_dir = "murtazo/cloudnaca"

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
                #os.system("ls -l")
                os.system("chmod +x convert_xml.sh")
                os.system("./convert_xml.sh") 
                
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False

        return True
      
if __name__ == '__main__':
  if run_mesh_script(start, stop, nr, nodes, refine_levels):
        print("*** XML files generated :))) ***")
  else:
        print("*** Failed ://// ***")
  

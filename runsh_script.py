
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

def run_script(ang_0, ang_1, n_ang, n_nodes, n_lvl):
        cwd = os.getcwd()
        print(cwd)
        os.chdir(script_dir)

        try:
                print("$ ./runme.sh", ang_0, ang_1, n_ang, n_nodes, n_lvl)
                print("Loading...")
                subprocess.check_call(["./runme.sh", ang_0, ang_1, n_ang, n_nodes, n_lvl])
                os.chdir(cwd)
                subprocess.call(["./convert_xml.sh"])
                
        except subprocess.CalledProcessError:
                print("Oops: ./runme.sh could not finish")
                return False
        except:
                print("Unexpected error:", sys.exc_info()[0])
                return False


        return True


start = str(0);     stop = str(10);     nr = str(2);        nodes = str(50);    refine_levels = str(1)

if run_script(start, stop, nr, nodes, refine_levels):
        print("*** Data generated :))) ***")
else:
        print("*** Failed ://// ***")

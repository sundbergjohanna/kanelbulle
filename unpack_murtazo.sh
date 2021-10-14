
#!/bin/bash

#Unpack zippacks
tar xzvf murtazo.tgz
cd murtazo
tar xvf cloudnaca.tgz
tar xvf navier_stokes_solver.tar 

#Install navier solver
echo "*Entering /navier_stokes_solver"
cd navier_stokes_solver/src
./compile_forms
cd ..
cmake .
make -j 2

#Fix gmsh
echo "*Entering /cloudnaca "
cd ..
cd cloudnaca
apt-get update
apt-get -y install gmsh
sed -i '\/Applications\/Gmsh.app\/Contents\/MacOS\/gmsh/c\GMSHBIN=\"\/usr\/bin\/gmsh\"' runme.sh
apt install python-numpy

#Test running
# ./runme.sh 0 30 10 200 3
# cd msh
# dolfin-convert r0a0n50.msh r0a0n50.xml
# cd ..
# cd ..
# cd navier_stokes_solver 
# ./airfoil 10 0.01 10. 1 ../cloudnaca/msh/r0a0n50.xml

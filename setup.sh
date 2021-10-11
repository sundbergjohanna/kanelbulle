# Setup file
#!/bin/sh

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce

sudo docker run --name airfoil_container -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current
sudo docker cp murtazo airfoil_container:/home/fenics/shared/.
sudo docker exec -t -i airfoil_container /bin/bash
cd murtazo/navier_stokes_solver/src/
chmod +x compile_forms
./compile_forms
cd ..
cmake .
make -j 2
cd ..
cd cloudnaca

#apt-get update
#apt-get install gmsh
#apt install python-numpy


# ARGUMENTS to runme.sh
# angle_start : smallest anglemof attack (degrees)
# angle_stop  : biggest angle of attack (degrees)
# n_angles    : split angle_stop-angle_start into n_angles parts
# n_nodes     : number of nodes on one side of airfoil
# n_levels    : number of refinement steps in meshing 0=no refinement 1=one time 2=two times etc...
chmod +x runme.sh
./runme.sh 0 30 10 200 3
cd msh
dolfin-convert r2a15n200.msh r2a15n200.xml
cd ..
cd ..
cd navier_stokes_solver
./airfoil  10 0.0001 10. 1 ../cloudnaca/msh/r2a15n200.xml

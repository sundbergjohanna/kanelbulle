# Setup file
#!/bin/sh

tar -xvf murtazo.tgz
cd murtazo
tar -xvf cloudnaca.tgz
tar -xvf navier_stokes_solver.tar
cd .. 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo apt-get install -y python-dolfin
sudo apt-get install dolfin-bin
echo "*Image and packages installed."

sudo docker run --name airfoil_container -td -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current
echo "*Docker created: "
sudo docker ps
sudo docker cp murtazo airfoil_container:/home/fenics/shared/.
sudo docker cp second_step.sh airfoil_container:/home/fenics/shared/.
sudo docker exec airfoil_container bash -c "./second_step.sh"
echo "*Executing second script "

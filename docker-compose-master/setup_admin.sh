#!/bin/sh
# Create user:
sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl add_vhost admin
sudo rabbitmqctl set_permissions -p admin admin ".*" ".*" ".*"
sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh /home/ubuntu/kanelbulle/docker-compose-master/docker_comp/flask_app/xmls
sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh /home/ubuntu/kanelbulle/docker-compose-master/docker_comp/murtazo_worker/xmls
sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh /home/ubuntu/kanelbulle/docker-compose-woker/murtazo_worker/xmls

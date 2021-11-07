#!/bin/sh
# Create user:
sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl add_vhost admin
sudo rabbitmqctl set_permissions -p admin admin ".*" ".*" ".*"

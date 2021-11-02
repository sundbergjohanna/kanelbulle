# Airfoil as a Service
The airfoil project is made to work as a cloud service using celery workers, RabbitMQ as the broker, Flask as the application.

<div style="text-align:center"><img src="sys.jpg" alt="workflow" width=45% /></div>

## Starting up VM with CloudInit
For starting upp VM CloudInit is used.
On your own terminal source the file from your cloud provider
```source UPPMAX 2021_1-5-openrc.sh```

Update the `ssc-userdata-instance.py` with your keyfile and flavour of choice. The minimum flavour required for the application to work is `ssc.medium`. Run `python ssc-userdata-instance.py`. Make sure to have your keyfile, `ssc-userdata-instance.py` and `cfg-airfoil.txt` in the same directory. 

## Starting up with Heat
On your own terminal source the file from your cloud provider
```source UPPMAX 2021_1-5-openrc.sh```

Update heat-file `ssc-test-stack.yaml` with your key name and the public part of your key.
Have key-file and the `ssc-test-stack.yaml` in the same folder and run
``` openstack stack create airfoil_stack -f 'yaml' -t ssc-test-stack.yaml```

Please have patience when setting up the VM! This will take time! Both heat and cloudinit installs necessary packages on the VM and deploys a docker with the airfoil application to run the mesh files with below input. If you wish another set of mesh arguments edit this in `second_step.sh` shell script.
`#ARGUMENTS to runme.sh <angle.start> <angle.stop> <no.of.angles> <no.of.nodes> <no.of.refinement.levels>
 #./runme.sh 0 30 10 200 1`
 
Once the set up is finished you need to copy the files from the initial airfoil docker and place them in directory `kanelbulle/this_should_work/docker_comp/murtazo_worker/xml`. This can be achieved by using the following commands when standing in the `kanelbulle`-directory using commands:
``` 
$ sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh this_should_work/docker_comp/murtazo_worker
$ sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh this_should_work/docker_comp/flask_app
```

## Starting application service
Log in to master worker.
Thereafter cd into kanelbulle and run the following commands to move the xml files to the required locations.
```
sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh docker-compose-master/docker_comp/murtazo_worker/xmls
sudo docker cp airfoil_container:home/fenics/shared/murtazo/cloudnaca/msh docker-compose-master/docker_comp/flask_app/xmls
```
Before starting upp docker-compose below to make sure you can access the ports.
```
$ sudo lsof -i tcp:5672
$ sudo kill -9 <pid id>
```

cd into `kanelbulle/docker-compose-master/docker_comp/`

``` sudo docker-compose up```
starts the service

```sudo docker-compose up --scale worker_1=N```
starts the service with N workers




Go into a web browser and run(obs number of files < N number of workes)
`http://<floating-ip>:5000/murtazo/<number of files>`







###TODO LIST INNAN VI ÄR KLARA:
- Heat code
- Om xml redan körts ska den ta gamla resultatet
- Rensa upp lite i githubben
- Skriv instruktioner för hur man startar upp och kör allt
- Rapport: Reusltat
           Metod


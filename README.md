# Airfoil as a Service
The airfoil project is made to work as a cloud service using celery workers, RabbitMQ as the broker, Flask as the application.

<div style="text-align:center"><img src="sys.jpg" alt="workflow" width=45% /></div>

## Starting up VMs
For starting upp VMs CloudInit is used.
On your own terminal source the file from your cloudprovider
`source UPPMAX 2021_1-5-openrc.sh`

Update the `ssc-userdata-instance.py` with your keyfile and flavour of choice. The minimum flavour required for the application to work is `ssc.medium`. Run `python ssc-userdata-instance.py`. Make sure to have your keyfile, `ssc-userdata-instance.py` and `cfg-airfoil.txt` in the same directory. 

Please have patience when setting up the VM! This will take time! The cloud cfg installs necessary packages on the VM and deploys a docker with the airfoil application to run the mesh files with below input. If you wish another set of mesh arguments edit this in `second_step.sh` shell script.
`#ARGUMENTS to runme.sh <angle.start> <angle.stop> <no.of.angles> <no.of.nodes> <no.of.refinement.levels>
 #./runme.sh 0 30 10 200 1`
Once the set up is finished you need to copy the files from the initial airfoil docker and place them in directory `kanelbulle/this_should_work/docker_comp/murtazo_worker/xml`. You can rename the folder `msh` to xml when moving it. 

## Starting application service
Before starting run below to make sure you access the ports.
```
$ sudo lsof -i tcp:5672
$ sudo kill -9 <pid id>
```

cd into `kanelbulle/this_should_work/docker_comp/`



same procedure if you began by enetring. **$docker-compose up --build **
but instead of $docker-compose up -d --build
$docker-compose up -d --build , use.
docker-compose up -d --build --force-recreate


bla bla inline code: `docker-compose up`




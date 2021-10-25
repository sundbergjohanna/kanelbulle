# kanelbulle
Very cool project

Install docker compose:
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo docker–compose --version


$ sudo lsof -i tcp:5672   
$ sudo kill -9 <PID>   
$ docker-compose up -d --build   

same procedure if you began by enetring. 
**$docker-compose up --build **      
but instead of **$docker-compose up -d --build**  
**$docker-compose up -d --build** , use.  
**docker-compose up -d --build --force-recreate**  
  
See, https://stackoverflow.com/questions/59413021/docker-container-fails-because-service-rabbit-failed-programming-external-connec


  
I FLASK NEW innan du kör docker-compose
  $ docker pull quay.io/fenicsproject/stable:current
  

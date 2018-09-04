# install docker
wget -qO- https://get.docker.com/ | sh

# to run a new container
docker run 

# to see running and stopped container
docker 

# to see info about images
docker images

# to pull latest images from docker registry
docker pull image_name

# to pull a particular version of images from docker registry
docker pull image_name:version

# to remove an images
docker rmi image_name:version

# to remove a container 
docker rm container_name

# -d for detached --name name your container -p host_port:container_port
docker run -d --name my_container_name -p 8080:80 image_name

# -it interactive 
docker run -it --name temp ubuntu /bin/bash

# -it interactive to already running docker
# exec run a command in already running container
docker exec -it docker_name command_to_run

# exiting docker container without stopping it
ctrl P+Q

# remove all container : -q for quiet, returns only id
docker stop $(docker ps -aq)

# copy from host
docker cp /host/file/path container_name:/container/file/path

# docker execute command in container
docker exec -it container_name /bin/bash

# make image from existing container
docker commit  existing_container_name new_image_name

# run docker image with auto start
docker run -dit --restart unless-stopped --name container_name -p host_port:container_port image_name command-to-run

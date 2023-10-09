# phishing

#Lancer l'infrastructure:
cd phishing
sudo docker-compose up -d( lancement du conteneur infesté qui contient docker)
sudo docker  exec -ti phishing-docker-1 /bin/ash
docker-compose up -d(lancement de 4 conteneur)

#Lancer l'attaque:
docker exec -ti phishing-ansible-1 bash
ansible-playbook *


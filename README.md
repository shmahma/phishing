#################### Phishing ####################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
################ Lancer l'infrastructure #########################################################################
##################################################################################################################
##################################################################################################################
################ A partir de git hub #############################################################################
##################################################################################################################
cd phishing
sudo docker-compose up -d( lancement du conteneur infesté qui contient docker)
sudo docker  exec -ti phishing-docker-1 /bin/ash
docker-compose up -d(lancement de 4 conteneur)
##################################################################################################################
################ A partir de docker hub ##########################################################################
##################################################################################################################
sudo docker pull shmahma/phishing:v1
sudo docker run -d --privileged --name dockerphish -p 80:80 -v /var/mysql/:/root/mysql shmahma/phishing:v1
sudo docker exec -ti dockerphish /bin/ash
docker-compose up -d(lancement de 4 conteneur)
##################################################################################################################
##################################################################################################################
################### Lancer l'attaque #############################################################################
##################################################################################################################
##################################################################################################################
docker exec -ti phishing-ansible-1 bash
ansible-playbook *
Check les mails.
##################################################################################################################
##################################################################################################################

# phishing
cd phishing
sudo docker-compose up(lancement du conteneur infesté qui contient docker)
sudo docker ps
sudo docker exec -ti <id conteneur infesté> /bin/ash
docker-compose up(lancement de 3 conteneur site web,serveur mail(envoie des mail),mysql)
docker ps
docker exec -ti <id serveur mail> /bin/sh
python3 email_sender.py(on envoit les mails aux adresses mails presents dans la base)
exit
docker exec -ti <id website> /bin/sh
python3 view.py(on lance notre site sur localhost(à changer apres))
clique sur le lien d'email envoyé sur gmail.

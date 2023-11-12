Tests Automatisés de DDoS avec Docker Swarm et Ansible
Ce dépôt contient les codes et configurations nécessaires pour mettre en place un environnement de test automatisé de DDoS (Distributed Denial of Service) en utilisant Docker Swarm et Ansible.
Vue d'Ensemble
Ce projet automatise le déploiement d'un environnement de test de DDoS. Il utilise Docker Swarm pour l'orchestration des conteneurs et Ansible pour exécuter le script de DDoS contre une cible spécifiée.
Composants

    Playbook Ansible (ddos.yml) : Définit les tâches pour exécuter le script Python de DDoS.
    Dockerfile pour Ansible (Dockerfile_ansible) : Construit une image Docker avec Ansible installé.
    Configuration Ansible (ansible.cfg) : Fichier de configuration pour Ansible.
    Fichier Hosts (hosts) : Fichier d'inventaire pour Ansible, listant les nœuds de Docker Swarm.
    Dockerfile pour l'Application (Dockerfile_app) : Construit une image Docker pour exécuter le script de DDoS.
    Script DDoS (ddos.py) : Script Python pour envoyer des requêtes HTTP à une URL cible.
    Script Automatisé (autoddos.sh) : Script Bash pour configurer Docker Swarm, déployer des services et exécuter le playbook Ansible.
    Fichier Docker Compose (docker-compose.yml) : Définit les services pour le contrôleur Ansible et les agents de DDoS.

Prérequis

    Docker et Docker Swarm installés et configurés.
    Ansible installé sur la machine hôte.

Configuration et Déploiement

    Construire les Images Docker :
        Pour Ansible : docker build -f Dockerfile_ansible -t votrenomutilisateur/ansible:ddos .
        Pour l'application DDoS : docker build -f Dockerfile_app -t votrenomutilisateur/ddos:ddos .

    Initialiser Docker Swarm (si pas déjà fait) :
        docker swarm init

    Exécuter le Script d'Automatisation :
        chmod +x autoddos.sh
        ./autoddos.sh [NOMBRE_MANAGERS] [NOMBRE_TRAVAILLEURS] [NOMBRE_DE_REQUETES] [URL_CIBLE]

Utilisation

    Pour visualiser le Docker Swarm, naviguez vers http://localhost:8080.
    Pour exécuter manuellement le playbook Ansible dans le conteneur Ansible, utilisez la commande suivante :
docker exec -ti [NOM_DU_CONTENEUR] sh -c 'ansible-playbook ddos.yml --extra-vars "nb_r

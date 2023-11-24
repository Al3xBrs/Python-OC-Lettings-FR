## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

- Le déploiement est configuré de sorte qu'une image **Docker** est générée et déployée sur **Render** à chaque commit
sur la branche **master** que lorsque les tests sont validés sur **circleci**.

- Pour que le déploiement se déroule sans accroc, les tests doivent couvrir 80% du code et générer 
une image **Docker** compatible avec le déploiement sur **Render**.

- Il est également important de renseigner les variables d'environnement sur les différents sites.


#### Déploiement manuel

- Requirements : `pip install docker`
- Pour un déploiement manuel, assurez vous de couvrir au moins 80% du code avec des tests en utilisant 
pytest --cov par exemple.

- Lancer la création de l'image Docker `docker build -t [nom-user-dockerhub]/[nom-de-l'img]:[tag] .`
*Le fait de renseigner le nom de l'user DockerHub permettra un push plus simple sur DockerHub.*
- Pour vous aider à maitriser la conteneurisation des images Docker, vous pouvez utiliser **Docker Desktop** 
disponible ici : https://www.docker.com/products/docker-desktop/. Docker Desktop possède une interface
graphique user friendly pour comprendre le déroulement de ces opérations.

- Faire tourner l'image Docker créée à l'instant : `docker run [nom-user-dockerhub]/[nom-de-l'img]:[tag]`

- Pour push l'image sur DockerHub : `docker push [nom-user-dockerhub]/[nom-de-l'img]:[tag]`




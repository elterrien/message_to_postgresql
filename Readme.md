# Exemple de copie de messages RabbitMQ vers une base de données PostgreSQL avec Python

Exemple simple d'enregistrement de données provenant de messages RabbitMQ dans une base de données PostgreSQL.

1. Un publisher se charge d'envoyer des messages dans une queue RabbitMQ `publisher.py`. 
2. Un consummer se charge de lire les messages de la queue et de les enregistrer dans une base de données PostgreSQL `consumer.py`.

**Publisher -> RabbitMQ <- Consumer -> PostgreSQL**

## Installation

L'exemple s'appuie sur la librairie `pika` pour communiquer RabbitMQ et `psycopg2` pour intéragir avec PostgreSQL.

Le fichier `requirements.txt` contient les packages Python nécessaires à l'exécution de l'exemple.

Le fichier `docker-compose.yml` permet de lancer RabbitMQ et PostgreSQL dans des conteneurs Docker. 
Il est préconfiguré pour que les conteneurs soient sur le même réseau et que le consumer puisse accéder à la base de données.

### Packages Python

```bash
pip install -r requirements.txt
```

### Lancement des conteneurs Docker

```bash
docker-compose up -d
```

## Utilisation

Pour commencer à envoyer des messages dans la queue RabbitMQ, il faut que les conteneurs Docker soient lancés. Ensuite, il suffit de lancer le script `publisher.py` :

```bash
python publisher.py
```

Pour finir, il faut lancer le script `consumer.py` :

```bash
python consumer.py
```

Le script `consumer.py` va lire les messages de la queue RabbitMQ et les enregistrer dans la base de données PostgreSQL.
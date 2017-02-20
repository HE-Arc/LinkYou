# LinkYou

# Concept

L'idée c'est de créer une plateforme sur laquelle on peut s'authentifier. Cette plateforme contiendrait des collections de liens qui
pourraient être partagés, en interne et en externe (par exemple sur Facebook). La collection peut être représentée par un nom, une image
et une description.
Le framework Django sera utilisé pour développer ce projet.

# Objectifs

## Primaires

* Création de compte et connexion
* Permettre la création de collections de liens
* Partage
* Pouvoir épingler une collection qui a été partagée

## Secondaires

* Pour chaque lien, récupérer le favicon et/ou un screenchot de la page du lien. Eventuellement, un texte de remplacement pour le lien.
* Organisation des liens dans une collection.
* Avoir une collection de base contenant les liens vers les réseaux sociaux les plus communs (Facebook, Twitter, Google,... )
* Pouvoir liker une collection
* Avoir des collections collaboratives (plusieurs personnes peuvent la modifier)
* Suggérer des liens en fonction du titre de la collection
* Avoir une black-list de liens


# Setup

Créer un utilisateur et une base de données postgre

```
>> sudo su - postgres
>> psql

>> CREATE DATABASE linkyou;
>> CREATE USER myprojectuser WITH PASSWORD 'password';

>> ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
>> ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
>> ALTER ROLE myprojectuser SET timezone TO 'UTC';

>> GRANT ALL PRIVILEGES ON DATABASE linkyou TO myprojectuser;
```

Configurer les variables d'environnement

```
# ~/.bashrc

export LINKYOU_SECRET_KEY="YOUR_KEY"
export LINKYOU_DEBUG=True
export LINKYOU_DB_NAME="snapventure"
export LINKYOU_DB_USER="root"
export LINKYOU_DB_PASSWORD="1234"
export LINKYOU_DB_HOST="localhost"

```

It's ok now

#Maquette

Page principale :
![](https://github.com/HE-Arc/LinkYou/blob/master/docs/2017-02-20%2013.06.56.jpg)

Page d'une collection de liens :
![](https://github.com/HE-Arc/LinkYou/blob/master/docs/2017-02-20%2013.06.43.jpg)

#Schéma de la base de données

![](https://github.com/HE-Arc/LinkYou/blob/master/docs/BDD_Linkyou.png)

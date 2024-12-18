# Plateforme d'Intégration Communautaire

## Description
Une application Flask pour faciliter l'intégration des immigrants haïtiens à l'étranger, en utilisant des fonctionnalités comme la recherche géolocalisée et les avis communautaires.

## Prérequis
- Python 3.10 ou version ultérieure
- Docker et Docker Compose

## Installation Locale
1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre_profil/plateforme_integration.git
   cd plateforme_integration
   ```

2. Construisez et démarrez les services :
   ```
   docker-compose up --build
   ```

3. Accédez à l'application :
   - http://localhost:5000

## Déploiement sur AWS
1. Clonez ce projet sur votre serveur EC2 AWS :
   ```
   git clone https://github.com/votre_profil/plateforme_integration.git
   cd plateforme_integration
   ```

2. Installez Docker sur l'instance EC2.

3. Lancez l'application :
   ```
   docker-compose up --build -d
   ```

4. Configurez un Load Balancer AWS pour acheminer le trafic.

## Crédits
- Inspiré de Material Kit React
- Backend : Flask
- Base de Données : PostgreSQL
- Conteneurs : Docker
# Image de base
FROM python:3.10

# Répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY ../app /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour Flask
EXPOSE 5000

# Démarrer l'application Flask
CMD ["python", "app.py"]
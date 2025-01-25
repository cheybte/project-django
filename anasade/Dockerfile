# Utiliser une image Python officielle comme base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires pour mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'application
COPY . /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port que l'application utilise
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:23086"]

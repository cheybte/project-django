# Utilisez l'image Python slim comme base
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système requises
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers du projet
COPY . /app/

# Exposer le port 8000 pour le serveur
EXPOSE 8000

# Commande par défaut pour exécuter le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

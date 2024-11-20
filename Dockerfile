FROM python:3

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier le script et les dépendances
COPY app.py requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour exécuter le programme
CMD ["python", "app.py"]

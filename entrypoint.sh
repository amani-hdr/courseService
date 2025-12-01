#!/bin/bash
# entrypoint.sh

# Exécute les migrations avant de démarrer l'application
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collecte des fichiers statiques (si ce n'est pas fait dans le build)
# C'est souvent mieux de le laisser ici pour être sûr.
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Lancer le serveur Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn mini_projet_idl.wsgi:application

#!/bin/sh

echo "production started...."
python manage.py makemigrations --settings=core.settings.production
python manage.py migrate --settings=core.settings.production
python manage.py collectstatic --settings=core.settings.production --no-input --clear
python manage.py update_index --settings=core.settings.production
gunicorn core.wsgi:application -b :8000  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG
exec "$@"
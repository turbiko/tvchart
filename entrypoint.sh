#!/bin/sh

python manage.py makemigrations --settings=core.settings.dev
python manage.py migrate --settings=core.settings.dev
python manage.py collectstatic --settings=core.settings.dev --no-input --clear
#python manage.py update_index --settings=core.settings.dev
gunicorn core.wsgi:application -b :8000  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG
exec "$@"
#!/bin/sh
python manage.py makemigrations

python manage.py migrate

python manage.py loaddata */fixtures/*.json

python manage.py collectstatic --noinput

cp -r collected_static/. /backend_static/static/

gunicorn -b 0.0.0.0:8000 ecom.wsgi

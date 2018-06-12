#!/bin/bash
echo "Create password"
randpw(){ < /dev/urandom tr -dc '+^_|=12345!/@\-&#$%qwertQW*ERTasdfgASDFGzxcvbZXCVB' | head -c64;echo; }
var=$(randpw)
echo "DJANGO_PASSWORD='$var'" > contact/credentials.py
echo "Delete old database and migrations..."
rm db.sqlite3
rm -rf webapp/migrations
rm -rf webapp/__pycache__
rm -rf _autofixture
echo "Database changes"
source virtualenv/bin/activate
./manage.py makemigrations webapp
./manage.py migrate
echo "Create superuser"
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '12345678a')"
echo "Create plot ER"
./manage.py graph_models webapp -g -o doc-img/ER.png
echo "Autofixture"
./manage.py loadtestdata webapp.Contact:2
echo "Start"
./manage.py runserver 0.0.0.0:8000

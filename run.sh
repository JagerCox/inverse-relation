#!/bin/bash
echo "Activate enviorement"
source virtualenv/bin/activate
echo "Database changes"
./manage.py makemigrations webapp
./manage.py migrate
echo "Create plot ER"
./manage.py graph_models webapp -g -o ER.png
echo "Start"
./manage.py runserver 0.0.0.0:8000

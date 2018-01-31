#!/bin/bash
echo " ========================== "
echo "|  Running on production   |"
echo " ========================== "
echo "| Remember to use          |"
echo "| CollectStatics and       |"
echo "| change the path in your  |"
echo "| settings_production.py   |"
echo "| to load the static files |"
echo " ========================== "
echo ""
echo "Activate enviorement"
source virtualenv/bin/activate
echo "Database changes"
./manage.py makemigrations webapp
./manage.py migrate
echo "Start"
./manage.py runserver 0.0.0.0:8000 --settings=contact.settings_production
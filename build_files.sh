#!/usr/bin/env bash

echo "Building project packages----"
python -m pip -r requirements.txt

# echo "Migrating Database...."
# python3.9 manage.py makemigrations 
# python3.9 manage.py migrate 

echo "Collecting static files...."
python manage.py collectstatic 




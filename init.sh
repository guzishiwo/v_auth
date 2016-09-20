#!/bin/bash
python manage.py migrate
sleep 2

python manage.py runserver 0.0.0.0:80

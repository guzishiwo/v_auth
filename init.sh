#!/bin/bash
python manage.py migrate
sleep 2
echo "from django.contrib.auth.models import User; User.objects.create_superuser('Vwms', 'admin@example.com', 'vwms')" | python manage.py shell

python manage.py runserver 0.0.0.0:80

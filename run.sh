#!/bin/bash
SERVER_PORT=8080;
echo port is $SERVER_PORT
echo "make migrations"
python3 today_topic/manage.py makemigrations
echo "migrate"
python3 today_topic/manage.py migrate
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.io', 'password')" | python3 manage.py shell
echo "from django.contrib.auth.models import User; user=User.objects.create_user('junyoung', password='chl010177'); user.is_superuser=True;user.is_staff=True;user.save()" | python3 today_topic/manage.py shell
echo [$0] Starting Django Server…
python3 today_topic/manage.py runserver 0.0.0.0:$SERVER_PORT

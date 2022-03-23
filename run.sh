#!/usr/bin/bash
echo "django project starting"
cd venv/bin
. activate
cd ../..
cd questionnaire
python manage.py runserver


$SHELL

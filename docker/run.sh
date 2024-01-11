#!/bin/bash

python /notification_service/docker/wait_for_postgres.py

python manage.py migrate

python manage.py loaddata notification/message_status_reference.json
python manage.py loaddata notification/tag_reference.json
python manage.py loaddata notification/mobile_operator_code_reference.json

python manage.py runserver 0.0.0.0:8000
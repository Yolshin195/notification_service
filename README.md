# Notification service

## Load data
```commandline
python manage.py loaddata notification/message_status_reference.json
python manage.py loaddata notification/tag_reference.json
python manage.py loaddata notification/mobile_operator_code_reference.json
```

## docker compose
```commandline
docker-compose build
docker-compose up -d
```

## open terminal Django
```commandline
docker exec -it notification_service bash
```

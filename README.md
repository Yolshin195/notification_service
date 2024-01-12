# Notification service
[Link to task](https://vans-tan-09u.craft.me/n6OVYFVUpq0o6L)

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

## Рассылка сообщений
1. Пользователь создаёт сущность Dispatch
2. Срабатывает django сигнал, который запускает celery задачу
3. Celery задача создаёт сообщения для каждого пользователя который попал под фильтр
4. Создаём задачу для каждого сообщения на отправку
5. В момент отправки проверяем, что время на отправку ещё не закончилось
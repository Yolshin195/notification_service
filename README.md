# Notification service

[Link to task (ru)](https://vans-tan-09u.craft.me/n6OVYFVUpq0o6L),
[Русский](docs/ru/README.md)

## ToDo

### Client entity

- [X] GET: View created clients
- [X] POST: Adding a new client with all of its attributes
- [X] PUT: Client attribute updates
- [X] DELETE: Delete a client

### Dispatch entity

- [X] GET: View created mailings
- [X] POST: Adding a new newsletter
- [X] PUT: Mailing attribute updates
- [X] DELETE: Delete a mailing
- [X] Processing active mailings and sending messages to clients

### Report

- [X] GET: Getting overall statistics on created mailings and the number of messages sent, grouped by their statuses
- [X] GET: Obtaining detailed statistics of sent messages for a specific mailing

### Additional tasks

- [X] 3\. Prepare a docker-compose file to launch all project services with a single command.
- [X] 5\. Configure it so that the Swagger UI page opens at the /docs/ address, displaying the documentation for the developed API.

## Load data

```commandline
python manage.py loaddata notification/message_status_reference.json
python manage.py loaddata notification/tag_reference.json
python manage.py loaddata notification/mobile_operator_code_reference.json
```

## Docker compose

```commandline
docker-compose build
docker-compose up -d
docker-compose run web python manage.py createsuperuser
```

## Open terminal Django

```commandline
docker exec -it notification_service bash
```

## ToDo
- [ ] Readme сделать на Русском
- [ ] Удалить: Load data
- [ ] Настроить logger в папка docker
- [ ] Написать тесты
- [ ] Посмотреть как правильно регистрировать signal def ready(self): import notification.signals
- [ ] flake8 - настроить
- [ ] Распилить api
- [ ] генерация id
- [ ] Сделать пометку, что время нужно указывать в UTC
- [ ] Рассылка добавить поле Timezone
# Notification service

[Link to task (ru)](https://vans-tan-09u.craft.me/n6OVYFVUpq0o6L),
[Русский](docs/ru/README.md)

## ToDo

### Client entity

- [X] GET: View created clients
- [X] POST: Adding a new client with all of its attributes
- [ ] PUT: Client attribute updates
- [ ] DELETE: Delete a client

### Dispatch entity

- [X] GET: View created mailings
- [X] POST: Adding a new newsletter
- [ ] PUT: Mailing attribute updates
- [ ] DELETE: Delete a mailing
- [ ] Processing active mailings and sending messages to clients

### Report

- [ ] GET: Getting overall statistics on created mailings and the number of messages sent, grouped by their statuses
- [ ] GET: Obtaining detailed statistics of sent messages for a specific mailing

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
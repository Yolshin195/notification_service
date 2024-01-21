# Notification service
Read this in other languages: [Русский](docs/ru/README.md)

## Task

It is necessary to develop a service for managing API administration and receiving statistics for mailings.
[Link to this task](https://vans-tan-09u.craft.me/n6OVYFVUpq0o6L).

### Description

- Implement methods for creating a new mailing, viewing created ones, and obtaining statistics for completed mailings.
- Implement the notification sending service to an external API.
- Optionally, you can choose any number of additional points described after the main ones.

## Documentation

- [How to run the project?](docs/en/run_app.md)

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

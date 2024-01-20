# Сервис уведомлений

[Link to task (ru)](https://vans-tan-09u.craft.me/n6OVYFVUpq0o6L),
[English](https://github.com/Yolshin195/notification_service)

## Сделать

### Таблица клиента (Client)

- [X] GET: Получение информации о клиенте
- [X] POST: Добавления нового клиента в справочник со всеми его атрибутами
- [ ] PUT: Обновления данных атрибутов клиента
- [ ] DELETE: Удаления клиента из справочника

### Таблица рассылок (Dispatch)

- [X] GET: Получение информации о рассылках
- [X] POST: Добавления новой рассылки со всеми её атрибутами
- [ ] PUT: Обновления атрибутов рассылки
- [ ] DELETE: Удаления рассылки
- [ ] Обработки активных рассылок и отправки сообщений клиентам

### Отчётность

- [ ] GET: Получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам
- [ ] GET: Получения детальной статистики отправленных сообщений по конкретной рассылке

## Инициализация справочников

```commandline
python manage.py loaddata notification/message_status_reference.json
python manage.py loaddata notification/tag_reference.json
python manage.py loaddata notification/mobile_operator_code_reference.json
```

## Запуск приложения

```commandline
docker-compose build
docker-compose up -d
docker-compose run web python manage.py createsuperuser
```

## Подключится к контейнеру

```commandline
docker exec -it notification_service bash
```
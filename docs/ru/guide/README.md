# Документация по API для интеграции с разработанным сервисом

Доступные адреса
```json
{
    "dispatch-reports": "http://localhost:8000/api/v1/dispatch-reports/",
    "clients": "http://localhost:8000/api/v1/clients/",
    "dispatches": "http://localhost:8000/api/v1/dispatches/",
    "messages": "http://localhost:8000/api/v1/messages/",
    "mobile-operator-codes": "http://localhost:8000/api/v1/mobile-operator-codes/",
    "message-statuses": "http://localhost:8000/api/v1/message-statuses/",
    "tags": "http://localhost:8000/api/v1/tags/"
}
```

## Инструкции
- Создание новой рассылки: [http://localhost:8000/api/v1/dispatches/](create_dispatches.md)
- Получение статистики по созданным рассылкам и количеству отправленных: [http://localhost:8000/api/v1/dispatch-reports/](get_despatches_report.md)
- Swagger: [http://localhost:8000/docs/](http://localhost:8000/docs/)
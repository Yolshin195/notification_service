# Запуск проекта с использованием Docker Compose

Данный проект использует Docker Compose для управления зависимостями и конфигурациями. Прежде чем начать, убедитесь, что
на вашем компьютере установлен Docker и Docker Compose.

Версия python: 3.12.1

## Шаги по установке

1. **Установите Docker:**

   Скачайте и установите Docker, следуя инструкциям на [официальном сайте Docker](https://docs.docker.com/get-docker/).

2. **Установите Docker Compose:**

   Установите Docker Compose, следуя инструкциям
   на [официальном сайте Docker Compose](https://docs.docker.com/compose/install/).

## Запуск проекта

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/Yolshin195/notification_service
   cd notification_service
   ```

2. **Настройте переменные окружения:**

   В корне проекта создайте файл `.env` и укажите необходимые переменные окружения. Пример:

   ```env
   MESSAGE_SENDER_API_TOKEN=Your token for api
   MESSAGE_SENDER_API_PATH=Your path for api
   SECRET_KEY=Your secret key for Django
   
   DB_HOST=db
   DB_PORT=5435
   ```

3. **Запустите проект:**

   ```bash
   docker-compose up -d
   ```

   Эта команда запустит все службы, указанные в файле `docker-compose.yml`, в фоновом режиме.

4. **Проверьте работоспособность:**

   Откройте ваш веб-браузер и перейдите по адресу [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/), где `порт` - это порт
   вашего веб-приложения.

## Остановка проекта

Для остановки проекта выполните:

```bash
docker-compose down
```

Это завершит работу всех контейнеров и освободит ресурсы.

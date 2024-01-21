# Running the Project with Docker Compose

This project utilizes Docker Compose for managing dependencies and configurations. Before getting started, make sure Docker and Docker Compose are installed on your machine.

## Installation Steps

1. **Install Docker:**

   Download and install Docker by following the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

2. **Install Docker Compose:**

   Install Docker Compose by following the instructions on the [official Docker Compose website](https://docs.docker.com/compose/install/).

## Running the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Yolshin195/notification_service
   cd notification_service
   ```

2. **Set Environment Variables:**

   Create a `.env` file in the project root and specify the required environment variables. Example:

   ```env
    MESSAGE_SENDER_API_TOKEN=Your token for api
    MESSAGE_SENDER_API_PATH=Your path for api
    SECRET_KEY=Your secret key for Django
    
    DB_HOST=db
    DB_PORT=5435
   ```

3. **Launch the Project:**

   ```bash
   docker-compose up -d
   ```

   This command will start all the services defined in the `docker-compose.yml` file in the background.

4. **Check the Functionality:**

   Open your web browser and go to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/), where `port` is the port of your web application.

## Stopping the Project

To stop the project, execute:

```bash
docker-compose down
```

This will stop all containers and free up resources.

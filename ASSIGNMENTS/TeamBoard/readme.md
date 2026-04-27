# TeamBoard Backend

Django backend with PostgreSQL using Docker. Includes KBEntry module and seed data.

## Prerequisites

- Python 3.10+ (only if running without Docker)
- Docker & Docker Compose installed
- Git

## Clone Project

```bash
git clone <repo-url>
cd <project-folder>
```

## Run with Docker (Recommended)

Start everything:

```bash
docker-compose down -v
docker-compose up --build
```

This will start:
- Django → http://localhost:8000
- PostgreSQL → localhost:5434

## Database Configuration

Already handled inside Docker.

For pgAdmin connection:

- Host: localhost  
- Port: 5434  
- User: postgres  
- Password: postgres  
- Database: teamboard  

## Apply Migrations

Run inside container:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## Create Superuser (optional)

```bash
docker-compose exec web python manage.py createsuperuser
```

## Seed Knowledge Base

```bash
docker-compose exec web python manage.py seed_kb
```

This will insert sample KB entries into the database.

## Run Commands (General)

```bash
docker-compose exec web python manage.py <command>
```

Example:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Common Issues

### DB not connecting
- Make sure containers are running:
```bash
docker ps
```

### Reset database

```bash
docker-compose down -v
docker-compose up --build
```

### psycopg2 error
Add this in `requirements.txt`:

```
psycopg2-binary
```

Rebuild:

```bash
docker-compose up --build
```

## Important Notes

- Inside Docker → DB host = `db`, port = `5432`
- Outside Docker → use `localhost:5434`
- DB credentials are set in `docker-compose.yml`
- If you change DB credentials → reset volumes

## Project Structure

```
project/
│── api/
│   ├── models.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_kb.py
│
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── manage.py
```

## Done

You can now access the backend at:

http://localhost:8000

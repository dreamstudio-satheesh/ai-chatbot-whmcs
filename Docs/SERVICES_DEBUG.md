# Checking the Status of FastAPI, PostgreSQL, and Other Services in Docker Compose

When running services with Docker Compose, it's essential to monitor their status to ensure everything is working correctly. Below are various ways to check the status of FastAPI, PostgreSQL, and other services.

## 1. List Running Containers
To see all active containers:
```sh
docker ps
```
This command will display running containers, their status, and port mappings.

## 2. Check Logs for FastAPI
To view logs from the FastAPI service:
```sh
docker logs ai-chatbot --follow
```
This will stream logs in real-time, helping to debug issues.

## 3. Check Logs for PostgreSQL
To monitor PostgreSQL logs:
```sh
docker logs ai-chatbot-db --follow
```
This helps verify if the database is running properly.

## 4. Verify FastAPI is Running
Run the following command to check if FastAPI is responding:
```sh
curl http://localhost:8000/docs
```
If FastAPI is active, it should return the interactive API documentation.

Alternatively:
```sh
curl -I http://localhost:8000
```
A successful response indicates the service is running.

## 5. Check Docker Compose Service Status
To see the status of all services:
```sh
docker compose ps
```
This will show running states and assigned ports.

## 6. Check Database Connection
To manually verify the PostgreSQL database:
```sh
docker exec -it ai-chatbot-db psql -U your_db_user -d your_db_name
```
Inside PostgreSQL, run:
```sql
SELECT * FROM pg_database;
```
This confirms database connectivity.

## 7. Restart Services
If a service is down, restart it with:
```sh
docker compose restart ai-chatbot
```
For a complete restart:
```sh
docker compose down
```
```sh
docker compose up -d
```

## 8. Check Network Bindings
To verify ports are correctly exposed:
```sh
docker inspect ai-chatbot | grep -i '"IPAddress"'
```
or
```sh
netstat -tulpn | grep LISTEN
```
This ensures FastAPI and PostgreSQL are reachable.

## Summary
| Command | Purpose |
|---------|---------|
| `docker ps` | List running containers |
| `docker compose ps` | Check status of all services |
| `docker logs ai-chatbot --follow` | View FastAPI logs |
| `docker logs ai-chatbot-db --follow` | View PostgreSQL logs |
| `curl http://localhost:8000` | Check if FastAPI is responding |
| `docker exec -it ai-chatbot-db psql -U your_db_user -d your_db_name` | Connect to PostgreSQL |
| `docker compose restart ai-chatbot` | Restart FastAPI |

These commands will help you monitor and debug your Docker Compose services efficiently. 🚀


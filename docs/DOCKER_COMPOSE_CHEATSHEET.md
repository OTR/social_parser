# Check Existing Containers

```bash
docker ps -a
```

# Remove the Existing Container

```bash
docker rm -f django_local_social_parser
```
# Rebuild and restart the Containers

```bash
docker-compose down
docker-compose up --build
```

#  Remove a Specific Stopped Container

```bash
docker rm <container_id>
```

# Restart a Stopped Container 

```bash
docker start <container_id>
```

# Remove Containers with docker-compose

If your containers were started with docker-compose, use the following commands to stop and remove them:

```bash
docker-compose down
```

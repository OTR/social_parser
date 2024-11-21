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

# Show Container Logs

## Show Logs for a Specific Container

docker logs <container_name_or_id>

##  Follow Live Logs (Real-Time)

docker logs -f <container_name_or_id>

## Show Specific Number of Log Lines

docker logs --tail 50 django_remote_social_parser

## Include Timestamps

docker logs --timestamps <container_name_or_id>


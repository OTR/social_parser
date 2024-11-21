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

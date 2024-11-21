# Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

# Add Your User to the Docker Group 

```bash
sudo usermod -aG docker $USER
```

# Install Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

# Rootless Docker

To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.


To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the 'Docker daemon attack surface'
         documentation for details: https://docs.docker.com/go/attack-surface/


# Verify Installation:

```bash
docker --version
docker-compose --version
```

# Clone your repository:

```bash
git clone git@github.com:OTR/social_parser.git
```

# Troubleshooting

## Add correct host key in /root/.ssh/known_hosts to get rid of this message.

### Remove the Old Host Key

```bash
ssh-keygen -f "/root/.ssh/known_hosts" -R "github.com"
```

### Fetch the Updated Host Key

```bash
ssh-keyscan github.com >> /root/.ssh/known_hosts
```

### Test the SSH Connection

```bash
ssh -T git@github.com
```
### Check If an SSH Key Is Present

```bash
ls -l ~/.ssh/id_*
```

### Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Ensure the SSH agent is running:

```bash
eval "$(ssh-agent -s)"
```

### Add the new SSH key to the ssh-agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

# Check the SSH Server Configuration

```bash
sudo nano /etc/ssh/sshd_config
```

----

# failed to bind port 0.0.0.0:80/tcp

Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use

 Identify the Process Using Port 80

```bash
sudo lsof -i :80
```

# Use a Reverse Proxy

## Configure Nginx: Edit your Nginx configuration

`/etc/nginx/sites-available/default`

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:8000;  # Forward to your container's exposed port
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

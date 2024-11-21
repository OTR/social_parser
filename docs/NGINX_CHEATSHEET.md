# Nginx Configuration for static files

`/etc/nginx/sites-available/social_parser`

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /var/www/social_parser/static/;
    }
}
```

# Activate the configuration:

```bash
sudo ln -s /etc/nginx/sites-available/social_parser /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```


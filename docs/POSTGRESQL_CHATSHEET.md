# Install PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib -y
```

#  Start and enable PostgreSQL

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

# Login as PostgreSQL user to create a database and user:

```bash
sudo -i -u postgres
```

# Access the PostgreSQL shell:

```bash
psql
```

# Create a new database

```sql
CREATE DATABASE social_parser;
```

# Create a new user with a password:

```sql
CREATE USER application WITH PASSWORD 'secure_password';
```
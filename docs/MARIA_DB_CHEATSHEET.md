#  Update the MariaDB Repository

## Remove the existing repository

```bash
sudo rm /etc/apt/sources.list.d/mariadb*
```

## Re-add the repository using the official MariaDB script:

```bash
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
sudo apt-get update
```
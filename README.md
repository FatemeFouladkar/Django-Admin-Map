# Django-Admin-Map

This repository contains the source code for [Add Interactive Map to Django Admin](https://medium.com/@fatemefuoladkar/add-interactive-map-to-django-admin-9278ddab950f) Tutorial on Medium. 

## How to run the project 

Open the terminal (cmd, powershell, git bash, ...) and:

#### Clone the repository
```
git clone git@github.com:FatemeFouladkar/Django-Admin-Map.git
```

#### Build and run the docker container
``` 
docker-compose up --build
```

#### Make migrations
``` 
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

```

# quality-test

- [Test](https://simba-latam.notion.site/Desarrollador-Full-Stack-d5d80e82bf194abc8adebdd63cf920bd)

## Stack

- asgiref==3.4.1
- backports.zoneinfo==0.2.1
- black==22.8.0
- click==8.0.4
- dataclasses==0.8
- dj-database-url==2.2.0
- Django==3.2.25
- django-cors-headers==3.10.1
- django-environ==0.11.2
- django-rest-framework==0.1.0
- djangorestframework==3.15.1
- djangorestframework-simplejwt==4.4.0
- importlib-metadata==4.8.3
- importlib-resources==5.4.0
- mypy-extensions==1.0.0
- pathspec==0.9.0
- platformdirs==2.4.0
- psycopg2==2.9.8
- psycopg2-binary==2.9.8
- PyJWT==2.4.0
- python-decouple==3.8
- pytz==2024.1
- sqlparse==0.4.4
- tomli==1.2.3
- typed-ast==1.5.5
- typing-extensions==4.1.1
- zipp==3.6.0
- python==Python 3.6.5

## Create enviroment
- python -m venv technicalTestQuality
- source technicalTestQuality/bin/activate

### Create Data Base (example)

```bash
# Server in  http://localhost:3000
# sudo -u postgres psql
$ postgres=# CREATE USER william_user_quality WITH PASSWORD '123456';
$ postgres=# CREATE DATABASE quality;
$ postgres=# GRANT ALL PRIVILEGES ON DATABASE quality TO william_user_quality;
$ postgres=# ALTER USER william_user_quality CREATEDB;
# In case you don't load the database you may need to export the variable in the terminal
$ export DATABASE_URL=postgres://william_user_quality:123456@localhost:5432/quality
```


### Clone repo

```bash
# Clone repo (ssh)
$ git clone git@github.com:WilliamPerezBeltran/quality.git

# Clone repo (http)
$ git clone https://github.com/WilliamPerezBeltran/quality.git

# Go to app directory
$ cd quality


# Install depedencies
$ pip install -r requirements.txt
```
## Installation
- pip install -r requirements.txt

### Run app

```bash
# Server in  http://localhost:3000
$ cd quality
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Basic use

```bash
# Server in  http://localhost:3000
$ cd quality
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## What's included

```
.
├── inventory
│   ├── admin.py
│   ├── apps.py
│   ├── auth_views.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── auth_views.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── serializers.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── inventory_api
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pyproject.toml
├── README.md
└── requirements.txt


```

### Data base


```bash
```

### Secuence for service


## Creator

**William Pérez**
- [William Pérez github](https://github.com/WilliamPerezBeltran)

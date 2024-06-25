# CreditService

How to run:

1. goto: app directory,
2. Run: python3 manage.py runserver,
3. goto: web: "https://localhost:8000/Authenticator/api/register-user"
4. register user,
5. login with the registered email-id, and password,
6. Welcome page follows.

Relevant Commands on bash:

Installation Commands:
```shell

pip3 install djangorestframework
  or
python3 -m pip install djangorestframework

pip3 install django-admin
```

Running the application:
```shell
cd app/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py flush
python3 manage.py runserver
```

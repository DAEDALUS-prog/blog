It is blog. Here used language PYTHON and framework DJANGO.
========================
USE   
(YOU MUST HAVE A PYTHON BEFORE STARTING v==3.9 AND DJANGO v==3.2.5)

`pip install Django==3.2.5`

---
> You have to come up with your secret key or generate it here *https://djecrety.ir/*
> 
![1](https://user-images.githubusercontent.com/69119928/129967857-5619c38f-bdf2-42a0-a745-fc4792c808ac.jpg)
---
> Postgres database used here
> Instead db_name, db_user, db_password - you must enter your details or just copy-pust this code
> 
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}`

![2](https://user-images.githubusercontent.com/69119928/129969051-e3a4c5d9-8687-491a-b07a-26f4aca5169c.jpg)

---

> You need go to the folder **mysite** (`cd mysite`).

---

> Next command `py manage.py makemigrations`
>               `py manage.py migrate`
>               `py manage.py runserver`
              
---

> And in the  web-browser  go to the *http://127.0.0.1/* or *localhost*.
---

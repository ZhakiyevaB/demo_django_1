pip install django==4
poetry add django==4
pip freeze > requirements.txt
django-admin startproject config .
python manage.py runserver

DATABASES = { 
    'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2',
                 'NAME': 'myproject', 
                 'USER': 'myprojectuser', 
                 'PASSWORD': 'password', 
                 'HOST': 'localhost', 
                 'PORT': '', 
                } 
    }
pip install django psycopg2
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp app /name/
python manage.py startapp post
python manage.py makemigrations
python manage.py migrate
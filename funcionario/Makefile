.PHONY: install run test env createsuperuser

SECRET_KEY := $(shell cat /dev/urandom | tr -dc 'A-Za-z0-9@$%&_+=!?,.*[]()' | head -c 32)


createsuperuser:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell


env:
	echo "SECRET_KEY='$(SECRET_KEY)'\n\
	DJANGO_CONFIGURATION='Development'\n\
	" > .env

envprod:
	echo "SECRET_KEY='$(SECRET_KEY)'\n\
	DJANGO_CONFIGURATION='Production'\n\
	" > .env


install: env createsuperuser
	pip install pipenv
	pipenv install
	pipenv install --dev


run:
	pipenv run ./manage.py runserver


test:
	pipenv run pytest --cov-report term-missing

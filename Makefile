.PHONY: install run test env
.SILENT: env run

SECRET_KEY := $(shell cat /dev/urandom | tr -dc 'A-Za-z0-9@$%&_+=!?,.*[]()' | head -c 64)


env:
	echo "SECRET_KEY='$(SECRET_KEY)'\n\
	DJANGO_CONFIGURATION='Production'\n\
	" > cep/.env
	cp cep/.env funcionario/.env
	echo 'CEP_URL=http://localhost:8001/api/v1/ceps/' >> funcionario/.env


install: env
	pip install pipenv
	pipenv install
	pipenv install --dev


run:
	echo "\nAcesse:\n\
	http://localhost:8001/api/v1/ceps/\n\
	http://localhost:8002/api/v1/funcionarios/\n\n"
	docker-compose up


test:
	(cd cep && pipenv run pytest)
	docker-compose up -d cep
	(cd funcionario && pipenv run pytest)
	docker-compose stop

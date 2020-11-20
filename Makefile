MY_VIRTUAL_ENV = household_calculator_2020

TCPPORT=8000
RUNSERVER=python manage.py runserver 0.0.0.0:${TCPPORT}

domigrate: virtualenv
	python manage.py makemigrations
	python manage.py migrate

run:	virtualenv
		${RUNSERVER}

virtualenv:
	@if test "$$(basename "$${VIRTUAL_ENV}")" != "${MY_VIRTUAL_ENV}"; \
	then echo "Please activate your virtualenv by typing: workon ${MY_VIRTUAL_ENV}" ; \
	>&2; exit 44; \
	fi

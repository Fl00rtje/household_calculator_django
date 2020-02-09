MY_VIRTUAL_ENV = household_calculator_2019

TCPPORT=8000
RUNSERVER=python manage.py runserver 0.0.0.0:${TCPPORT}

#-run:	start server :${TCPPORT} in the background and sleep 3
run:	virtualenv
		${RUNSERVER}

virtualenv:
	@if test "$$(basename "$${VIRTUAL_ENV}")" != "${MY_VIRTUAL_ENV}"; \
	then echo "Please activate your virtualenv by typing: workon ${MY_VIRTUAL_ENV}" ; \
	>&2; exit 44; \
	fi

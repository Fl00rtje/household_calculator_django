TCPPORT=8000
RUNSERVER=python manage.py runserver 0.0.0.0:${TCPPORT}

#-run:	start server :${TCPPORT} in the background and sleep 3
run:
	${RUNSERVER} & sleep 3
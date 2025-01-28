mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
db:
	./manage.py createsuperuser
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn scoops4u_capstone.wsgi
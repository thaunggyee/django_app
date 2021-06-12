from python:3.9

workdir /app

copy . /app

run pip install -r requirements.txt

cmd ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

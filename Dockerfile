<<<<<<< HEAD
FROM python:3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
=======
from python:3.9

workdir /app

copy . /app

run pip install -r requirements.txt

cmd ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
>>>>>>> 349a70d9b3dc27d6b2c0e4f91da938c075be9c14

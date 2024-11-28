FROM python:3.12-slim

WORKDIR /app

COPY /requirements.txt /

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .

# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"] - данная команда прописывается тут если в docker-compose.yaml не указана

# --no-cache-dir - устанавливается флаг, что бы не кешировались список зависимостей
FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN apt update && apt install netcat -y

RUN pip install mysqlclient
RUN pip install -r requirements.txt


CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" \
    && python manage.py shell -c "sleep 20 && python manage.py runserver 0.0.0.0:8000" \

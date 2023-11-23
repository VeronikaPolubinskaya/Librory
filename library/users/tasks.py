from celery import shared_task
from django.core.mail import send_mail
from .models import User

@shared_task
def send_email(user_id):
    user = User.objects.get(id=user_id)

    subject = f'Приветствуем,  {user.name}!'
    message = f'Приветствуем, {user.name}!\n\n' \
              f'Добро пожаловать в нашу библиотеку!'

    send_mail(
        subject,
        message,
        'searchmp2@gmail.com',
        [user.email],
        fail_silently=False,
    )
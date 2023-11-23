from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.id}. Пользователь {self.name}'
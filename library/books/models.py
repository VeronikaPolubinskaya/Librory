from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    isbn = models.CharField(max_length=13)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.id} Книга {self.name}'

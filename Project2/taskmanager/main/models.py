from django.db import models

class Task(models.Model):
    title = models.CharField('Nagłówek', max_length=50)
    text = models.TextField('Tekst dla zadania')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Zadanie'
        verbose_name_plural = 'Zadania'
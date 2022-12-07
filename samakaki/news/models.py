from django.db import models

class Articles(models.Model):
    title = models.CharField('Nagłówek', max_length=50)
    preview = models.CharField('Ogłoszenie', max_length=250)
    full_text = models.TextField('Artykuł')
    date = models.DateTimeField('Data publikacji')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Aktualność'
        verbose_name_plural = 'Aktualności'
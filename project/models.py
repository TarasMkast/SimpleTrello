from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Імя проекту')
    description = models.CharField(max_length=300, verbose_name='Опис проекту')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'

    def __str__(self):
        return self.name

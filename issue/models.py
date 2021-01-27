from django.db import models


class Issue(models.Model):
    name = models.CharField(max_length=50, verbose_name='Імя задачі')
    descriptiom = models.CharField(max_length=300, verbose_name='Опис задачі')
    status = models.CharField(max_length=30, verbose_name='Статус')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

    def __str__(self):
        return self.name


class Image(models.Model):
    img = models.ImageField(upload_to='/image',
                            height_field=100, width_field=100)
    issue = models.ForeignKey(Issue, on_delete=True, related_name='ImageRel')

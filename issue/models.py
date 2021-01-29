from django.db import models
from users.models import User
from project.models import Project
from issue.utils import StatusIssue


class Issue(models.Model):
    name = models.CharField(max_length=50, verbose_name='Імя задачі')
    description = models.CharField(max_length=300, verbose_name='Опис задачі')
    status = models.CharField(max_length=30, verbose_name='Статус', choices=StatusIssue.choices,
                              default=StatusIssue.TODO)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(verbose_name='Зображення', height_field=100, width_field=100)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='ImageRel')

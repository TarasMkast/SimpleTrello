from django.db import models


class StatusIssue(models.TextChoices):
    TODO = 'TODO', 'TODO'
    IN_PROGRESS = 'In progress', 'In progress'
    TEST = 'TEST', 'Test'
    DONE = "Done", "Done"

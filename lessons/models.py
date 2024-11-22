from django.db import models

class Lesson (models.Model):
    title = models.CharField("Название", max_length=150)
    date = models.DateField("Дата обновления", auto_now=True, auto_created=True)
    
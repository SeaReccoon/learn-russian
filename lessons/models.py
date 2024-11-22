from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Lesson (models.Model):
    title = models.CharField("Название", max_length=150)
    date = models.DateField("Дата обновления", auto_now=True, auto_created=True)
    content = CKEditor5Field("Содержимое")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Lesson (models.Model):
    title = models.CharField("Название", max_length=150)
    date = models.DateField("Дата обновления", auto_now=True, auto_created=True)
    content = CKEditor5Field("Содержимое")
    category = models.CharField("Категория", max_length=120, null=True, blank=True)
    number = models.IntegerField("Номер занятия", null=True, blank=True)

    def __str__(self):
        return f"{self.category}. Урок {self.number}. {self.title}"
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering =["category", "number"]

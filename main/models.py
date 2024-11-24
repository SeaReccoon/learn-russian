from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="Отзыв")
    text = models.TextField("Текст")

    def __str__(self):
        return "Отзыв " + self.user.username
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
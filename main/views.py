from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from main.models import Feedback
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

# Функция для отправки сообщений на почту
def email(subject, content):
    send_mail(subject, content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, ])

# Главная страница
class IndexView (TemplateView):
    template_name = "main/index.html"

# Страница обратной связи
class FeedbackView (LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = "main/feedback.html"
    fields = ["text",]

    # Получение ссылки на страницу после усшеного заполнения формы
    def get_success_url(self):
        return reverse("success_feedback")
    
    # Отправка сообщения на электронную почту после проверки формы
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        subject = "Обратная связь от " + user.username
        email(subject, form.data["text"])
        return super().form_valid(form)

# Страница успешной обратной связи
class SuccessFeedback (TemplateView):
    template_name = "main/success_feedback.html"

# О проекте
class AboutView (TemplateView):
    template_name = "main/about.html"

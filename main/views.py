from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from main.models import Feedback
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

def email(subject, content):
    send_mail(subject, content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, ])

class IndexView (TemplateView):
    template_name = "main/index.html"

class FeedbackView (LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = "main/feedback.html"
    fields = ["text",]

    def get_success_url(self):
        return reverse("success_feedback")
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        subject = "Обратная связь от " + user.username
        email(subject, form.data["text"])
        return super().form_valid(form)

class SuccessFeedback (TemplateView):
    template_name = "main/success_feedback.html"

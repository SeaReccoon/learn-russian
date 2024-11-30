from django.views.generic import ListView, TemplateView
from testing.models import Question
import random

class QuestionsListView(ListView):
    model = Question
    template_name = "testing/test.html"
    context_object_name = "questions"

    def get_queryset(self):
        questions = Question.objects.all()
        random.shuffle(list(questions))
        return questions

class StartTestingView(TemplateView):
    template_name = "testing/start.html"

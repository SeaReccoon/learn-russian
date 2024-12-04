from django.views.generic import ListView, DetailView
from lessons.models import Lesson

class ListLessonsView(ListView):
    model = Lesson
    template_name = "lessons/list.html"
    context_object_name = "categories"

    # Получаем уроки и группируем их по категориям
    def get_queryset(self):
        categories = {}
        lessons = Lesson.objects.all()
        for lesson in lessons:
            category = lesson.category
            if not category in categories:
                categories[category] = []
            categories[category].append(lesson)
        return categories

class LessonView(DetailView):
    model = Lesson
    template_name = "lessons/lesson.html"
    context_object_name = "lesson"

    # Получаем все уроки из той же категории
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["other_lessons"] = Lesson.objects.filter(category=obj.category)
        return context

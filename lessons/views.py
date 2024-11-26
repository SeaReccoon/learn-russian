from django.views.generic import ListView
from lessons.models import Lesson

class ListLessonsView(ListView):
    model = Lesson
    template_name = "lessons/list.html"
    context_object_name = "categories"

    def get_queryset(self):
        categories = {}
        lessons = Lesson.objects.all()
        for lesson in lessons:
            category = lesson.category
            if not category in categories:
                categories[category] = []
            categories[category].append(lesson)
        return categories

from django.urls import path
from lessons.views import ListLessonsView, LessonView

urlpatterns = [
    path("lesson/<int:pk>", LessonView.as_view(), name="lesson"),
    path("list/", ListLessonsView.as_view(), name="lessons_list")
]
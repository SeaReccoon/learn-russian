from django.urls import path
from lessons.views import ListLessonsView

urlpatterns = [
    path("list/", ListLessonsView.as_view(), name="lessons_list")
]
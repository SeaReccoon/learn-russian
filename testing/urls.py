from django.urls import path
from testing.views import QuestionsListView, StartTestingView

urlpatterns = [
    path("test/", QuestionsListView.as_view(), name="testing"),
    path("", StartTestingView.as_view(), name="start_test")
]
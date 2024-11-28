from django.urls import path
from main.views import IndexView, FeedbackView, SuccessFeedback, AboutView

urlpatterns = [
    path("feedback/success/", SuccessFeedback.as_view(), name="success_feedback"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("about/", AboutView.as_view(), name="about"),
    path("", IndexView.as_view(), name="index")
]
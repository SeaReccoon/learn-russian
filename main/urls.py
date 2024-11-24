from django.urls import path
from main.views import IndexView, FeedbackView, SuccessFeedback

urlpatterns = [
    path("feedback/success/", SuccessFeedback.as_view(), name="success_feedback"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("", IndexView.as_view(), name="index")
]
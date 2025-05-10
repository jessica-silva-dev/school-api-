from django.urls import path
from .views import AssessmentApiView

urlpatterns = [
    path('assessments', AssessmentApiView.as_view()),
]


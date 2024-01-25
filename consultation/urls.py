from django.urls import path
from .views import ConsultationList,ConsultationDetail

urlpatterns = [
    path('',ConsultationList.as_view()),
    path('<int:pk>/',ConsultationDetail.as_view()),
    # New Path to be added hereby -->
    ]
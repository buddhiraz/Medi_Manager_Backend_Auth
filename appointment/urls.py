from django.urls import path
from .views import AppointmentDetail, AppointmentList

urlpatterns = [
    path('',AppointmentList.as_view()),
    path('<int:pk>/',AppointmentDetail.as_view()),
    #New Path to be added hereby -->
    
    ]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='tests'),
    path('email/',views.test_email, name='email'),
    path('schedule_email/',views.schedule_mail, name='schedule_mail'),
]
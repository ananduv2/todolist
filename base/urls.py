from django.urls import path
from .views import views

urlpatterns=[
    path('', views.taskList,name='tasks'),
]
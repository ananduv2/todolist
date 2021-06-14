"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from base import views as baseview
from base.views import CustomLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', baseview.RegisterView.as_view(),name='register'),

    path('admin/', admin.site.urls),
    path('', baseview.TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', baseview.TaskDetail.as_view(),name='details'),
    path('create-task/', baseview.TaskCreate.as_view(),name='create'),
    path('edit/<int:pk>/', baseview.TaskUpdate.as_view(),name='edit'),
    path('delete/<int:pk>/', baseview.TaskDelete.as_view(),name='delete'),
]

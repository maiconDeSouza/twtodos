"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todos.views import TodoList, CreateList, UpateList, DeleteList, CompleteList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoList.as_view(), name="todo_list"),
    path('create', CreateList.as_view(), name="create_list"),
    path('update/<int:pk>', UpateList.as_view(), name='update_list'),
    path('delete/<int:pk>', DeleteList.as_view(), name='delete_list'),
    path('complete/<int:pk>', CompleteList.as_view(), name='complete_list')

]

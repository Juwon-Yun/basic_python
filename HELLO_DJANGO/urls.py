"""HELLO_DJANGO URL Configuration

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
from HELLO_DJANGO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello',views.index, name='hello'),
    path('param',views.param1, name='param'),
    path('param2',views.param2, name='param2'),
    path('myforward',views.myforward, name='myforward'),
    path('emp_list',views.emp_list, name='emp_list'),
    path('insert.ajax',views.insert_ajax, name='insert.ajax'),
    path('update.ajax',views.update_ajax, name='update.ajax'),
    path('delete.ajax',views.delete_ajax, name='delete.ajax'),
]





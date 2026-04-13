"""
URL configuration for hotelManagement project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rooms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.roomsList , name='roomsList'),
    path('CategoryList', views.CategoryList, name ='CategoryList'),
    path('createCategory', views.createCategory, name ='createCategory'),
    path('createRoom', views.createRoom, name='createRoom'),
    path('room/<int:id>/', views.roomDetail, name='roomDetail'),
    path('room/edit/<int:id>/', views.editRoom, name='editRoom'),
    path('room/delete/<int:id>/', views.deleteRoom, name='deleteRoom'),

]
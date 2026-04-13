from django.urls import path
from .import views

urlpatterns = [
    path('', views.roomsList , name='roomsList'),
    path('CategoryList', views.CategoryList, name ='CategoryList'),
    path('createCategory', views.createCategory, name ='createCategory'),
    path('createRoom', views.createRoom, name='createRoom'),
    path('room/<int:id>/', views.roomDetail, name='roomDetail'),
    path('room/edit/<int:id>/', views.editRoom, name='editRoom'),
    path('room/delete/<int:id>/', views.deleteRoom, name='deleteRoom'),

]
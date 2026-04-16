from django.urls import path
from .import views

urlpatterns = [
    path('', views.roomsList, name='roomsList'),
    path('rooms/', views.roomsList, name='roomsList'),
    path('rooms/categories/', views.CategoryList, name='CategoryList'),
    path('rooms/categories/create/', views.createCategory, name='createCategory'),
    path('rooms/create/', views.createRoom, name='createRoom'),
    path('rooms/<int:id>/', views.roomDetail, name='roomDetail'),
    path('rooms/<int:id>/edit/', views.editRoom, name='editRoom'),
    path('rooms/<int:id>/delete/', views.deleteRoom, name='deleteRoom'),
]
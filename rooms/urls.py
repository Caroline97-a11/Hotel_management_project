from django.urls import path
from .import views

urlpatterns = [
    path('', views.roomsList, name='roomsList'),
    path('categories/', views.CategoryList, name='CategoryList'),
    path('categories/create/', views.createCategory, name='createCategory'),
    path('create/', views.createRoom, name='createRoom'),
    path('<int:id>/', views.roomDetail, name='roomDetail'),
    path('<int:id>/edit/', views.editRoom, name='editRoom'),
    path('<int:id>/delete/', views.deleteRoom, name='deleteRoom'),
    path('edit/<int:id>/', views.edit_category, name='edit_category'),
    path('delete/<int:id>/', views.delete_category, name='delete_category'),
]
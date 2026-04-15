from django.urls import path
from . import views   

urlpatterns = [
    path('guests/', views.guestList, name='guestList'),
    path('guests/add/', views.addGuest, name='addGuest'),
    path('guests/<int:pk>/', views.viewGuest, name='viewGuest'),
    path('guests/<int:pk>/edit/', views.editGuest, name='editGuest'),
    path('guests/<int:pk>/delete/', views.deleteGuest, name='deleteGuest'),
]
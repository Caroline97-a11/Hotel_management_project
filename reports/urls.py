from django.urls import path
from reports.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
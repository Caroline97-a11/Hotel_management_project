from django import forms
from .models import Room, RoomType


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name', 'price']
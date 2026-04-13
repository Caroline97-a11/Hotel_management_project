from django import forms
from .models import Room, RoomType


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

        error_messages ={
            'room_number':{
                'required':'Please enter a valid room number'}
                }
        error_messages ={
            'room_category':{
                'required':'Please enter a valid room category'}
                }
        


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name', 'price']
        error_messages ={
            'name':{
                'required':'Please enter a valid room number'}
                }
        error_messages ={
            'price':{
                'required':'Please enter  valid amount'}
                }
        


       
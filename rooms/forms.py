from django import forms
from .models import Room, RoomType


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        labels ={
            'room_number': 'Please enter a room number',
            'room_category': 'Please select a room category',
            'room_status': 'Please select a room status'
        }
        widget ={
            'room_status': forms.Select(attrs={'class':'form_control'})
        }

        error_messages ={
            'room_number':{
                'required':'Please enter a valid room number'},
            'room_category':{
                'required':'Please enter a valid room category'}
                }
        


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['category', 'price']

        labels ={
            'category': 'Please enter a room category',
            'price': 'Please enter a room price'
        }
        error_messages ={
            'name':{
                'required':'Please enter a valid room number'},
            'price':{
                'required':'Please enter  valid amount'}
                }
        


       
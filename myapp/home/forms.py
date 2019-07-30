from django import forms
from .models import *



class firstform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class signupform(forms.ModelForm):
    class Meta:
        model = Auth
        fields = '__all__'


class HotelForm(forms.ModelForm) :

    class Meta :
        model = Hotel
        fields = ['name', 'hotel_Main_Img']


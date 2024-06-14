from cars import models
from django import forms

class Car_Brands(forms.ModelForm):
    class Meta:
        model = models.CarBrande
        fields = '__all__'

class Car_Models(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']
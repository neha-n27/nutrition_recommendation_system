from django import forms

class FoodForm(forms.Form):
    food_name = forms.CharField(label='Food Name', max_length=100)

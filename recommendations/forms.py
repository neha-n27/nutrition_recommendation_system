from django import forms

class PreferenceForm(forms.Form):
    DIET_CHOICES = [
        ('balanced', 'Balanced'),
        ('high-protein', 'High-Protein'),
        ('low-fat', 'Low-Fat'),
        ('low-carb', 'Low-Carb'),
        ('high-fiber', 'High-Fiber'),
        ('low-sodium', 'Low-Sodium'),
    ]
    ALLERGY_CHOICES = [
        ('gluten-free', 'Gluten-Free'),
        ('peanut-free', 'Peanut-Free'),
        ('tree-nut-free', 'Tree Nut-Free'),
        ('dairy-free', 'Dairy-Free'),
        ('egg-free', 'Egg-Free'),
        ('shellfish-free', 'Shellfish-Free'),
        ('soy-free', 'Soy-Free'),
        ('vegan','Vegan'),
        ('vegetarian','Vegetarian'),
        ('wheat-free','Wheat-Free'),
    ]

    dietary_preferences = forms.ChoiceField(choices=DIET_CHOICES, required=False)
    Specification = forms.ChoiceField(choices=ALLERGY_CHOICES, required=False)
    calories_min = forms.IntegerField(required=True)
    calories_max = forms.IntegerField(required=True)
    # Add other fields as needed

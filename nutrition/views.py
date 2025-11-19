import requests
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse
from .forms import FoodForm
from django.conf import settings
import json

def get_nutrient_data(food_name):
    api_key = 'fcaNcVJgKLibkxVBL9XSwXfJt04OfgYCXp8c5nH8'
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?query={food_name}&api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'foods' in data and len(data['foods']) > 0:
            return data['foods'][0]['foodNutrients']
    return None

def calculate_activity_times(calories):
    activities = {
        'jogging': calories / 8,  # 8 calories per minute
        'yoga': calories / 3,     # 3 calories per minute
        'running': calories / 11, # 11 calories per minute
        'walking': calories / 4   # 4 calories per minute
    }
    return activities

def food_nutrient_view(request):
    nutrient_data = None
    activity_times = None
    nutrient_values = {'protein': 0, 'lipid': 0, 'carbohydrate': 0, 'energy': 0}

    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food_name = form.cleaned_data['food_name']
            nutrient_data = get_nutrient_data(food_name)
            if nutrient_data:
                for nutrient in nutrient_data:
                    if nutrient['nutrientName'] == 'Energy':
                        calories = nutrient['value']
                        nutrient_values['energy'] = nutrient['value']
                    elif nutrient['nutrientName'] == 'Protein':
                        nutrient_values['protein'] = nutrient['value']
                    elif nutrient['nutrientName'] == 'Total lipid (fat)':
                        nutrient_values['lipid'] = nutrient['value']
                    elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
                        nutrient_values['carbohydrate'] = nutrient['value']
                activity_times = calculate_activity_times(calories)
    else:
        form = FoodForm()
    
    return render(request, 'nutrition/food_nutrient.html', {
        'form': form, 
        'nutrient_data': nutrient_data, 
        'activity_times': activity_times,
        'nutrient_values': nutrient_values
    })

def pie_chart(request):
    food_name = request.GET.get('food_name')
    nutrient_data = get_nutrient_data(food_name)
    nutrient_values = {'protein': 0, 'lipid': 0, 'carbohydrate': 0, 'fiber': 0}
    
    if nutrient_data:
        for nutrient in nutrient_data:
            if nutrient['nutrientName'] == 'Fiber, total dietary':
                nutrient_values['fiber'] = nutrient['value']
            elif nutrient['nutrientName'] == 'Protein':
                nutrient_values['protein'] = nutrient['value']
            elif nutrient['nutrientName'] == 'Total lipid (fat)':
                nutrient_values['lipid'] = nutrient['value']
            elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
                nutrient_values['carbohydrate'] = nutrient['value']
                
    labels = list(nutrient_values.keys())
    values = list(nutrient_values.values())

    context = {
        'labels_json': json.dumps(labels),
        'values_json': json.dumps(values),
    }

    fig = px.pie(values=values, names=labels, title='')
    pie_chart_html = fig.to_html(full_html=False)
    
    return render(request, 'nutrition/pie_chart.html', {'pie_chart_html': pie_chart_html})

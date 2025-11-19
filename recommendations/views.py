from django.shortcuts import render
from .forms import PreferenceForm
import requests

def get_recipe_recommendations(preferences):
    # Replace 'YOUR_EDAMAM_API_KEY' and 'YOUR_EDAMAM_APP_ID' with your actual Edamam API credentials
    api_url = 'https://api.edamam.com/api/recipes/v2?type=any'
    params = {
        'app_id': '8cbf096e',
        'app_key': '2de7b3248272bd769c05178582f8f3c9',
        'diet': preferences['dietary_preferences'],
        'health':preferences['Specification'],
        'calories': f"{preferences['calories_min']}-{preferences['calories_max']}",
         # Limit to 10 results
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        recipes = []
        for hit in data.get('hits', []):
            recipe_data = hit.get('recipe', {})
            total_calories = recipe_data.get('calories', 0)
            yield_value = recipe_data.get('yield', 1)  # Default to 1 if yield is not provided
            calories_per_serving = total_calories / yield_value
            
            if preferences['calories_min'] <= calories_per_serving <= preferences['calories_max']:
                recipe = {
                    'label': recipe_data.get('label', 'No Label'),
                    'url': recipe_data.get('url', '#'),
                    'image': recipe_data.get('image', ''),
                    'calories': total_calories,
                    'calories_per_serving': calories_per_serving,
                    'ingredients': recipe_data.get('ingredientLines', []),
                    'yield': yield_value,  # Add yield to recipe dictionary
                }
                
                recipes.append(recipe)
        
        # Ensure the calories fall within the specified range after the initial fetch
        filtered_recipes = [
            recipe for recipe in recipes
            if preferences['calories_min'] <= recipe['calories_per_serving'] <= preferences['calories_max']
        ]
        
        for recipe in filtered_recipes:
            # Printing for debugging or logging
            print(f"Recipe: {recipe['label']}")
            print(f"URL: {recipe['url']}")
            print(f"Total Calories: {recipe['calories']}")
            print(f"Calories per Serving: {recipe['calories_per_serving']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Yield: {recipe['yield']}")
            print()
        
        return filtered_recipes
    else:
        print(f"Error: {response.status_code}")
        return []

def preference_view(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            preferences = form.cleaned_data
            recipes = get_recipe_recommendations(preferences)
            return render(request, 'recommendations/results.html', {'recipes': recipes})

    else:
        form = PreferenceForm()
    return render(request, 'recommendations/preferences.html', {'form': form})


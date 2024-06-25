from flask import render_template
from flask.views import MethodView
import requests

MEAL_API_URL = "https://www.themealdb.com/api/json/v1/1/random.php"

class Index(MethodView):
    def get(self):
        return render_template('index.html')
    
    def post(self):
        """Makes a call to `themealdb` API for a random meal.
        The response is a json file populated with numerous fields.
        ex. strMeasure, strIngredient[1:21], strInstructions
            Returns:
                render_template('meal.html', args)
        """
        meal = None
        ingredients = []
        response = requests.get(MEAL_API_URL)
        meal = response.json()['meals'][0]
        if meal:
            ingredients = [
                f"{meal[f'strMeasure{i}']} {meal[f'strIngredient{i}']}".strip()
                for i in range(1, 21)
                if meal[f'strIngredient{i}']
            ]
        return render_template('meal.html', meal=meal, ingredients=ingredients)
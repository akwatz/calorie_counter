from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_calories():
    food = request.form['food']
    response = requests.get('https://api.calorieninjas.com/v1/nutrition', 
                                headers={'X-Api-Key': 'sTC6y/A4Zt7HrKqqdcv9iQ==8KSu1rjPFHMtc2dd'},
                                params={'query': food})
    if response.status_code == 200:
        food_data = []
        for data in response.json()['items']:
            # Extract relevant data
            name = data['name']
            calories = data['calories']
            serving_size = data['serving_size_g']
            fat_total = data['fat_total_g']
            fat_saturated = data['fat_saturated_g']
            protein = data['protein_g']
            sodium = data['sodium_mg']
            potassium = data['potassium_mg']
            cholesterol = data['cholesterol_mg']
            carbohydrates_total = data['carbohydrates_total_g']
            fiber = data['fiber_g']
            sugar = data['sugar_g']

            # Add data to list
            food_data.append({'name': name, 'calories': calories, 'serving_size': serving_size,
                            'fat_total': fat_total, 'fat_saturated': fat_saturated, 'protein': protein,
                            'sodium': sodium, 'potassium': potassium, 'cholesterol': cholesterol,
                            'carbohydrates_total': carbohydrates_total, 'fiber': fiber, 'sugar': sugar})


        return render_template('index.html', food_desc =food,  food_data=food_data)
    else:
        return 'Error getting data'


if __name__ == '__main__':
    app.run(debug=True)
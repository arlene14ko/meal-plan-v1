from flask import Flask, render_template
from recipes import Recipe
app = Flask(__name__)


@app.route('/')
@app.route('/mealplan')
def index():
    recipes_list = Recipe.list_recipes()
    dinner = Recipe.dinner_recipes()
    return render_template("mealplan.html", recipes=dinner)

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")

@app.route('/calorie')
def calorie():
    return render_template("calorie.html")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/mealplan')
def index():
    meals = ["chicken", "beef", "rice", "noodles"]
    return render_template("mealplan.html", recipes=meals)

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")

@app.route('/calorie')
def calorie():
    return render_template("calorie.html")


if __name__ == "__main__":
    app.run(debug=True)
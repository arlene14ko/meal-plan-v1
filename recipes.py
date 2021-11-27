import pandas as pd

class Recipe:

    def load_recipe():
        recipe_file = "data/recipes.csv"
        # read csv file
        recipe_list = pd.read_csv(recipe_file)
        # display DataFrame
        #print(recipe_list)
        return recipe_list

    def list_recipes():
        recipe_list = Recipe.load_recipe()
        list_of_recipes = []
        for recipe in recipe_list.Recipe:
            #print(recipe)
            list_of_recipes.append(recipe)
        return list_of_recipes

    def dinner_recipes():
        recipe_list = Recipe.load_recipe()
        dinner_rec = recipe_list[recipe_list.Type == "Dinner"]
        dinner = []
        for recipe in dinner_rec.Recipe:
            dinner.append(recipe)
        return dinner

    
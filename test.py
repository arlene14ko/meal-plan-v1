import pandas as pd

def load_recipe():
    recipe_file = "data/recipes.csv"
    # read csv file
    recipe_list = pd.read_csv(recipe_file)
    # display DataFrame
    #print(recipe_list)
    return recipe_list

def list_recipes():
    recipe_list = load_recipe()
    list_of_recipes = []
    for recipe in recipe_list.Recipe:
        #print(recipe)
        list_of_recipes.append(recipe)
    return list_of_recipes

def dinner_recipes():
    recipe_list = load_recipe()
    dinner = []
    for recipe in recipe_list.Recipe:
        for type in recipe_list.Type:
            if type == "Dinner":
                dinner.append(recipe)
    return dinner


rec = load_recipe()
dinner = []
for i in rec:
    print(i)

    
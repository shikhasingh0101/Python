class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, title, ingredients, instructions, author):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.author = author

class User:
    def __init__(self, username):
        self.username = username
        self.recipes = []

    def add_recipe(self, title, ingredients, instructions):
        recipe = Recipe(title, ingredients, instructions, self)
        self.recipes.append(recipe)
        print(f"Recipe '{title}' added by {self.username}.")

    def search_by_ingredient(self, ingredient_name):
        # Search for recipes containing the specified ingredient
        matching_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name.lower() == ingredient_name.lower():
                    matching_recipes.append(recipe)
                    break  # Break the inner loop when the ingredient is found in the recipe

        return matching_recipes

# Example usage:
# Create ingredients, users, and add recipes
ingredient1 = Ingredient("Chicken")
ingredient2 = Ingredient("Tomato")
ingredient3 = Ingredient("Onion")

user1 = User("Alice")
user2 = User("Bob")

user1.add_recipe("Chicken Curry", [ingredient1, ingredient2, ingredient3], "Cook chicken with tomatoes and onions.")
user1.add_recipe("Tomato Salad", [ingredient2, ingredient3], "Mix tomatoes and onions.")

user2.add_recipe("Onion Soup", [ingredient3], "Boil onions to make a delicious soup.")

# Search for recipes by ingredient
ingredient_to_search = "Tomato"
matching_recipes_user1 = user1.search_by_ingredient(ingredient_to_search)
matching_recipes_user2 = user2.search_by_ingredient(ingredient_to_search)

# Display matching recipes
print(f"\nRecipes containing '{ingredient_to_search}':")
print(f"From {user1.username}:")
for recipe in matching_recipes_user1:
    print(f"{recipe.title} by {recipe.author.username}")

print(f"\nFrom {user2.username}:")
for recipe in matching_recipes_user2:
    print(f"{recipe.title} by {recipe.author.username}")

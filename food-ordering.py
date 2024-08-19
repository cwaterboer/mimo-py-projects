italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

#checks if the meal is in the menu
def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

#Returns the selected meal, by checking it against lists
def select_meal(name, food_type):
  if food_type=="Italian":
    return find_meal(name, italian_food)
  elif food_type=="Indian":
    return find_meal(name, indian_food)
  else:
    return None

#Displays the food in your different lists
def display_available_meals(food_type):
  if food_type == "Italian":
    print(f"Available Italian Meals:")
    for item in italian_food:
      print(item)
  elif food_type == "Indian":
    print(f"Available Indian Meals:")
    for item in indian_food:
      print(item)
  else:
    return "Invalid food type"
  
#Creates a summary of your order
def create_summary(name, amount, food_type):
  order = select_meal(food_type, name)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

#Displays the menu
print("Welcome to the Food Order System!")

#Asks which type of food you'd like
type_input = input("Which type of food would you like?")
display_available_meals(type_input)

#This section takes your order
name_input = input("Which meal would you like to order?")
amount_input =input("How many would you like?")

#This section creates a checkout summary based on your inputs
result = create_summary(type_input, name_input, amount_input)
print(result)

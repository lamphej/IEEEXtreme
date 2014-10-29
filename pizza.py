import sys

toppings = {
    'Anchovies': 50,
    'Artichoke': 60,
    'Bacon': 92,
    'Broccoli': 24,
    'Cheese': 80,
    'Chicken': 30,
    'Feta': 99,
    'Garlic': 8,
    'Ham': 46,
    'Jalapeno': 5,
    'Meatballs': 120,
    'Mushrooms': 11,
    'Olives': 25,
    'Onions': 11,
    'Pepperoni': 80,
    'Peppers': 6,
    'Pineapple': 21,
    'Ricotta': 108,
    'Sausage': 115,
    'Spinach': 18,
    'Tomatoes': 14
}

if __name__ == "__main__":
    calorie_count = 0
    readline__split = sys.stdin.readline().strip().split(' ', 1)
    combo_count, pizza_combos = readline__split
    pizza_combos = [c for c in pizza_combos.split(' ')]
    for i in range(0, len(pizza_combos), 2):
        slice_count = int(pizza_combos[i])
        for slice in range(slice_count):
            slice_calories = 270
            for topping in pizza_combos[i+1].split(','):
                slice_calories += toppings[topping]
            calorie_count += slice_calories
    print "The total calorie intake is %s" % calorie_count
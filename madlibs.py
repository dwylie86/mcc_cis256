# David Wylie
# CIS256 24903
# Python Refresher Silly Assignment: Mad Lib Generator

DEBUG = False # Turn this variable to True to populate the dictionary without inputs.

def create_mad_lib(debug):
    word_dict = {}
    
    if debug:
        word_dict = {
        "nationality": "Italian", 
        "chef_name": "Giuseppe",
        "dough_ingredient": "flour",
        "shape_adjective": "perfect",
        "shape_noun": "circle",
        "sauce_adjective": "spicy",
        "cheese_adjective": "melted",
        "toppings": "mushroom",
        "oven": "furnace",
        "slice_count": "8",
        "slice_shapes": "triangle",
        "gross_food": "beet",
        "favorite_food": "jamon de serano",
        "times_per_day": "47"
        }

    else:
        word_dict["nationality"] = input("Enter a nationality: ")
        word_dict["chef_name"] = input("Enter a someone's name: ")
        word_dict["dough_ingredient"] = input("Enter a cooking ingredient: ")
        word_dict["shape_adjective"] = input("Enter an adjective: ")
        word_dict["shape_noun"] = input("Enter a shape: ")
        word_dict["sauce_adjective"] = input("Enter an adjective: ")
        word_dict["cheese_adjective"] = input("Enter an adjective: ")
        word_dict["toppings"] = input("Enter a vegetable: ")
        word_dict["oven"] = input("Enter a kitchen appliance: ")
        word_dict["slice_count"] = input("Enter a number: ")
        word_dict["slice_shapes"] = input("Enter a shape: ")
        word_dict["gross_food"] = input("Enter your least favorite pizza topping: ")
        word_dict["favorite_food"] = input("Enter your favorite food: ")
        word_dict["times_per_day"] = input("Enter a number: ")
    
    mad_lib = (
        f"\n~The TRUE history of Pizza~\n" +
        f"Pizza was invented by a {word_dict['nationality']} chef named {word_dict['chef_name']}.\n" +
        f"To make a pizza, you need to take a lump of {word_dict['dough_ingredient']} and form it into a thin, {word_dict['shape_adjective']}, {word_dict['shape_noun']}.\n" +
        f"Then you cover the pizza with {word_dict['sauce_adjective']} sauce, {word_dict['cheese_adjective']} cheese, and freshly chopped {word_dict['toppings']}.\n" +
        f"Next you bake the pizza in a very hot {word_dict['oven']}. Finally, cut the pizza into {word_dict['slice_count']} {word_dict['slice_shapes']}s and serve.\n" +
        f"Some people like {word_dict['gross_food']} pizza the best, but my favorite is a pizza loaded with {word_dict['favorite_food']}.\n" +
        f"If I could, I would eat pizza {word_dict['times_per_day']} times a day!\n"
        )

    return mad_lib

def main():
    print("Welcome to the MADLIB Program!")
    print(create_mad_lib(DEBUG))

main()
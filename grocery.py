# Grocery List practice example:
# 1) Search by Fruit or Vegetable
# 2) Interaction: N = Item Name G = Category
# 3) Search by name case insentive,
#   return "The item entered does not exist in the grocery list."
# 4) Search by category prints list of all items in category
#    followed by the total number of items.
#    If empty "No items found in the category entered."

grocery_list = {
    "Apples": "Fruit",
    "Bananas": "Fruit",
    "Carrots": "Vegetable",
    "Broccoli": "Vegetable",
    "Milk": "Dairy",
    "Cheese": "Dairy",
    "Bread": "Bakery",
    "Chicken": "Meat"
    }


def search_by_item(item):
    formatted_item = item.title()
    if formatted_item in grocery_list:
        print(
            f"{formatted_item} belongs to the category: "
            f"{grocery_list[formatted_item]}"
            )
    else:
        print(
            f"The item, {formatted_item}, "
            f"does not exist in the grocery list."
            )


def search_by_category(category):
    items_in_category = [
        item for item, cat in grocery_list.items()
        if cat.lower() == category.lower()
        ]
    if items_in_category:
        print(f"Items in the {category.title()} category:")
        for item in items_in_category:
            print(f"- {item}")
        print(
            f"Total items in {category.title()} "
            f"category: {len(items_in_category)}"
            )
    else:
        print("No items found in the category entered.")


while True:
    # Prompt Mr. Hasty to choose search by item or by category
    choice = input(
        "Search by Item Name (N) or by Category (G)? ").strip().upper()

    if choice == "N":
        # Search by grocery item name
        item = input("Enter the grocery item name: ").strip()
        search_by_item(item)  # the function we made to search by item
    elif choice == "G":
        # Search by category
        category = input("Enter the category : ").strip()
        # The function we made to search by category
        search_by_category(category)

    else:
        print(
            "Invalid option. Please enter 'N' for Item Name or "
            "'G' for Category."
            )

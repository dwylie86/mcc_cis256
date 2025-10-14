# David Wylie
# CIS256 Fall 2025
# EX 3.1.2

# Part 2: Lists
# 1 Create and print a List:
tech_list = ["Laptop", "Smartphone"]
print(tech_list)

# 2 Use .append
tech_list.append("Tablet")
print(tech_list)

# 3 Insert into List:
tech_list.insert(1, "Smartwatch")
print(tech_list)

# 4 Check if an Item Exists:
if "Headphones" in tech_list:
    print("Headphones are available")
else:
    print("Headphones are not available")

# 5 Loop to Print List Elements on same line:
for item in tech_list:
    print(item, end=' ')
print()

# 6 Extend the list
new_items = ["Monitor", "Keyboard", "Mouse"]
tech_list.extend(new_items)
print(tech_list)

# 7 Replace an Item in the List
tech_list[tech_list.index("Smartphone")] = "Desktop"
print(tech_list)

# 8 Remove an Item using .pop()
tech_list.pop(tech_list.index("Tablet"))
print(tech_list)

# 9 Slicing with Lists: Print "Desktop", "Smartwatch", and "Monitor"
print(tech_list[1:4])

# 10 Create a List Using Comprehension
odd_number_list = [x for x in range(1, 21, 2)]
print(odd_number_list)

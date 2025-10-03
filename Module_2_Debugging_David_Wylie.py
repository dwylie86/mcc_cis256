# David Wylie
# CIS256 24903
# Debugging 2: Animal Class
# The following code defines two classes:
# Animal (the parent class) and Dog (the child class that inherits from Animal).
# However, the code contains several bugs. Can you find and fix them?

# Expected Output
# Some generic animal sound.
# Golden Retriever says Woof!
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound.")


# Dog class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):  # Added name for inheritance
        super().__init__(name)  # Inherited name from Animal
        self.breed = breed

    def speak(self):
        super().speak()  # Added this to match the expected output
        print(f"{self.breed} says Woof!")  # Changed speak variable to breed to match expected output.


# Creates animal object for first line of expected output
my_dog = Dog("Dog", "Golden Retriever")  # Added missing name attribute
my_dog.speak()

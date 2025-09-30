# David Wylie
# CIS256 24903
# Interactive 2: Fortune Teller
# A fortune teller that delivers random fortunes with mood assessments.
import random

# Fortunes and Moods are outside of the function show their nebulous nature!
fortunes = {
    "positive_fortunes": [
    "you should not be afraid of competition.",
    "an exciting opportunity lies ahead of you.",
    "you will get your mind set and confidence will lead you on.",
    "you will always be surrounded by true friends.",
    "better days await you!"
    ],
    "negative_fortunes": [
        "you will sell your computer to pay your cell phone bill.",
        "will fail at a new and complex undertaking.",
        "someone you love will stub their toe.",
        "a dog you will want to pet will refuse your approach.",
        "your ability to juggle many tasks will lead to a sore back."
    ]
}
moods = {
    "positive_moods": [
        "emboldened","pleased","refreshed"
     ],
     "negative_moods":
    [
        "distraught","skeptical","nauseated"
     ]
}

class FortuneTeller:
    """
    A fortune teller that delivers random fortunes with mood assessments.
    True to fortune telling form, your name and age have no impact on the fortune ;) 
    
    :attributes:
        name (str): The name of the person receiving the fortune.
        age (int): The age of the person receiving the fortune.
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def find_fortune(self):
        """
        Finds a random fortune from the fortunes dictionary.
        :params: None
        :return: A fortune from the fortunes dictionary.
        """
        category = random.choice(list(fortunes.keys()))
        fortune = random.choice(fortunes[category])
        return fortune

    def assess_mood(self,fortune):
        """
        Assesses how one would feel by determining if fortunes source
        is from the positive_fortunes or negative_fortunes
        Generates a random mood from corresponding mood dictionary
        :params: fortune (string)
        :return: mood
        """
        if fortune in fortunes["positive_fortunes"]:
            return random.choice(moods["positive_moods"])
        else:
            return random.choice(moods["negative_moods"])
    
    def tell_fortune(self):
        """
        Generates a fortune for the object with a combo of the other class functions
        :params: None
        :return: fortune as a complete string.
        """
        fortune = self.find_fortune()
        mood = self.assess_mood(fortune)
        fortune_string = (
            f"Dearest {self.name},\nOn year {self.age} of your earthly journey,\n"
            f"I divine that {fortune}\nI can see you are {mood} by this news."
            f"\nGoodbye!"
        )
        return fortune_string

    def __str__(self):
         """
         Function to test that the attributes and functions are working. 
         """
         fortune = self.find_fortune()
         return f"""
name: {self.name}
age: {self.age}
fortune: {fortune}
mood: {self.assess_mood(fortune)}
"""

def main():
    """
    Main entry point - Asks user for input, generates a fortune.
    
    :return: None.
    """
    print("Welcome, My Curious Visitor!")
    print("I, Pythos the Great, will read your fortune!")
    name = input("Please tell me your name: ")
    age = input("Please tell me your age: ")
    you = FortuneTeller(name, age)
    print(f"\n{you.tell_fortune()}")

main()

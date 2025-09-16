# David Wylie
# CIS256 24903
# PA1: Cultural Program
# This program displays cultural facts a selected country
# While DEBUG is True, the program will automatically print out facts about Japan

DEBUG = True # Turn this to False to run the program as intended

# Loaded up multiple countries' cultural facts into one dictionary
CULTURAL_DICTIONARY = {
    "Japan": [
        "Japanese",
        "Konnichiwa",
        "Sushi - A dish made of rice, seafood, and vegetables.",
        "Haru no Umi - A song that evokes the peaceful feeling of the Seto Inland Sea in springtime.",
        "Omiyage - The custom of bringing back small gifts (usually local food specialties) for family, friends, and coworkers when traveling.",
        ],
    "Spain": [
        "Spanish",
        "Hola",
        "Paella - A dish made of seafood, meat, vegetables, and beans.",
        "Entre Dos Aguas - A song that blends traditional flamenco with jazz and other influences.",
        "La Siesta - The traditional afternoon rest period between 2-5 PM when many businesses close, allowing people to enjoy a leisure time with family.",
        ],
    "Germany": [
        "German",
        "Guten Tag",
        "Sauerbraten - A traditional pot roast that is marinated for several days in vinnegar, wine, and spices.",
        "Die Lorelei - A song based on Heinrich Heine's poem about a beautiful siren",
        "Stammtisch - A regular gathering of friends or colleagues at the same table in a local pub or restaurant."
        ],
    "China": [
        "Chinese",
        "Nǐ Hǎo",
        "Peking Duck - A dish featuring crispy-skinned roasted duck served with thin pancakes.",
        "Mo Li Hua - A traditional Chinese folk song praising the beauty of jasmine flowers",
        "Hongbao - The custom of giving red envelopes containing money during holidays and special occasions."
        ],
    "England": [
        "English",
        "Hello",
        "Fish and Chips - Battered and deep-fried fish served with thick-cut fried potatoes",
        "Greensleeves - A traditional English often performed during Christmas",
        "Afternoon Tea - The ritual of taking tea with small sandwiches, scones, and cakes in the mid-afternoon."
        ]
}


class Culture:
    """
        Represents cultural information for a specific country.
    
        This class stores and provides access to cultural elements including
        greetings, food, music, and customs for a given country.
        
        :attributes:
            country (str): The name of the country
            culture (str): The name of the culture
            greeting (str): A common greeting in the local language
            food (str): Description of a traditional food dish
            music (str): Description of traditional or notable music
            custom (str): Description of a cultural custom or tradition
    """
    def __init__(self, country, culture, greeting, food, music, custom):
        self.country = country
        self.culture = culture  
        self.greeting = greeting
        self.food = food
        self.music = music
        self.custom = custom
   
    def get_greeting(self):
        return self.greeting
    
    def get_food(self):
        return self.food

    def get_music(self):
        return self.music
        
    def get_custom(self):
        return self.custom
        
    def __str__(self):
        return f"""
Information about {self.culture} culture:
Greeting: {self.greeting}
Food: {self.food}
Music: {self.music}
Custom: {self.custom}"""

def get_cultural_facts(dictionary):
    """
    Display cultural information for a user-selected country.
    
    :param dictionary: A dictionary with country names as keys and cultural data as values.
    :return: None (prints cultural information directly).
    """
    country_options = {}
    country_number = 0
    print(
        f"~LET'S LEARN ABOUT OTHER CULTURES~\n"
        f"Please select from the following countries:"
        )
    for country in dictionary:
        country_number += 1
        country_options.update({country_number:country})
        print(country_number, country)
    
    while True:
        try:
            selected_country = int(input("\nEnter the number of the country you would like to learn about: "))
            if selected_country in country_options:
                break
            else:
                print(f"Please enter a number between 1 and {len(country_options)}.")
        except ValueError:
            print("Please enter a valid number.")

    country_culture = Culture(country_options[selected_country], *CULTURAL_DICTIONARY[country_options[selected_country]])
    
    print(country_culture)

def main():
    """
    Main entry point - runs debug mode or interactive cultural learning program.
    
    :return: None (prints debug info if DEBUG=True, otherwise runs interactive program).
    """
    if DEBUG:
        japanese_culture = Culture("Japan", *CULTURAL_DICTIONARY["Japan"])
        print(
            f"DEBUG MODE:\n"
            f"Greeting Function: {japanese_culture.get_greeting()}\n"
            f"Food Function: {japanese_culture.get_food()}\n"
            f"Music Function: {japanese_culture.get_music()}\n"
            f"Custom Function: {japanese_culture.get_custom()}\n\n"
            f"String Function: {japanese_culture}\n"
            f"Turn DEBUG to False to run the program as intended."
            )
    else:
        get_cultural_facts(CULTURAL_DICTIONARY)
        print("Thanks for learning, Bye!")

main()
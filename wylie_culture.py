# David Wylie
# CIS256 24903
# PA1: Cultural Program

def greeting(country):
    language_dict = {
        "japan": "Konnichiwa",
        "spain": "Hola",
        "germany": "Guten Tag",
        "china": "Nǐ Hǎo",
        "england": "Hello"
    }
    if country in language_dict:
        return language_dict[country]
    else:
        return "Language not found in dictionary."
    
def food(country):
    food_dict = {
        "japan": "Sushi - A dish made of rice, seafood, and vegetables.",
        "spain": "Paella - A dish made of seafood, meat, vegetables, and beans.",
        "germany": "Sauerbraten - A traditional pot roast that is marinated for several days in vinnegar, wine, and spices.",
        "china": "Peking Duck - A dish featuring crispy-skinned roasted duck served with thin pancakes.",
        "england": "Fish and Chips - Battered and deep-fried fish served with thick-cut fried potatoes",
    }
    if country in food_dict:
        return food_dict[country]
    else:
        return "Food not found in dictionary."

def music(country):
    music_dict = {
        "japan": "Haru no Umi - A song that evokes the peaceful feeling of the Seto Inland Sea in springtime.",
        "spain": "Entre Dos Aguas - A song that blends traditional flamenco with jazz and other influences.",
        "germany": "Die Lorelei - A song based on Heinrich Heine's poem about a beautiful siren",
        "china": "Mo Li Hua - A traditional Chinese folk song praising the beauty of jasmine flowers",
        "england": "Greensleeves - A traditional English often performed during Christmas",
    }
    if country in music_dict:
        return music_dict[country]
    else:
        return "Music not found in dictionary."
    
def custom(country):
    custom_dict = {
        "japan": "Omiyage - The custom of bringing back small gifts (usually local food specialties) for family, friends, and coworkers when traveling.",
        "spain": "La Siesta - The traditional afternoon rest period between 2-5 PM when many businesses close, allowing people to enjoy a leisure time with family.",
        "germany": "Stammtisch - A regular gathering of friends or colleagues at the same table in a local pub or restaurant.",
        "china": "Hongbao - The custom of giving red envelopes containing money during holidays and special occasions.",
        "england": "Afternoon Tea - The ritual of taking tea with small sandwiches, scones, and cakes in the mid-afternoon."
    }
    if country in custom_dict:
        return custom_dict[country]
    else:
        return "Music not found in dictionary." 



print(greeting("japan"))
print(food("japan"))
print(music("japan"))
print(custom("japan"))
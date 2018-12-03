# The script of the game goes in this file.

# DEFS
define p = Character("You", color = "#FFA500")

define b_aff =  0
define b2_aff =  10000000
define DMG = 0

define subj = {"Male": "he", "Female": "she", "Nonbinary": "they" }
define obj = {"Male": "him", "Female": "her", "Nonbinary": "them" }
define poss = {"Male": "his", "Female": "her", "Nonbinary": "their" }
define refl = {"Male": "himself", "Female": "herself", "Nonbinary": "themself" }
define person = {"Male": "Boy", "Female": "Girl", "Nonbinary": "They" }

# INITIALIZE PYTHON
# $ = ONE-LINE PYTHON STATEMENT
init python:
    import random as r
    import json
    import os

    # Read in dogs from json
    with open(renpy.loader.transfn("resources/dogs.json")) as json_data:
        dogs = json.load(json_data, object_hook=as_dog)

    # ALWAYS CHOOSES FIRST DOG
    dog = dogs[0]
    d = Character(dog.name)
    owner = Owner()
    
    # Evaluate pronouns
    objPronoun = obj[dog.sex]
    subjPronoun = subj[dog.sex]
    possPronoun = poss[dog.sex]
    reflPronoun = refl[dog.sex]
    personPronoun = person[dog.sex]
    
# NEEDS A START LABEL
label start:
    # BACKGROUND SCENE / DOG PARK.PNG
    scene dog park

    $ day_done = []

label new_day:
    "What do you want to do today?"
    menu:
        "Stay at home." if not "home" in day_done:
            $ day_done.append("home")
            jump home_start
        "Go to the park." if not "park" in day_done:
            $ day_done.append("park")
            jump park_start
        "Go shopping." if not "shopping" in day_done:
            $ day_done.append("shopping")
            jump shopping_start
        "Take a walk." if not "walk" in day_done:
            $ day_done.append("walk")
            jump walk_start
        "Nothing else!":
            "nice demo end - dog [dog.traits.training]"
            "kindness [owner.traits.kindness]"
            "loyalty [owner.traits.loyalty]"
            "patience [owner.traits.patience]"
            "discipline [owner.traits.discipline]"


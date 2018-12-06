# The script of the game goes in this file.

# DEFS
define p = Character("You", color = "#FFA500")
define ds = Character("Dogging Sim Employee")

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
    subjPronoun_upper = subjPronoun.capitalize()
    possPronoun = poss[dog.sex]
    possPronoun_upper = possPronoun.capitalize()
    reflPronoun = refl[dog.sex]
    personPronoun = person[dog.sex]



# NEEDS A START LABEL
label start:
    
    # Load all background images
    image dogShelter = "scenes/dog shelter.png"
    image dogPark = "scenes/dog park.png"
    image home = "scenes/home.png"
    image petStore = "scenes/pet store.png"
    image petCoo = "scenes/petcoo.png"
    image outsideHouse = "scenes/outside house.png"
    image walkPath = "scenes/walk path.png"
    image shopping = "scenes/shopping.png"

    # BACKGROUND SCENE / DOG PARK.PNG
    # scene dog park
    scene dogShelter

    "Dogs. Perfect, fuzzy little bundles of joy and happiness. Why not adopt a dog?"
    "Maybe you're feeling lonely. Maybe you want someone to play fetch with. Maybe you want someone to guard your door."
    "It doesn't matter- people are different. And there's a perfect dog out there for everyone."
    ds "Welcome, new potential dog owner! To the Dogging Sim shelter."
    ds "We give our clients five days with a potential pup to get to know each other."
    ds "If, after those five days are up, it doesn't work out, then you are free to bring them back!"
    ds "But, if all goes well, you'll gain a lifelong friend to stand by your side and love you no matter what."

    # A dog was picked
    # This is their image
    image dogImage = "dogs/[dog.name].png"

    $ days = 0
    $ day_done = []
    if len(day_done) < 5:
        jump new_day
    else:
        jump end_true

label new_day:
    $ days += 1 
    scene outsideHouse

    if days == 1:
        "Today's my first day with [dog.name]. Maybe I should try to get [dog.name] to be more comfortable with me."
    elif days == 2:
        "Today's my second day with [dog.name]. I think I should try to get to know [dog.name] a little better."
    elif days == 3:
        "Today's my third day with [dog.name]. I feel like I know more about [dog.name] now."
    elif days == 4:
        "Today's my fourth day with [dog.name]. I only have 2 days left with [dog.name]. I should try to get [dog.name] to like to me more."
    elif days == 5:
        "Today's my last day with [dog.name]. I'll be going to the dog shelter tomorrow. I need to make today count!"

    "What should I do today?"
    menu:
        "Go to the park." if not "park" in day_done:
            $ day_done.append("park")
            jump park_start
        "Go shopping." if not "shopping" in day_done:
            $ day_done.append("shopping")
            jump shopping_start
        "Take a walk." if not "walk" in day_done:
            $ day_done.append("walk")
            jump walk_start
        "Stay at home." if not "home" in day_done:
            $ day_done.append("home")
            jump home_start
        "Nothing else!":
<<<<<<< Updated upstream
            "end: dog [dog.traits.training], kindness [owner.traits.kindness], loyalty [owner.traits.loyalty], patience [owner.traits.patience], discipline [owner.traits.discipline]"
            jump end_true

=======
            "nice demo end - dog [dog.traits.training]"
            "kindness [owner.traits.kindness]"
            "loyalty [owner.traits.loyalty]"
            "patience [owner.traits.patience]"
            "discipline [owner.traits.discipline]"
            jump end_determiner
>>>>>>> Stashed changes

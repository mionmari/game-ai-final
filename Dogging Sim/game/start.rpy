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

    # Intialize variables
    owner = Owner()
    days = 0
    day_done = []
    training = 0

# NEEDS A START LABEL
label start:
    $owner = Owner()
    $days = 0
    $day_done = []
    $training = 0

    # Load all background images
    image dogShelter = "scenes/dog shelter.png"
    image dogPark = "scenes/dog park.png"
    image home = "scenes/home.png"
    image petStore = "scenes/pet store.png"
    image petCoo = "scenes/petcoo.png"
    image outsideHouse = "scenes/outside house.png"
    image walkPath = "scenes/walk path.png"
    image shopping = "scenes/shopping.png"

    # Load dog cards
    image buddyCard = "images/dog_cards/buddy_card.png"
    image daisyCard = "images/dog_cards/daisy_card.png"
    image dukeCard =  "images/dog_cards/duke_card.png"
    image lionCard = "images/dog_cards/lion_card.png"
    image lupinCard = "images/dog_cards/lupin_card.png"
    image rascalCard = "images/dog_cards/rascal_card.png"
    image sausageCard = "images/dog_cards/sausage_card.png"
    image teddyCard = "images/dog_cards/teddy_card.png"

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

    ds "We have 8 lovable dogs available for adoption. Who would you like to bring home?"

    jump dog_menu1

label dog_menu1:
    menu:
        "Lupin":
            show lupinCard
            ds "Ooh, yes Lupin is a very good boy! He's full of energy, but can get a bit clingy at times."
            ds "Will you adopt Lupin?"
            menu:
                "Yes, I want to pick Lupin.":
                    $dog = dogs[0]
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide lupinCard
                    jump dog_menu1       
        "Rascal":
            show rascalCard
            ds "Rascal is the CUTEST DOG!! He likes cuddles and long naps. Do be careful, though, sometimes he can get a bit moody."
            ds "Will you adopt Rascal?"
            menu:
                "Yes, I want to pick Rascal.":
                    $dog = dogs[1]
                    hide rascalCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide rascalCard
                    jump dog_menu1
        "Buddy":
            show buddyCard
            ds "Aww, Buddy is such a good girl! She looooves to eat, and gets a little upset if she hasn't eaten."
            ds "Will you adopt Buddy?"
            menu:
                "Yes, I want to pick Buddy.":
                    $dog = dogs[2]
                    hide buddyCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide buddyCard
                    jump dog_menu1    
        "Lion":
            show lionCard
            ds "Lion is a great dog!! She's is a bit of a diva and can get very attached to you!"
            ds "Will you adopt Lion?"
            menu:
                "Yes, I want to pick Lion.":
                    $dog = dogs[3]
                    hide lionCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide lionCard
                    jump dog_menu1
        "Show me more dogs":
            jump dog_menu2   
label dog_menu2:
    menu:
        "Duke":
            show dukeCard
            ds "Duke is the nicest dog!! He's got so much energy and eats a lot!"
            ds "Will you adopt Duke?"
            menu:
                "Yes, I want to pick Duke.":
                    $dog = dogs[4]
                    hide dukeCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide dukeCard
                    jump dog_menu2   
        "Sausage":
            show sausageCard
            ds "Sausage is our most well-behaved dogs! He's a sweetheart all-around!!"
            ds "Will you adopt Sausage?"
            menu:
                "Yes, I want to pick Sausage.":
                    $dog = dogs[5]
                    hide sausageCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide sausageCard
                    jump dog_menu2 
        "Teddy":
            show teddyCard
            ds "Okay, so Teddy is also the cutest dog!! She's got the most energy a small dog can ever get!"
            ds "Will you adopt Teddy?"
            menu:
                "Yes, I want to pick Teddy.":
                    $dog = dogs[6]
                    hide teddyCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide teddyCard
                    jump dog_menu2 
        "Daisy":
            show daisyCard
            ds "Daisy is our most expressive dog! He is very well-trained but can get a little moody."
            ds "Will you adopt Daisy?"
            menu:
                "Yes, I want to pick Daisy.":
                    $dog = dogs[7]
                    hide daisyCard
                    jump dog_picked
                "Hmm, not sure... Show me other dogs first.":
                    hide daisyCard
                    jump dog_menu2 
        "Show me the other dogs again":
            jump dog_menu1   


label dog_picked:
    python:
        # Evaluate pronouns
        objPronoun = obj[dog.sex]
        subjPronoun = subj[dog.sex]
        subjPronoun_upper = subjPronoun.capitalize()
        possPronoun = poss[dog.sex]
        possPronoun_upper = possPronoun.capitalize()
        reflPronoun = refl[dog.sex]
        personPronoun = person[dog.sex]
        d = Character(dog.name)
        training = dog.traits.training

    image dogImage = "dogs/[dog.name].png"
    
    ds "Great choice! I hope you and [dog.name] get along well! See you in 5 days."

    jump new_day


label new_day:
    $ days += 1 
    
    if days > 5:
        jump end_determiner

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
        "Should I go somewhere that [dog.name] likes or somewhere that trains [dog.name] well?"
        $day_done = []

    jump action_menu

label action_menu:
    
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
        "Return to dog shelter.":
            "Are you sure you want to return [dog.name] to the shelter?"
            $days_remaining = (5 - days) + 1
            "You still have [days_remaining] day(s) to spend time with [objPronoun]."
            menu:
                "[dog.name]'s training level: [training] \nYour traits: kindness [owner.traits.kindness], loyalty [owner.traits.loyalty], patience [owner.traits.patience], discipline [owner.traits.discipline]"
                "Yes":
                    jump end_determiner
                "No":
                    jump action_menu


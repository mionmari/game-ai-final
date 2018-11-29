# SHOPPING FILE
# TODO: IMPLEMENT MONEY ($50 OR SO?)
# TODO: SPECIFIC BEHAVIOR FOR EACH MENU ITEM, MORE MENU ITEMS

# SHOPPING INTRO
label shopping_start:
    python:
        shopping_done = []
        shopping_petcoo_done = []
        shopping_yummy_done = []
        petcoo_employee = Character("Part-Time PetCoo Employee")
        yummy_employee = Character("Yummy Bone Employee")
        grocery_employee = Character("OK-Mart Employee")

    "You decide to do a little shopping today for some doggy goods. You don't really have anything better to do!"
    p "Wanna pick up some stuff? Come with me, I wanna see how you like them."
    d "Woof!"

    jump shopping_menu_start

label shopping_menu_start:
    "Which store would you like to go to first?"
    menu:
        "PetCoo, a retail chain pet supply store.":
            $ shopping_done.append("petcoo")
            jump shopping_petcoo
        "Yummy Bone, a smaller pet supply store down the street.":
            $ shopping_done.append("yummy")
            jump shopping_yummy
        "OK-Mart, the local grocery store.":
            $ shopping_done.append("grocery")
            jump shopping_grocery

label shopping_menu:
    "Which store would you like to go to next?"
    menu:
        "PetCoo, a retail chain pet supply store." if not "petcoo" in shopping_done:
            $ shopping_done.append("petcoo")
            jump shopping_petcoo
        "Yummy Bone, a smaller pet supply store down the street." if not "yummy" in shopping_done:
            $ shopping_done.append("yummy")
            jump shopping_yummy
        "OK-Mart, the local grocery store." if not "grocery" in shopping_done:
            $ shopping_done.append("grocery")
            jump shopping_grocery
        "You think you're done shopping for today!":
            jump shopping_end

label shopping_petcoo:
    "You walk into PetCoo and are immediately greeted by a harmony of zealous employees."
    petcoo_employee "Hey, welcome to PetCoo!!! How can I help you today?? Are you looking for something in particular? Your dog is so cute!!"
    if dog.traits.social <= 2:
        "[dog.name] gets scared and bolts out the doorway!"
        p "Hey! It's okay, #GIRL!"
        petcoo_employee "Oh my god, I'm so sorry! It's my first day here, and-"
        "You are pulled out the door by the leash. [dog.name] makes it a little bit down the block before #SHE hides behind a trash can, shivering."
        p "It's okay, come on. Let's get to a different shop!"
        jump shopping_menu
    else:
        p "No, just browsing today, thank you."
        jump shopping_petcoo_menu

label shopping_petcoo_menu:
    "What would you like to look at?"
    menu:
        "A brand new squeaky chew toy." if not "chew" in shopping_petcoo_done:
            $ shopping_petcoo_done.append("chew")
            if dog.traits.passAggress >= 3:
                "[dog.name] gnashes viciously into the chew toy!"
            else:
                "[dog.name] sniffs the chew toy and plays with it a little. #SHE doesn't seem entirely impressed, though"
        "Some super expensive dog treats." if not "treats" in shopping_petcoo_done:
            $ shopping_petcoo_done.append("treats")
            if dog.traits.gluttony >= 4:
                "[dog.name] tries to knock the whole jar out of your hand."
                p "Whoah there!! Bad #GIRL!"
                petcoo_employee "Careful not to feed #HER too much... They can really get attached to treats."
                p "I'll keep that in mind."
            else:
                "[dog.name] seems to love the new treats a lot!!!"
                d "{i}Arf! Arf! Arf!{/i}"
        "Nothing else interests you here at PetCoo.":
            "You thank the employees and take your leave."
            jump shopping_menu
    jump shopping_petcoo_menu

label shopping_yummy:
    "You walk into Yummy Bone and are greeted by an elderly woman at the counter."
    yummy_employee "Welcome to the store, dearie!! What would you like?"
    p "Oh, I'm just browsing-"
    yummy_employee "Not you, the dog! Come here, dearie."
    if dog.traits.social <= 2:
        "[dog.name] seems apprehensive of the woman, until she walks over and holds out a treat in her hand."
        "[dog.name] licks the treat out of the employee's hand."
        yummy_employee "You sometimes have to treat them very, very gently. Now you can both browse comfortably!"
        jump shopping_yummy_menu
    else:
        "The woman reaches down and pets [dog.name]."
        yummy_employee "Let me know if you need anything!"
        jump shopping_petcoo_menu

label shopping_yummy_menu:
    "What would you like to look at?"
    menu:
        "A large, round stuffed hamster." if not "hamster" in shopping_yummy_done:
            $ shopping_yummy_done.append("hamster")
            if dog.traits.passAggress <= 2:
                "[dog.name] lovingly hugs the plush hamster. #SHE seems to really love it."
            else:
                "[dog.name] doesn't seem entirely impressed."
        "A very large, fluffy dog bed." if not "bed" in shopping_yummy_done:
            $ shopping_yummy_done.append("bed")
            d "{i}Arf! Arf! Arf!{/i}"
            "[dog.name] lies down into the bed, snuggling #HER snout deep into the fuzz."
            if dog.traits.energy <= 2:
                "[dog.name] falls asleep."
                yummy_employee "Aww, what a sweet child!! Here, if you'd like it, I'll give you a special discount."
                "The lady takes out a camera and takes a picture of [dog.name] sleeping."
                "After a little while, [dog.name] eventually comes to."
            else:
                "It seems like #SHE really likes it!"
        "Nothing else interests you here at Yummy Bone.":
            "You thank the employees and take your leave."
            jump shopping_menu
    jump shopping_yummy_menu

label shopping_grocery:
    "You get a little ways into the store before an employee notices."
    grocery_employee "Excuse me!! No pets in the store, please! It's company policy- we have a lot of food items out in the open."
    if dog.traits.gluttony >= 4:
        "[dog.name] appears to smell something good in the store, and tries to push #HER way in."
        p "I'm sorry!!"
        "You manage to shove [dog.name] back out the door with a little effort."
        grocery_employee "It's... it's no problem."
    else:
        p "Oh, I never knew that..."
        "You learn a lot about where you can go with dogs when you actually have one with you."
    jump shopping_menu

label shopping_end:
    "I guess that's enough stuff you picked up!"
    jump new_day
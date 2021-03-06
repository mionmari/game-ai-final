# SHOPPING FILE
# TODO: IMPLEMENT MONEY ($50 OR SO?)
# TODO: SPECIFIC BEHAVIOR FOR EACH MENU ITEM, MORE MENU ITEMS

# SHOPPING INTRO
label shopping_start:
    play music "Road_to_Moscow.mp3" fadeout 1
    scene shopping
    python:
        shopping_done = []
        shopping_petcoo_done = []
        shopping_yummy_done = []
        petcoo_employee = Character("Part-Time PetCoo Employee")
        yummy_employee = Character("Yummy Bone Employee")
        grocery_employee = Character("OK-Mart Employee")
        puppy = Character("Curious Puppy")
    image petcooeImg = "images/npcs/petcoo_employee.png"
    image yummyeImg = "images/npcs/yummy_employee.png"
    image groceryeImg = "images/npcs/grocery_employee.png"
    image puppyImg = "images/npcs/puppy.png"

    "You decide to do a little shopping today for some doggy goods. You don't really have anything better to do!"
    p "Wanna pick up some stuff? Come with me, I wanna see how you like them."
    show dogImage
    d "Woof!"
    hide dogImage

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
    scene shopping
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
    scene petcoo
    "You walk into PetCoo and are immediately greeted by a harmony of zealous employees."
    show petcooeImg
    petcoo_employee "Hey, welcome to PetCoo!!! How can I help you today?? Are you looking for something in particular? Your dog is so cute!!"
    hide petcooeImg
    if dog.traits.social <= 2:
        "[dog.name] gets scared and bolts out the doorway!"
        p "Hey! It's okay, [personPronoun]!"
        show petcooeImg
        petcoo_employee "Oh my god, I'm so sorry! It's my first day here, and-"
        hide petcooeImg
        "You are pulled out the door by the leash. [dog.name] makes it a little bit down the block before [subjPronoun] hides behind a trash can, shivering."
        
        menu:
            "Coax [dog.name] to go inside Petcoo.":
                $ owner.traits.patience += 1
                $ if owner.traits.patience > 5: owner.traits.patience = 5
                p "Ssssh, hey it's alright now."
                show dogImage
                d "*whimper*"
                hide dogImage
                p "It'll be alright buddy, let's make our way inside."

                jump shopping_petcoo_menu
            "Go to a different store.":
                $ owner.traits.kindness += 1
                $ if owner.traits.kindness > 5: owner.traits.kindness = 5
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
            $ owner.traits.kindness += 1
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
            if dog.traits.passAggress >= 3:
                "[dog.name] gnashes viciously into the chew toy!"
                menu:
                    "Sternly scold [dog.name]":
                        p "No!!! Bad [personPronoun]!"
                        show petcooeImg
                        petcoo_employee "Um..."
                        hide petcooeImg
                        "Looks like you have to buy the chew toy now."
                        $ owner.traits.discipline += 1
                        $ if owner.traits.discipline > 5: owner.traits.discipline = 5
                    "Quietly warn [dog.name]":
                        p "No, [dog.name]. That's not good."                        
                        $ owner.traits.patience += 1
                        $ if owner.traits.patience > 5: owner.traits.patience = 5
                $ training += 0.5
                $ if training > 5: training = 5
            elif dog.traits.energy >= 4:
                "[dog.name] bounces around excitedly as you give [objPronoun] the toy."
                show dogImage
                d "Woof! Woof!"
                hide dogImage
                "[dog.name] does a backflip! 10 out of 10."
                p "Wow you {i} really {\i} like this toy!"
                "[dog.name] runs away with the chew toy."
                menu: 
                    "Wait for [dog.name] to get tired.":
                        "[dog.name] eventually calms back and returns the toy."
                        $ owner.traits.patience += 1
                        $ if owner.traits.patience > 5: owner.traits.patience = 5
                    "Chase after [dog.name].":
                        p "Hey!! Wait!!"
                        "After much running, you catch up to [dog.name] and..."
                        menu:
                            "Chastise [objPronoun]":
                                "Bad [personPronoun]! Don't run off without me!"
                                show dogImage
                                d "*whine*"
                                hide dogImage
                                $ owner.traits.discipline += 1
                                $ if owner.traits.discipline > 5: owner.traits.discipline = 5
                            "Trade the toy for a treat.": 
                                "[dog.name] proudly returns the toy."
                                $ owner.traits.kindness += 1
                                $ if owner.traits.kindness > 5: owner.traits.kindness = 5
                $ training += 0.5
                $ if training > 5: training = 5

            else:
                "[dog.name] sniffs the chew toy and plays with it a little. [subjPronoun_upper] doesn't seem entirely impressed, though."
                p "Well... it was work a shot."
        "Free samples of some super expensive dog treats." if not "treats" in shopping_petcoo_done:
            $ shopping_petcoo_done.append("treats")
            
            show petcooeImg
            petcoo_employee "Hey there, wanna try some treats? ...for your dog of course!"
            hide petcooeImg
            if dog.traits.gluttony >= 4:
                "[dog.name] tries to knock the treat out of your hand."
                menu:
                    "Scold [objPronoun]":
                        p "Whoah there!! Bad [personPronoun]!"
                        $ owner.traits.discipline += 1
                        $ if owner.traits.discipline > 5: owner.traits.discipline = 5
                    "Don't":
                        "You pick up the treat that fell on the floor."
                        show petcooeImg
                        petcoo_employee "Careful not to feed [objPronoun] too much... They can really get attached to treats."
                        hide petcooeImg
                        p "I'll keep that in mind."            
                        $ owner.traits.kindness += 1
                        $ if owner.traits.kindness > 5: owner.traits.kindness = 5
                $ training += 0.5
                $ if training > 5: training = 5
            else:
                "[dog.name] seems to love the new treats a lot!!!"
                show dogImage
                d "{i}Arf! Arf! Arf!{/i}"
                hide dogImage
        "Check out the puppy window." if not "puppyWindow" in shopping_petcoo_done:
             $ shopping_petcoo_done.append("puppyWindow")
             "Let's check out the puppies, [dog.name]!"
             show dogImage
             d "Woof?" 
             hide dogImage
             show puppyImg
             "A small puppy comes close to the glass. It stares curiously at [dog.name]."
             hide puppyImg
             p "Wow, I think this one likes you, [dog.name]."
             if dog.traits.jealousy >= 4:
                "[dog.name] looks completely disinterested and tries to pull you away from the glass."   
                menu:
                    "Continue interacting with puppy.":
                        p "Hmm, what was that puppy? Oh yes, see [dog.name] doesn't like to meet new dogs."
                        show dogImage
                        d "*annoyed bark*"
                        hide dogImage
                        $ owner.traits.discipline += 1
                        $if owner.traits.discipline > 5: owner.traits.discipline = 5
                    "Try to get [dog.name] to play with puppy.":
                        p "Look, this is [dog.name]. [dog.name] say \"hi\"!"  
                        show dogImage
                        d "Bark! Bark!"
                        hide dogImage
                        p "Haha, okay, I'm done."
                        $ owner.traits.kindness += 1
                        $if owner.traits.kindness > 5: owner.traits.kindness = 5
                    "Look at something else.":
                        "[dog.name] looks content."
                        $ owner.traits.loyalty += 1
                        $ if owner.traits.loyalty > 5: owner.traits.loyalty = 5
                $ training += 0.5
                $ if training > 5: training = 5
             else:
                if dog.traits.passAggress >= 4:                    
                    "[dog.name] looks up and down at the puppy."
                    show puppyImg
                    puppy "Arf?"                    
                    hide puppyImg
                    show dogImage
                    d "{i} Hiss! {/i}"
                    hide dogImage
                    show puppyImg
                    puppy "{b} *whimper* {/b}"
                    hide puppyImg
                    "You pull [dog.name] away before [subjPronoun] alerts the other employees."
                    p "Sigh... [dog.name] when will you learn?"
                else:
                    "[dog.name] looks pretty interested in the puppy."
                    show dogImage
                    d "Bark! Bark!"
                    show puppyImg at right
                    puppy "Arf!"
                    hide puppyImg
                    hide dogImage
                    "[dog.name] runs around in a circle and wags [possPronoun] tail playfully."
                    "You and [dog.name] feel warm and fuzzy inside."
        "Nothing else interests you here at PetCoo.":
            "You thank the employees and take your leave."
            jump shopping_menu
    jump shopping_petcoo_menu

label shopping_yummy:
    scene petStore
    "You walk into Yummy Bone and are greeted by an elderly woman at the counter."
    show yummyeImg
    yummy_employee "Welcome to the store, dearie!! What would you like?"
    hide yummyeImg
    p "Oh, I'm just browsing-"    
    show yummyeImg
    yummy_employee "Not you, the dog! Come here, dearie."
    hide yummyeImg

    if dog.traits.social <= 2:
        "[dog.name] seems apprehensive of the woman, until she walks over and holds out a treat in her hand."
        "[dog.name] licks the treat out of the employee's hand."
        show yummyeImg
        yummy_employee "You sometimes have to treat them very, very gently. Now you can both browse comfortably!"
        hide yummyeImg
        jump shopping_yummy_menu
    else:
        "The woman reaches down and pets [dog.name]."
        show yummyeImg
        yummy_employee "Let me know if you need anything!"
        hide yummyeImg
        jump shopping_yummy_menu

label shopping_yummy_menu:
    "What would you like to look at?"
    menu:
        "A large, round stuffed hamster." if not "hamster" in shopping_yummy_done:
            $ shopping_yummy_done.append("hamster")
            if dog.traits.passAggress <= 2:
                "[dog.name] lovingly hugs the plush hamster. [subjPronoun_upper] seems to really love it."
                show dogImage
                d "Woof!"
                hide dogImage
            else:
                "[dog.name] looks ready to rip the stuffed hamster into shreds."
                "You quickly put back the toy on the shelf."
        "A very large, fluffy dog bed." if not "bed" in shopping_yummy_done:
            $ shopping_yummy_done.append("bed")
            show dogImage
            d "{i}Arf! Arf! Arf!{/i}"
            hide dogImage
            "[dog.name] lies down into the bed, snuggling [possPronoun] snout deep into the fuzz."
            if dog.traits.energy <= 2:                
                "[dog.name] immediately falls asleep."
                menu: 
                    "Wake [dog.name] up. The employee might think we're going to buy the bed.":
                        "Hey, c'mon [dog.name] we can't sleep here. It's not ours."
                        show dogImage
                        d "Woof?"
                        hide dogImage
                        $ owner.traits.discipline += 1
                        $ if owner.traits.discipline > 5: owner.traits.discipline = 5
                    "Let [dog.name] sleep. [subjPronoun_upper] looks exhausted.":
                        show yummyeImg
                        yummy_employee "Aww, what a sweet child!! Here, if you'd like it, I'll give you a special discount."
                        hide yummyeImg
                        "The lady takes out a camera and takes a picture of [dog.name] sleeping."
                        "After a little while, [dog.name] eventually comes to."
                        $ owner.traits.kindness += 1
                        $ if owner.traits.kindness > 5: owner.traits.kindness = 5
                        $ owner.traits.patience += 1
                        $ if owner.traits.patience > 5: owner.traits.patience = 5
                $ training += 0.5
                $ if training > 5: training = 5
            else:
                "It seems like [subjPronoun] really likes it!"
                if training < 3:
                    "[dog.name] has a suspicious glimmer in [possPronoun] eyes. You have a weird feeling that [dog.name] might do something bad."
                    menu:
                        "Ignore. [dog.name] is just being playful.":
                            "You shrug off your suspicions. After all, [dog.name] just used the bathroom before coming inside the store."
                            p "Hey! Wait!"
                            "[dog.name] rolls over with [possPronoun] stomach exposed."
                            p "Hmm... so you just wanted belly rubs, huh?"
                            show dogImage
                            d "Yip!"
                            hide dogImage
                            $ owner.traits.patience += 1
                            $ if owner.traits.patience > 5: owner.traits.patience = 5
                        "Remove [dog.name] from bed.":
                            "You quickly scoop up [dog.name] and take her outside before [subjPronoun] can do [possPronoun] business."
                            $ owner.traits.discipline += 1
                            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
                    p "Phew, that was a close one."

        "Yummy Bone™ dog food." if not "food" in shopping_yummy_done:
            $ shopping_yummy_done.append("food")
            show yummyeImg
            yummy_employee "Ooh! Yes, we do sell your favorite dog food brands, but we also sell our own organic dog mix! Want to try a sample?"
            hide yummyeImg
            "[dog.name] looks at you expectantly."
            menu:
                "Sure, we'd like to try!":
                    p "Definitely!"
                    if dog.traits.gluttony >= 4:
                        "As soon as the employee finishes pouring out the sample, [dog.name] has already eaten all of it."
                        show yummyeImg
                        yummy_employee "Aww, do you want more?"
                        hide yummyeImg
                        show dogImage
                        d "Arf!"
                        hide dogImage
                        show yummyeImg
                        yummy_employee "Sorry, this is all we're allowed to give per customer... But since you're so sweet, I'll give you a little extra {b} *wink* {\b}."
                        hide yummyeImg
                        "[dog.name] runs around in circles."
                    else:
                        "[dog.name] patiently waits for the employee to finish pouring before starting to eat."
                        p "Does it taste good?"
                        show dogImage
                        d "Woof!"
                        hide dogImage
                    $ owner.traits.kindness += 1
                    $ if owner.traits.kindness > 5: owner.traits.kindness = 5
                "Nope, [dog.name] has eaten too much today.":
                    p "Thanks, but no thanks. [dog.name] ate way too much already."
                    "[dog.name] flashes you a look of betrayal."
                    show yummyeImg
                    yummy_employee "Aww, okay. Maybe next time."
                    hide yummyeImg
                    $ owner.traits.discipline += 1
                    $ if owner.traits.discipline > 5: owner.traits.discipline = 5

        "Nothing else interests you here at Yummy Bone.":
            "You thank the employees and take your leave."
            jump shopping_menu
    jump shopping_yummy_menu

label shopping_grocery:
    "You get a little ways into the store before an employee notices."
    show groceryeImg
    grocery_employee "Excuse me!! No pets in the store, please! It's company policy- we have a lot of food items out in the open."
    hide groceryeImg
    if dog.traits.gluttony >= 4:
        "[dog.name] appears to smell something good in the store, and tries to push [possPronoun] way in."
        p "I'm sorry!!"
        "You manage to shove [dog.name] back out the door with a little effort."
        show groceryeImg
        grocery_employee "It's... it's no problem."
        hide groceryeImg
    else:
        p "Oh, I never knew that..."
        "You learn a lot about where you can go with dogs when you actually have one with you."
    jump shopping_menu

label shopping_end:
    "I guess that's enough stuff you picked up!"
    jump new_day
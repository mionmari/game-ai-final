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
        puppy = Character("Curious Puppy")

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
        p "Hey! It's okay, [personPronoun]!"
        petcoo_employee "Oh my god, I'm so sorry! It's my first day here, and-"
        "You are pulled out the door by the leash. [dog.name] makes it a little bit down the block before [subjPronoun] hides behind a trash can, shivering."
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
                p "No!! Bad [personPronoun]!"
                petcoo_employee "Um..."
                "Looks like you have to buy the chew toy now."
            elif dog.traits.energy >= 3:
                "[dog.name] runs around excitedly as you give [objPronoun] the toy."
                d "Woof! Woof!"
                "[dog.name] does a backflip! 10 out of 10!"
                p "Woah! You {i} really {/i} like this!"
                $if owner.traits.kindness < 5: owner.traits.kindness += 0.5
            else:
                "[dog.name] sniffs the chew toy and plays with it a little. [subjPronoun] doesn't seem entirely impressed, though."
                p "Well... it was work a shot."
        "Some super expensive dog treats." if not "treats" in shopping_petcoo_done:
            $ shopping_petcoo_done.append("treats")
            if dog.traits.gluttony >= 4:
                "[dog.name] tries to knock the whole jar out of your hand."
                p "Whoah there!! Bad [personPronoun]!"
                petcoo_employee "Careful not to feed [objPronoun] too much... They can really get attached to treats."
                p "I'll keep that in mind."
            else:
                "[dog.name] seems to love the new treats a lot!!!"
                d "{i}Arf! Arf! Arf!{/i}"
                p "Aww, so cute!"
                $if owner.traits.kindness < 5: owner.traits.kindness += 0.5
        "Check out the puppy window." if not "puppyWindow" in shopping_petcoo_done:
             $ shopping_petcoo_done.append("puppyWindow")
             "Let's check out the puppies, [dog.name]!"
             d "Woof?" 
             "A small puppy comes close to the glass. It stares curiously at [dog.name]."
             p "Wow, I think this one likes you, [dog.name]."
             if dog.traits.jealousy >= 3:
                menu:
                    "Try to get [dog.name] to play with puppy.":
                        p "Look, this is [dog.name]. [dog.name] say \"hi\"!"
                        "[dog.name] looks a completely disinterested and tries to pull you away from the glass."     
                        d "Bark! Bark!"
                        p "Haha, okay, I'm done."
                        $if owner.traits.patience < 5: owner.traits.patience += 0.5
                    "Look at something else.":
                        "[dog.name] looks pleased."
                        $if owner.traits.loyalty < 5: owner.traits.loyalty += 0.5
             else:
                if dog.traits.passAggress >= 3:                    
                    "[dog.name] looks up and down at the puppy."
                    puppy "Arf?"
                    d "{i} Hiss! {/i}"
                    puppy "{b} *whimper* {/b}"
                    menu:
                        "Scold [dog.name].":
                            p "Hey! That wasn't nice!"
                            if dog.traits.training < 3:
                                "[dog.name] starts hissing at you now."
                            else:
                                "[dog.name]'s tail droops."
                            $if owner.traits.discipline < 5: owner.traits.discipline += 0.5
                        "Handle the situation quietly.":
                            "You pull [dog.name] away before [subjPronoun] alerts the other employees."
                            $if owner.traits.patience < 5: owner.traits.patience += 0.5
                    p "Sigh... [dog.name] when will you learn?"
                else:
                    "[dog.name] looks pretty interested in the puppy."
                    d "Bark! Bark!"
                    puppy "Arf!"
                    "[dog.name] runs around in a circle and wags [possPronoun] tail playfully."
                    "You and [dog.name] feel warm and fuzzy inside."
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
        jump shopping_yummy_menu

label shopping_yummy_menu:
    "What would you like to look at?"
    menu:
        "A large, round stuffed hamster." if not "hamster" in shopping_yummy_done:
            $ shopping_yummy_done.append("hamster")
            if dog.traits.passAggress <= 2:
                "[dog.name] lovingly hugs the plush hamster. [subjPronoun] seems to really love it."
                d "Woof!"
                $if owner.traits.kindness < 5: owner.traits.kindness += 0.5
            else:
                "[dog.name] looks ready to rip the stuffed hamster into shreds."
                menu:
                    "Tell [dog.name] to behave.":
                        "Hey, hey! [dog.name], behave yourself!"
                        d "Snarl."
                    "Put it away.":
                        "You quickly put back the toy on the shelf."
                "[dog.name] walks away, disinterested."
                $if owner.traits.discipline < 5: owner.traits.discipline += 0.5
        "A very large, fluffy dog bed." if not "bed" in shopping_yummy_done:
            $ shopping_yummy_done.append("bed")
            d "{i}Arf! Arf! Arf!{/i}"
            "[dog.name] lies down into the bed, snuggling [possPronoun] snout deep into the fuzz."
            if dog.traits.energy <= 2:
                "[dog.name] falls asleep."
                menu: 
                    "Wake [dog.name] up. The employee might think we're going to buy the bed.":
                        "Hey, c'mon [dog.name] we can't sleep here. It's not ours."
                        d "Woof?"
                        $if owner.traits.discipline < 5: owner.traits.discipline += 0.5
                    "Let [dog.name] sleep. [subjPronoun] looks exhausted.":
                        yummy_employee "Aww, what a sweet child!! Here, if you'd like it, I'll give you a special discount."
                        "The lady takes out a camera and takes a picture of [dog.name] sleeping."
                        "After a little while, [dog.name] eventually comes to."
                        $if owner.traits.kindness < 5: owner.traits.kindness += 0.5
                        $if owner.traits.patience < 5: owner.traits.patience += 0.5
            else:
                "It seems like [subjPronoun] really likes it!"
                if dog.traits.training < 3:
                    "[dog.name] has a suspicious glimmer in [possPronoun] eyes. You have a weird feeling that [dog.name] might drop a log in the bed."
                    menu:
                        "Ignore. [dog.name] is just being playful.":
                            "You shrug off your suspicions. After all, [dog.name] just used the bathroom before coming inside the store."
                            p "Hey! Wait!"
                            "[dog.name] rolls over with [possPronoun] stomach exposed."
                            p "Hmm... so you just wanted belly rubs, huh?"
                            d "Yip!"
                            $if owner.traits.patience < 5: owner.traits.patience += 0.5
                        "Remove [dog.name] from bed.":
                            "You quickly scoop up [dog.name] and take her outside before [subjPronoun] can do [possPronoun] business."
                            $if dog.traits.training < 5: dog.traits.training += 0.5;
                            $if owner.traits.discipline < 5: owner.traits.discipline += 0.5
                    p "Phew, that was a close one."

        "Yummy Bone™ dog food." if not "food" in shopping_yummy_done:
            $ shopping_yummy_done.append("food")
            yummy_employee "Ooh! Yes, we do sell your favorite dog food brands, but we also sell our own organic dog mix! Want to try a sample?"
            "[dog.name] looks at you expectantly."
            menu:
                "Sure, we'd like to try!":
                    p "Definitely!"
                    if dog.traits.gluttony >= 4:
                        "As soon as the employee finishes pouring out the sample, [dog.name] has already eaten all of it."
                        yummy_employee "Aww, do you want more?"
                        d "Arf!"
                        yummy_employee "Sorry, this is all we're allowed to give per customer... But since you're so sweet, I'll give you a little extra {b} *wink* {\b}."
                        "[dog.name] runs around in circles."
                    else:
                        "[dog.name] patiently waits for the employee to finish pouring before starting to eat."
                        p "Does it taste good?"
                        d "Woof!"
                    $if dog.traits.gluttony < 5: dog.traits.gluttony += 0.5
                "Nope, [dog.name] has eaten too much today.":
                    p "Thanks, but no thanks. [dog.name] ate way too much already."
                    "[dog.name] flashes you a look of betrayal."
                    yummy_employee "Aww, okay. Maybe next time."
                    $if owner.traits.discipline < 5: owner.traits.discipline += 0.5

        "Nothing else interests you here at Yummy Bone.":
            "You thank the employees and take your leave."
            jump shopping_menu
    jump shopping_yummy_menu

label shopping_grocery:
    "You get a little ways into the store before an employee notices."
    grocery_employee "Excuse me!! No pets in the store, please! It's company policy- we have a lot of food items out in the open."
    if dog.traits.gluttony >= 4:
        "[dog.name] appears to smell something good in the store, and tries to push [possPronoun] way in."
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
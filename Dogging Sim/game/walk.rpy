# TAKING A WALK FILE
# TODO: MORE THINGS DURING THE WALK

# WALK INTRO
label walk_start:
    scene walkPath
    $ walk_done = []
    $ cream = Character("Cream")

    p "Let's go for a little walk today, [dog.name]. Come see the neighborhood!"
    p "But... let's get a leash on you first, just in case."
    "You walk towards [dog.name] with the leash."

    if dog.traits.training <= 2 or dog.traits.social <= 2 or dog.traits.passAggress >= 4 or dog.traits.energy >= 4:
        if dog.traits.passAggress >= 4:
            "[dog.name] starts hissing at you."
        elif dog.traits.energy >= 4:
            "[dog.name] is too excited and keeps moving around."
        else:
            show dogImage
            d "Ruff!"
            hide dogImage
            "[dog.name] looks up at your imposing figure, and drops to the ground, putting [possPronoun] tail between [possPronoun] legs."
        menu:
            "Calmy put the collar on.":
                if dog.traits.passAggress >= 4:
                    "You slowly attach the collar onto [dog.name]."
                    show dogImage
                    d "Bark! Bark! Bark!"
                    hide dogImage
                    p "Ssssh... It's fine, trust me."
                elif dog.traits.energy >= 4:
                    p "Hey, hey [dog.name] look at me! Yes, that's it."
                    "You stroke [possPronoun] fur slowly."
                else:         
                    p "Don't worry, it's completely safe..."
                    "[dog.name] backs up slowly as you approach."
                    p "{i}Sigh...{/i} It's fine, I guarantee it!"
                "Eventually, you manage to calm [objPronoun] down enough to attach the collar."
                $ owner.traits.patience += 1
                $ if owner.traits.patience > 5: owner.traits.patience = 5
            "Give some treats.":
                if dog.traits.gluttony >= 3:
                    "[dog.name]'s ears perk up when [subjPronoun] sees you pull out a puppy snack."
                "With a couple dog treats in hand, you manage to calm [objPronoun] down enough to attach the collar."
                $ owner.traits.kindness += 1
                $ if owner.traits.kindness > 5: owner.traits.kindness = 5

    else:
        "[dog.name] waits patiently and politely for you to finish putting the leash on."
        p "Oooh, good [personPronoun]!"
        show dogImage
        d "Arf!"
        hide dogImage

    jump walk_menu_start

label walk_menu_start:
    "You walk out the door. Where would you like to go?"
    menu:
        "Go to the crepe stand.":
            $ walk_done.append("crepe")
            jump walk_crepe
        "Just wander around for some time.":
            $ walk_done.append("walk")
            jump walk_wander

label walk_menu:
    "What would you like to go next?"
    menu:
        "Go to the crepe stand." if not "crepe" in walk_done:
            $ walk_done.append("crepe")
            jump walk_crepe
        "Just wander around for some time." if not "walk" in walk_done:
            $ walk_done.append("walk")
            jump walk_wander
        "That's enough walking for today.":
            jump walk_end

label walk_crepe:
    "You make it to your favorite crepe stand."
    cream "Welcome to Cream's Scrumptious Crepes! Ooh, it's you again! And I see you have a furry friend with you. What would you like today?"
    menu:
        "Strawberry peanut butter crepe":
            jump walk_crepe_strawberry
        "Cheese-salmon crepe":
            jump walk_crepe_cheese
        "Chocolate-macadamia ice cream crepe":
            jump walk_crepe_chocolate

label walk_crepe_strawberry:
    cream "One strawberry peanut butter crepe coming right up! Now will you be sharing some with your dog today?"
    menu:
        "Yes.":
            cream "That's fine. Dogs can eat strawberries and peanut butter. I'll cut the strawberries extra thin for [objPronoun]!"
            p "Thank you!"
            "You feed a couple slices of peanut butter-covered strawberries to [dog.name]. [possPronoun_upper] tail wags happily."
            show dogImage
            d "Yip!"
            hide dogImage
            $ owner.traits.kindness += 0.5
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
        "No.":
            cream "Ooh, then I'd feel sorry for [objPronoun]. Here, let me get [objPronoun] a treat, so you can eat together!"
            "Cream reaches behind the counter and pulls out a nice-looking treat."
            show dogImage
            d "Woof! Woof!"
            hide dogImage
            $ owner.traits.discipline += 1
            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
    "You continue walking with your delicious, fruity crepe in hand. [dog.name] also seems highly satisfied."
    jump walk_menu

label walk_crepe_cheese:
    cream "One cheesy salmon crepe coming right up! Now will you be sharing some with your dog today?"
    menu:
        "Yes.":
            cream "That's fine, but be careful! Dogs can eat salmon, but can only eat cheese in moderation!!"
            p "Oh, thanks for the tip..."
            cream "Here, I'll give you a couple pieces of salmon. I think it's a beautiful thing when owner and doggo eat together."
            "You share a couple bits of salmon with [dog.name]."
            show dogImage
            d "Yip!"
            hide dogImage
            p "Delicious, isn't it? Thanks, Cream!"
            $ owner.traits.kindness += 0.5
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
        "No.":
            cream "Ooh, that's probably for the best; don't feed dogs too much cheese! Here, let me get [objPronoun] a treat, so you can eat together!"
            "Cream reaches behind the counter and pulls out a nice-looking treat."
            show dogImage
            d "Woof! Woof!"
            hide dogImage
            $ owner.traits.discipline += 1
            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
    "You continue walking with your filling, warm lunchtime crepe in hand. [dog.name] also seems happy."  
    jump walk_menu

label walk_crepe_chocolate:
    cream "One chocolate-macadamia ice cream crepe coming right up! Now will you be sharing some with your dog today?"
    menu:
        "Yes.":
            "Cream walks towards you with an ice cream scoop brandished in their right fist."
            cream ".excuse me."
            cream "..you're gonna."
            cream ".feed your dog.."
            cream ",,.,.,...,,a chocolate, macademia,,,, ice cream crepe."
            cream "DON'T YOU KNOW THAT CHOCOLATE CONTAINS THEOBROMINE, WHICH CAN BE HIGHLY TOXIC TO DOGS? THAT'S JUST COMMON SENSE! SO ARE MACADAMIA NUTS AND ICE CREAM. DO YOU WANT [objPronoun] TO HAVE HORRIFYING DIARRHEA ALL OVER YOUR BATHROOM FLOOR? DO YOU WANT [objPronoun] TO DIE? YOU ABSOLUTE MONSTER."
            cream "Please don't even joke about this kind of stuff. It's not funny!!"
            p "I... I got it, Cream. I'm sorry."
            "Cream stares daggers at you, and slowly hands over your crepe. As you walk, you feel the weight of your sins crawling down your back."
            $ owner.traits.kindness += 0.5
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
        "No.":
            cream "Good. [subjPronoun_upper] can't eat that stuff, you know! I feel bad for [objPronoun]. Be careful not to drop any."
            "Cream reaches behind the counter and pulls out a nice-looking treat."
            show dogImage
            d "Woof! Woof!"
            hide dogImage
            "You continue walking with your sweet crepe in hand."
            $ owner.traits.discipline += 1
            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
    jump walk_menu

label walk_wander:
    $ dog.traits.training += 1
    $ if dog.traits.training > 5: dog.traits.training = 5
    "It's a nice, warm day out. From time to time, the sun peeks out from behind the clouds."
    if dog.traits.energy <= 1:
        "[dog.name] slows down in the middle of the walk, panting a little."
        p "Aww... you're a little out of shape, aren't you?"
        show dogImage
        d "Whiiiine..."
        hide dogImage
        p "We'll get there. Both you and I."
    elif dog.traits.energy >= 4:
        "[dog.name] pulls you along a little faster than you're used to walking."
        p "Whoah there, [personPronoun]! You've got some energy in you!"
        show dogImage
        d "Ruff!"
        hide dogImage
        p "You rascal!! You wanna race?"
        "You make your way to a local park and begin jogging through it, [dog.name] right beside you."
        p "Phew.... I can barely keep up!!"
        show dogImage
        d "Ruff! Ruff!"
        hide dogImage
        "You spend some time running around, in perfect tandem, with [dog.name]. In fact, you start breathing heavily a little before [subjPronoun] does."
        "As the sun makes its way across the sky, you slow down gracefully into a walk."
        p "Huff.... that was fun, [dog.name]. Let's do that again sometime."
        show dogImage
        d "{i}Pants happily{/i}"
        hide dogImage
    else:
        "You make your way around the neighborhood, pointing out your favorite locations along the way."
        "[dog.name] appears to be enjoying [reflPronoun]. It's a nice, calming walk the whole way through."
        p "You like my town, [dog.name]?"
        "[subjPronoun_upper] looks back at you inquisitively."
        p "You'll learn to love it."
        "[subjPronoun_upper] turns around and keeps going."
    jump walk_menu

label walk_end:
    "It's been a long day, and both of you have done a lot of good walking."
    p "You know, [dog.name], all things considered, I'm glad you pulled me out of bed to take a walk with you today."
    show dogImage
    d "Woof!"
    hide dogImage
    
    jump new_day
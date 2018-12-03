# STAY HOME FILE
# TODO: MORE GAMES, DOG BREAKS SOMETHING

# HOME INTRO
label home_start:
    python:
        home_done = []
        tv_done = []
        cooking_host = Character("Cooking Host")

    "You decide to stay at home today. Hopefully, that'll give [dog.name] time to adjust!!"
    $if owner.traits.kindness < 5: owner.traits.kindness += 0.5 
    $if dog.traits.social <= 2 or dog.traits.jealousy >= 4: owner.traits.loyalty += 0.5

    if dog.traits.social <= 2:
        "You don't see [dog.name] anywhere."
        p "Hello? [dog.name]?"
        "No answer. You walk around the house, upturning furniture, until you see a fuzzy little paw under your bed."
        p "Hey there, [dog.name]... You're a shy little one, aren't you..."
        "You waggle a dog treat in front of [objPronoun] and manage to coax [objPronoun] out. You eventually lead [objPronoun] back to your kitchen."
    else:
        "You find [dog.name] sitting on your kitchen floor. You're pretty excited to get some quality time in!"

    jump home_menu_start

label home_menu_start:
    "You gather the supplies you have. What would you like to do?"
    menu:
        "Play the three-cup game with [dog.name]":
            $ home_done.append("cup")
            jump home_cup
        "Play tug-of-war with [objPronoun].":
            $ home_done.append("tug")
            jump home_tug
        "Petflix and chill.":
            $ home_done.append("tv")
            jump home_tv

label home_menu:
    "You gather the supplies you have. What would you like to do?"
    menu:
        "Play the three-cup game with [dog.name]" if not "cup" in home_done:
            $ home_done.append("cup")
            jump home_cup
        "Play tug-of-war with [objPronoun]." if not "tug" in home_done:
            $ home_done.append("tug")
            jump home_tug
        "Petflix and chill."if not "tv" in home_done:
            $ home_done.append("tv")
            jump home_tv
        "That's enough play for today.":
            jump home_end

label home_cup:
    "You remember a cute dog video you saw earlier. You gather three cups from the kitchen cabinet, and put them upside-down on the counter."
    "[dog.name] looks at you curiously, and sniffs the cups."
    p "Now watch carefully!"
    "You take out a dog treat and carefully place it under the left cup."
    if dog.traits.gluttony >= 3:
        d "Whiiiiine!"
        p "I'm going to switch up these cu-"
        "In a flash, [dog.name] nuzzles the cup over and snatches the treat up."
        p "You...."
        "[subjPronoun_upper] licks [possPronoun] lips contentedly."
        p "Let's try that again."
        "You place a treat under the cup and immediately start moving."

    menu:
        "Switch the cups around slowly.":
            "You slowly move the cup to the middle, then swap the outer cups, staring at [dog.name] the entire time."
            if dog.traits.energy >= 3:
                "[dog.name] immediately shoves [possPronoun] nose into the correct cup, sniffing a little."
                "[subjPronoun_upper] seems to know exactly what [subjPronoun] was doing, and whips [possPronoun] tail back and forth."
                jump home_cup_win
            elif r.random() < 0.7:
                jump home_cup_win
            else:
                jump home_cup_lose
        "Switch the cups around incredibly quickly.":
            "You shift the cups around rapidly, throwing in a flourish and a cup flip."
            if dog.traits.energy <= 2:
                "[dog.name] stares at you, and slowly places [possPronoun] paw on a cup."
                if r.random() < 0.3:
                    $ if dog.traits.training < 5: dog.traits.training += 0.5
                    jump home_cup_win
                else:
                    jump home_cup_lose
            elif r.random() < 0.3:
                $ if dog.traits.training < 5: dog.traits.training += 0.5
                jump home_cup_win
            else:
                jump home_cup_lose

label home_cup_win:
    "[dog.name] chooses the correct cup!"
    p "Good [personPronoun]! That's amazing!"
    d "Woof! Woof!!!"
    "You feed [objPronoun] another treat as a prize."
    $if owner.traits.kindness < 5: owner.traits.kindness += 0.5 
    jump home_menu

label home_cup_lose:
    "[dog.name] puts [objPronoun] paw on the wrong cup."
    p "Awww.... better luck next time..."
    "You reveal the dog treat under a different cup. [dog.name] gives you an incredibly sad stare."
    p "Well, thank you for playing..."
    "You give [objPronoun] a couple solemn pats as consolation."
    jump home_menu

label home_tug:
    "You get out some rope and tie a couple knots in it."
    p "[dog.name]? Come here!"
    "You hold out the rope next to [possPronoun] mouth."

    if dog.traits.gluttony >= 3:
        "[dog.name] immediately puts [possPronoun] teeth around the rope and starts chewing."
        p "That's it!"
    else:
        "With some encouragement, you manage to get [objPronoun] to grab on to the rope."

    p "Alright, let's do it!!"
    menu:
        "Tug the rope gently.":
            $if owner.traits.patience < 5: owner.traits.patience += 0.5 
            if dog.traits.passAggress >= 4:
                "[dog.name] notices you trying to take [possPronoun] rope away from [objPronoun]. [subjPronoun_upper] grabs the rope and runs away!"
                p "Good job!! Please come back!!!"
                "You chase [dog.name] across the house for a couple minutes, until you both get tired out."
            elif dog.traits.energy <= 1:
                "[dog.name] gently tugs back."
                "You feel a sense of bonding as you limply pass the rope back and forth."
                p "Mood."
            else:
                "[dog.name] manages to quickly yank the rope from your hands."
                p "Whoah there! Good [personPronoun]!!"
                d "Arf! Arf!"
                "You give [dog.name] a nice little treat."
        "Tug the rope hard.":
            if dog.traits.passAggress >= 4:
                "[dog.name] notices you trying to take [possPronoun] rope away from [objPronoun]. [subjPronoun_upper] pulls back with all [possPronoun] might, digging [possPronoun] feet into the ground."
                d "GRRRR!!!"
                menu:
                    "Let [objPronoun] win.":
                        "You begin to feel a little bad for [objPronoun]. You loosen your grip, and the rope flies out of your hands."
                        "[dog.name] stares at you intensely, saliva dripping from [possPronoun] jaw, grinning slightly."
                        p "{i}Sigh...{/i} Great work."
                        $if owner.traits.kindness < 5: owner.traits.kindness += 0.5 
                    "Keep pulling hard.":
                        "You continue tugging until you both get tired."
                        d "{i} Pant, pant. {\i}"
                        p "Ha... good work."
                        "It's a draw."
                        $if owner.traits.patience < 5: owner.traits.patience += 0.5 
                        $ if dog.traits.training < 5: dog.traits.training += 0.5
            elif dog.traits.energy <= 1:
                "The rope immediately flies out of [dog.name]'s mouth."
                p "Yeah, fair. Gotcha."
                "[dog.name] lies down on the ground and stares at you."
            else:
                "You are engaged in a fierce battle for a good minute."
                p "Putting up a great fight, huh!!! I won't lose to the likes of you!!"
                d "{i}Panting heavily{/i}"
                if r.random() < 0.5:
                    "Your hand slips, and you fall forward towards [dog.name]!"
                else:
                    "You pull hard enough, and [dog.name] gets pulled towards you!"
                "You collapse into a single, heartwarming pile."
                p "Gooood [personPronoun]."
                "You give [objPronoun] a well-earned treat."
                d "Woof!"
                $ if dog.traits.training < 5: dog.traits.training += 0.5
    jump home_menu

label home_tv:
    "You on turn on TV. Maybe you and [dog.name] can watch something interesting. [dog.name] watches carefully."
    menu:
        "The 11th Annual Dog Show" if not "dogShow" in tv_done:
            $tv_done.append("dogShow")
            "You switch over to the dog show. You might be able to learn a thing or two about dog training."
            "A short haired dog dashes through the agility obstacle course."
            d "Woof! Woof! Woof!"
            if dog.traits.jealousy >= 3:
                "[dog.name] keeps jumping in front of the screen, looking at you expectantly."
                p "Hmm... I think we should see a different show."
            elif dog.traits.energy >= 3:
                "[dog.name] starts running and bouncing around excitedly."
                p "You think you can compete too?"
                d "Arf!"
                $if dog.traits.training < 5: dog.traits.training += 0.5
            else:
                "[dog.name] seems invested in the competition."
                p "These dogs are the best of the best!"
                $if dog.traits.training < 5: dog.traits.training += 0.5
            jump home_tv
        "Apex Canines" if not "wolf" in tv_done:
            $tv_done.append("wolf")
            "A large intimidating wolf appears on screen."
            if dog.traits.passAggress >= 4:
                d "{b} Growl... {\b}"
            elif dog.traits.social >= 4:
                "[dog.name] starts barking at the TV excitedly. [subjPronoun] seems to think the wolf is just a giant dog."
                p "Friends with a wolf, huh?"
            else: 
                "[dog.name] looks a little scared and pulls close to you."
            jump home_tv
        "Dogs and Desserts" if not "cooking" in tv_done:
            $tv_done.append("cooking")
            cooking_host "And today we're making some delicious apple ice cream. Perfect for dogs of all sizes."
            if dog.traits.gluttony >= 4:
                "[dog.name] is drooling uncontrollably."
                p "That ice cream looks pretty good. Even I'd like to try some!"
                $if owner.traits.kindness < 5: owner.traits.kindness += 0.5
            else:
                "[dog.name] tries to sniff the TV screen, but it doesn't smell anything like ice cream."
                d "Woof?"
                "[dog.name] feels betrayed."
            jump home_tv
        "Turn off TV." if len(tv_done) > 0:
            p "I think we learned some new things today!"
            d "Bark!"
            
            # Doesn't pick the dog show channel
            if not "dogShow" in tv_done and dog.traits.jealousy >= 3:
                $if owner.traits.loyalty < 5: owner.traits.loyalty += 0.5
            # Doesn't pick the cooking channel
            if not "cooking" in tv_done and dog.traits.gluttony >= 3:
                $if owner.traits.discipline < 5: owner.traits.discipline += 0.5

            jump home_menu
label home_end:
    "It was a surprisingly tiring day today."
    p "I hope you grew more accustomed to my house, [dog.name]!"
    d "Arf!"
    "[dog.name] closes [possPronoun] eyes and takes a little nap by your side."
    jump new_day


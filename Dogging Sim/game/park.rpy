# DOG PARK FILE
# TODO: MORE THROWS

# PARK INTRO
label park_start:
    play music "C_Major_Prelude.mp3" fadeout 1
    scene dogPark
    python:
        park_fetched = 0
        park_met = []
        cocoa = Character("Cocoa")
        blogger = Character("Blogger")
        trainer = Character("Trainer")
        pepper = Character("Pepper")
        trucker = Character("Trucker")

    image cocoaImg = "images/npcs/cocoa.png"
    image bloggerImg = "images/npcs/blogger.png"
    image trainerImg = "images/npcs/trainer.png"
    image pepperImg = "images/npcs/pepper.png"
    image truckerImg = "images/npcs/trucker.png"

    "What better way to bond with [dog.name] than taking [objPronoun] to the park? There’s one pretty close to your house!"
    if dog.traits.social <= 2:
        "Along the way, [dog.name] puts [possPronoun] nose in the air and silently whips [possPronoun] head left and right. [possPronoun] ears are pointed straight up."
        "You notice a lot of slack on the leash as [subjPronoun] walks closely in front of you, checking [possPronoun] surroundings."
    elif dog.traits.energy <= 1:
        "[dog.name] walks a couple blocks with you, and then sits down on a street corner."
        show dogImage
        d "{i}Whimpers{/i}"
        hide dogImage
        "It.... it kinda reminds you of yourself during finals week."
        p "Come on, [dog.name]. It'll be fun, I promise!"
        "After some gentle encouragement, [dog.name] cooperates with you. It walks in front of you, keeping its head pointed low."
    elif dog.traits.energy >= 4 and dog.traits.passAggress >= 3:
        "[dog.name] leaps forward, pulling you into a brisk jog."
        show dogImage
        d "Woof! Woof!"
        hide dogImage
        p "Hey!! Slow down, [personPronoun]! I can't keep up like this!"
        "[dog.name] jumps around, trotting around trees and sniffing the ground. [possPronoun_upper] ears point straight up and [possPronoun] tail flicks left and right."
        "[possPronoun_upper] attention is quickly diverted to something new each time, and [subjPronoun] leads you up and down the streets."
        show dogImage
        d "{i}Heavy panting{/i}"
        hide dogImage
        "You have a feeling you're gonna get some good exercise today!"
    else:
        "[dog.name] briskly walks ahead of you. [subjPronoun_upper] occasionally sniffs at the base of a tree, and [possPronoun] eyes are caught by the occasional butterfly."
        "It's a beautiful day outside, and the crisp, fresh air smells amazing this time of year. You make it to the dog park in no time."
    jump park_menu_start

# PARK MENU
label park_menu_start:
    "It's a pretty busy day at the park. There's a good variety of dogs around, playing with each other and their owners."
    menu:
        "What would you like to do?"
        "Play fetch.":
            jump park_fetch_start
        "Meet other dogs.":
            jump park_meet_menu

# PARK FETCH
label park_fetch_start:
    "You pull out a tennis ball you found at home. Dogs like these, right? Probably."
    p "Over here, [dog.name]! Come sniff this ball."
    "You hold it out to [possPronoun]."
    show dogImage
    d "{i}Whiiine!{/i}"
    hide dogImage
    "[dog.name] snatches the ball from you, saliva getting all over your hand. [subjPronoun_upper] begins gnawing on it ravenously."

    if dog.traits.passAggress >= 4 or dog.traits.gluttony >= 4 or dog.traits.energy >= 4:
        if dog.traits.passAggress >= 4:
            show dogImage
            d "{i}Predatorial slobbering{/i}"
            hide dogImage
        elif dog.traits.gluttony >= 4 or dog.traits.energy >= 4:
            show dogImage
            d "{i}Loud and adorable chewing noises{/i}"
            hide dogImage
        
        "You wanted to get some exercise in, but you also feel a sort of spiritual connection to [objPronoun]."
        menu:
            "Admonish [dog.name] and take it away from [objPronoun].":
                "[dog.name] starts growling when you try to grab it back."

                if dog.traits.gluttony >= 4:
                    p "[dog.name], NO! Tennis balls are for {i}fetch{/i}, not {i}food{/i}!!"
                else:
                    p "Bad [personPronoun]! We need this to play fetch!"

                "With a little bit of stern talking and some force, you manage to pry it away from [objPronoun]."
                "[subjPronoun_upper] looks at the ground silently."
                $ owner.traits.discipline += 1
                $ if owner.traits.discipline > 5: owner.traits.discipline = 5
            "Feed [objPronoun] a dog treat.":
                p "{i}Sigh...{/i}"
                "You pull out a dog treat and hold it near [possPronoun] nose. [subjPronoun_upper] immediately drops the sopping wet ball onto the ground and licks the treat out of your hand."
                p "Well, I guess that works too..."
                "You pick the ball back up."
                $ owner.traits.kindness += 1
                $ if owner.traits.kindness > 5: owner.traits.kindness = 5
            "Wait for [objPronoun] to finish.":
                "A gentle breeze blows by. [possPronoun] beautiful coat is highlighted in the afternoon glow."
                show dogImage
                d "{i}Panting heavily{/i}"
                hide dogImage
                "After about a minute, [subjPronoun] puts the ball back into your outstretched hand."
                $ owner.traits.patience += 1
                $ if owner.traits.patience > 5: owner.traits.patience = 5
    elif dog.traits.social > 4:
        show dogImage
        d "Arf! Arf! Arf!"
        hide dogImage
        "[subjPronoun_upper] seems pretty hyped already, just by seeing the ball. [subjPronoun_upper] might have done this before!"
        p "Ready, [dog.name]? You ready, [personPronoun]?!"
        show dogImage
        d "Woof!"
        hide dogImage
    else:
        "[subjPronoun_upper] sniffs the ball inquisitively, then tilts [possPronoun] head to the side."
        p "You want the ball, [personPronoun]? You want it?"
        "[subjPronoun_upper] blinks."

    jump park_fetch_throw_1

label park_fetch_throw_1:
    $ training += 0.5
    $ if training > 5: training = 5
    "You get up and look down at [dog.name]."
    p "Let's give it a shot!"

    if dog.traits.passAggress >= 4:
        "You pull your arm back. [dog.name] stares intently at the ball, baring [possPronoun] teeth slightly."
        show dogImage
        d "{b}Grrrrrrr...{/b}"
        hide dogImage
    elif dog.traits.energy >= 3:
        "You pull your arm back. [dog.name] lowers the front of [possPronoun] body, forming a slight grin with [possPronoun] lips."

    menu:
        "Lightly toss the ball in front of you.":
            $ owner.traits.kindness += 0.5
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
            $ owner.traits.loyalty += 0.5
            $ if owner.traits.loyalty > 5: owner.traits.loyalty = 5
            "Probably best to start out light!"
            if dog.traits.passAggress >= 4:
                "[dog.name] dashes towards the ball, still gnawing at it until you take it away from [objPronoun]."
                p "Thanks?"
            elif dog.traits.energy >= 2:
                "[dog.name] bolts out immediately from beneath you. [subjPronoun_upper] makes [possPronoun] way there in no time at all, leaping onto the ball."
                "[subjPronoun_upper] dashes back with the ball in [possPronoun] mouth, and tilts [possPronoun] head to one side."
                p "Good [personPronoun]!"
                "[subjPronoun_upper] drops the ball at your feet and quickly wags [possPronoun] tail from side to side, looking at you expectantly."
            else:
                "[dog.name] turns back and stares at you for a moment. [subjPronoun_upper] calmly walks to the ball and places it in [possPronoun] jaw."
                p "Come on! Bring it back, [personPronoun]!"
                "[subjPronoun_upper] stares at you again and puts [possPronoun] jaw loosely around the ball. [subjPronoun_upper] trots over to you, drops the ball, and drops to the floor [possPronoun]SELF."
        "Chuck it a good distance forward.":
            $ owner.traits.patience += 0.5
            $ if owner.traits.patience > 5: owner.traits.patience = 5
            $ owner.traits.discipline += 0.5
            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
            "Let's get this exercise!"
            if dog.traits.passAggress >= 4:
                "[dog.name] senses your energy. You throw the ball as hard as you can and [subjPronoun] darts off, kicking up dirt as [subjPronoun] goes."
                show dogImage
                d "Arf! Arf!"
                hide dogImage
                "[subjPronoun_upper] practically trips over [reflPronoun] trying to get to the ball. You see [dog.name] gnash [possPronoun] teeth through the ball in the distance."
                "[subjPronoun_upper] stays there and starts shaking [possPronoun] head viciously with the ball still in [possPronoun] jaws."
                p "Whoah there!! Let go, [dog.name], come on!"
                "You run over to [possPronoun], and after some time, you manage to get [possPronoun] to drop the ball again."
                p "Jeez..."
            elif dog.traits.energy >= 2:
                "[dog.name] darts out from under you in a blur. [subjPronoun_upper] grasps the ball and gracefully turns towards you."
                "[subjPronoun_upper] dashes back towards you proudly, a certain twinkle in [possPronoun] eye. [subjPronoun_upper] drops the ball at your feet."
                show dogImage
                d "{i}Pants gently{/i}"
                hide dogImage
                p "Gooooood [personPronoun]!!! You did so well!!"
                "You give [possPronoun] a nice big rub all over the top of [possPronoun] fur coat. [possPronoun_upper] tail waggles happily."
            else:
                "You throw the ball a good distance away. It becomes a speck in the distance."
                "[dog.name] looks at the ball a little sadly. [subjPronoun_upper] turns back to look at you, and sits down."
                p "Okay, mood."
                "You stroll over and pick up the ball. [dog.name] follows you."

    $ park_fetched += 1
    jump park_menu

label park_fetch_throw_2:
    $ training += 0.5
    $ if training > 5: training = 5
    "We've still got time. Let's play more!"
    p "Hey, [dog.name], come here!"

    if dog.traits.passAggress >= 4:
        "[dog.name] snarls at the ball in your hand."
        show dogImage
        d "{b}Rrrrr...{/b}"
        hide dogImage
    elif dog.traits.energy >= 3:
        "[dog.name] bounces up and down, wagging [possPronoun] tail vigorously."

    menu:
        "Go for a light throw.":
            $ owner.traits.kindness += 0.5
            $ if owner.traits.kindness > 5: owner.traits.kindness = 5
            $ owner.traits.loyalty += 0.5
            $ if owner.traits.loyalty > 5: owner.traits.loyalty = 5
            "[dog.name] might be tired. Let's give them an easy throw."            
            if dog.traits.passAggress >= 4:
                "[dog.name] lunges towards the ball and pounces on it, but allows you to take the ball from [objPronoun]."
                p "An improvement."
            elif dog.traits.energy >= 4:
                p "Fet-"
                "Before you can even finish, you see that [dog.name] has already returned with the ball in [possPronoun] mouth."
                p "Oh, wow! Good [personPronoun]!"
            elif dog.traits.energy >= 2:
                "[dog.name] makes another runs towards the ball, but at a noticeably slower pace. [subjPronoun_upper] slowly makes [possPronoun] way back towards you and plops the ball at your feet."
                p "Thanks, [dog.name]!"
                d "Woof!"
                "[dog.name] stretches out [possPronoun] front paws and lies down on the grass."
            else:
                "The ball rolls to a halt. With [possPronoun] tail still wagging, [dog.name] looks at the ball and then back at you."
                p "You can do it, [dog.name]!"
                d "Arf!"
                "[dog.name] lets out a yawn and curls up into a ball. [subjPronoun_upper] looks ready to take nap."
                p "Oh.. huh.."
                "You walk over to pick up the ball, feeling a bit tired yourself."
        "Wind up for a pitch.":
            $ owner.traits.patience += 0.5
            $ if owner.traits.patience > 5: owner.traits.patience = 5
            $ owner.traits.discipline += 0.5
            $ if owner.traits.discipline > 5: owner.traits.discipline = 5
            "[dog.name] still seems to be full of energy. [subjPronoun_upper] can handle a far throw."
            if dog.traits.passAggress >= 4:
                "[dog.name] eyes the ball in your hand, ready to pounce at any moment."
                p "Fetch this! Haaah!"
                "[dog.name] zooms towards the ball at great speed."
                "You wrestle with [dog.name] again to retrieve the ball. You manage to pick up a soppy wet mess."
                p "Gross."                
            elif dog.traits.energy >= 4:
                "You throw the ball so far away that you can't even tell where it landed."
                p "Okay, so I might have overdone it just a bit."
                "[dog.name], doesn't seem to mind the distance at all, and keeps bounding towards the ball."
                "You consider running after [dog.name] too, because [subjPronoun] is starting to get out of sight." 
                p "Hey, [dog.name] where are you?"
                "Eventually, however, [dog.name] comes back with the ball proudly in [possPronoun] jaw."
                show dogImage
                d "Bark! Bark!"
                hide dogImage
                p "You're such... a GOOD [personPronoun]!!!"
            else:
                "You start to wind up, but [dog.name] is just rollling around in the grass."
                show dogImage
                d "Woof!"
                hide dogImage
                "You decide to put away the ball."

    $ park_fetched += 1
    jump park_menu


label park_menu:
    "What would you like to do now?"
    menu:
        "Play some fetch." if park_fetched == 0:
            jump park_fetch_throw_1
        "Play some more fetch." if park_fetched == 1:
            jump park_fetch_throw_2
        "Meet other dogs." if len(park_met) < 3:
            jump park_meet_menu
        "Call it a day." if park_fetched != 0 or len(park_met) > 0:
            jump park_end

label park_meet_menu:
    "You look around. There are a couple of dogs and owners you can talk to."
    menu:
        "Adorable dog getting its picture taken" if not "cocoa" in park_met:
            jump park_meet_cocoa
        "Obedient dog doing tricks" if not "roxy" in park_met:
            jump park_meet_roxy
        "Large, collared dog aggressively biting a chew toy" if not "pepper" in park_met:
            jump park_meet_pepper

label park_meet_cocoa:
    show bloggerImg
    blogger "Hey there! This is my dog Cocoa! Isn't he simply adorable?"
    hide bloggerImg

    show cocoaImg
    "A corgi with a darker brown coat looks up at you with shiny eyes, tail wagging contentedly behind him."
    cocoa "Yip!!"
    p "Nice to meet you. This is [dog.name]."
    "Cocoa rolls over onto his back, exposing his incredibly fluffy belly. It looks soft and luscious and beautiful."
    cocoa "Woof!!"
    "You feel your hand drawn towards his stomach."
    hide cocoaImg

    if dog.traits.passAggress >= 4:
        show dogImage
        d "Grrrr!!"
        hide dogImage
        "[dog.name] jumps out and tries to bite Cocoa!"
        p "Whoah!!!! [dog.name]!!!!!!!!!!"
        "You manage to pull [objPronoun] back before [subjPronoun] gets there."

        show bloggerImg
        show cocoaImg at right
        blogger "Hey, watch it! You gotta train your dog before you go to the park!"
        "Cocoa whimpers and cowers behind the blogger, who scowls at you. He picks up Cocoa and walks away."
        hide bloggerImg
        hide cocoaImg
    
    elif dog.traits.social >= 4 and dog.traits.social > dog.traits.jealousy:
            "[dog.name] sniffs curiously at Cocoa. Cocoa turns his head to the side, and stands up."
            show cocoaImg
            cocoa "Yip!"
            show dogImage at left
            d "Yip!"
            "They walk in a circle around each other and begin sniffing each other's butts."
            hide dogImage
            hide cocoaImg

            show bloggerImg
            blogger "Wow, they really seem to like each other. Cocoa doesn't have many genuine friends, so that's nice!"
            hide bloggerImg
            "They spend some time playing with each other. It's a very wholesome time!"
    else:
        menu:
            "Pet Cocoa":
                if dog.traits.jealousy >= 4:
                    "[dog.name] is a little clingy at times, but you can't always let [objPronoun] get what [subjPronoun] wants."
                    show dogImage
                    d "Whiiiiine..."
                    hide dogImage
                    "[dog.name] looks at you, ears flat against [possPronoun] head, and lowers [possPronoun] body to the ground."

                    show bloggerImg
                    blogger "Hey, your dog doesn't seem to like that. Some dogs are just naturally jealous of Cocoa's beauty! Sorry, babe!"
                    hide bloggerImg

                    "The blogger gives you a poop-eating grin, picks up Cocoa, and walks away."
                    $ owner.traits.discipline += 1
                    $ if owner.traits.discipline > 5: owner.traits.discipline = 5
            "Smile at Cocoa":
                "You smile at Cocoa. Cocoa smiles back."
                if dog.traits.jealousy >= 4:
                    "[dog.name] looks pleased."
                    $ owner.traits.loyalty += 1
                    $ if owner.traits.loyalty > 5: owner.traits.loyalty = 5
            "Let [dog.name] pet Cocoa":
                "You gesture [dog.name] to place [possPronoun] paw on Cocoa's belly."
                show dogImage
                d "Arf?"
                hide dogImage
                "[dog.name] looks very confused, but when you place [possPronoun] paw on Cocoa's belly, [subjPronoun] seems to enjoy it alot."

                show bloggerImg
                blogger "Dogs petting other DOGS???!!! I'm posting this right now!"
                hide bloggerImg

                $ owner.traits.kindness += 1
                $ if owner.traits.kindness > 5: owner.traits.kindness = 5


    $ park_met.append("cocoa")
    jump park_menu

label park_meet_roxy:
    "A dog trainer lightly tosses a frisbee into the air in front of you. In a flash, a golden retriever leaps straight up into the air."
    show trainerImg
    trainer "Good girl!"
    hide trainerImg
    "The dog catches the frisbee in midair, flips its body around, and lands gracefully. It hands off the frisbee proudly and recieves a treat."
    p "Sorry to bother you, but what an amazing trick that was! How did you get her to do that?"
    show trainerImg
    trainer "Thank you. My name is Ashe Trainem, and this is Roxy. It takes a lot of practice, but with time, you can train any dog new tricks!"
    hide trainerImg

    if dog.traits.passAggress >= 4:
        show dogImage
        d "Grrrr!!"
        hide dogImage
        "[dog.name] jumps out and tries to bite Roxy!"
        p "Whoah!!!! [dog.name]!!!!!!!!!!"
        "Roxy leaps away nimbly, running a circle around [dog.name]."

        show trainerImg
        trainer "Hey, you should train your dog before taking [objPronoun] to the park, you know! I offer training services for only 500 an hour."
        hide trainerImg
        p "Sorry, but that's a little out of my price range! I can't do $500 an hour!"
        show trainerImg
        trainer "$500? Ohohoho!! Oh no, I meant $500,000, of course. What a silly joke."
        hide trainerImg
        "You walk away."
    else:
        "Roxy walks up to [dog.name] and carefully sniffs at [objPronoun]."
        if dog.traits.social <= 2:
            "[dog.name] hides behind your legs."
            show trainerImg
            trainer "Awww, is someone a little shy? Maybe you should encourage [dog.name] a bit more."
            hide trainerImg
            menu:
                "Lure [dog.name] out with a treat.":
                    $ owner.traits.kindness += 1
                    $ if owner.traits.kindness > 5: owner.traits.kindness = 5
                    p "Heyyyy [dog.name], would ya come out for a puppy snack?"
                    "[possPronoun] ears perk up."
                    show dogImage
                    d "Arf?"
                    hide dogImage
                    "Sure enough, [dog.name] comes right out and gobbles up the puppy snack."
                "Get [dog.name] to come out on [subjPronoun] own.":
                    "You calmly stroke [possPronoun] fur and slowly encourage [subjPronoun] to come out."
                    "With enough time, [dog.name] comes out."
                    $ owner.traits.patience += 1
                    $ if owner.traits.patience > 5: owner.traits.patience = 5

        "[dog.name] looks at Roxy, tilting [possPronoun] head to the side."
        show trainerImg
        trainer "Roxy's really good at making friends. I trained her to do that as well!"
        hide trainerImg
        "You watch as Roxy and [dog.name] slowly warm up to each other. They seem to be getting along just fine!"

    $ park_met.append("roxy")
    jump park_menu

label park_meet_pepper:
    "You approach a large brown and white bulldog with a spiked collar around its neck. There are practically no other dogs around."
    "As you draw closer, the dog drops its chew toy and grows."
    show pepperImg
    pepper "{b}GRRRRRR....{/b}"
    hide pepperImg
    show truckerImg
    trucker "Whoa there, Pepper, old girl! Easy there!"
    hide truckerImg

    "A large, tattooed gentleman tugs on her leash and turns towards you."
    show truckerImg
    trucker "Careful there! Pepper here's been trained as a guard dog, and isn't very good at calming down."
    hide truckerImg
    p "I can tell. Best of luck to you!"
    $ park_met.append("pepper")
    jump park_menu

label park_end:
    "That's probably good enough for now. You got some good walking in, and you learned more about your new friend."
    
    # Don't meet all dogs
    if dog.traits.jealousy >= 4 and len(park_met) < 3:        
        "[dog.name] looks a bit relieved that you haven't tried to meet all the dogs at the park."
        $ owner.traits.loyalty += 0.5
        $ if owner.traits.loyalty > 5: owner.traits.loyalty = 5

    p "Thanks for spending some time with me, [dog.name]. It was fun."
    show dogImage
    d "Arf!"
    hide dogImage
    "[dog.name] tilts [possPronoun] head at you and sits down by your feet."


    jump new_day
# DOG PARK FILE
# TODO: MORE THROWS

# PARK INTRO
label park_start:
    python:
        park_fetched = 0
        park_met = []
        cocoa = Character("Cocoa")
        blogger = Character("Blogger")
        trainer = Character("Trainer")
        pepper = Character("Pepper")
        trucker = Character("Trucker")

    "What better way to bond with [dog.name] than taking [objPronoun] to the park? There’s one pretty close to your house!"
    if dog.traits.social <= 2:
        "Along the way, [dog.name] puts [possPronoun] nose in the air and silently whips [possPronoun] head left and right. [possPronoun] ears are pointed straight up."
        "You notice a lot of slack on the leash as [subjPronoun] walks closely in front of you, checking [possPronoun] surroundings."
    elif dog.traits.energy <= 1:
        "[dog.name] walks a couple blocks with you, and then sits down on a street corner."
        d "{i}Whimpers{/i}"
        "It.... it kinda reminds you of yourself during finals week."
        p "Come on, [dog.name]. It'll be fun, I promise!"
        "After some gentle encouragement, [dog.name] cooperates with you. It walks in front of you, keeping its head pointed low."
    elif dog.traits.energy >= 4 and dog.traits.passAggress >= 3:
        "[dog.name] leaps forward, pulling you into a brisk jog."
        d "Woof! Woof!"
        p "Hey!! Slow down, [personPronoun]! I can't keep up like this!"
        "[dog.name] jumps around, trotting around trees and sniffing the ground. [possPronoun_upper] ears point straight up and [possPronoun] tail flicks left and right."
        "[possPronoun_upper] attention is quickly diverted to something new each time, and [subjPronoun] leads you up and down the streets."
        d "{i}Heavy panting{/i}"
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

    if dog.traits.gluttony >= 4:
        d "{i}Whiiine!{/i}"
        "[dog.name] snatches the ball from you, saliva getting all over your hand. [subjPronoun_upper] begins gnawing on it ravenously."
        d "{i}Loud and adorable chewing noises{/i}"
        "You wanted to get some exercise in, but you also feel a sort of spiritual connection to [possPronoun]."
        menu:
            "Admonish [dog.name] and take it away from [possPronoun].":
                p "[dog.name], NO! Tennis balls are for {i}fetch{/i}, not {i}food{/i}!!"
                "With a little bit of stern talking and some force, you manage to pry it away from [possPronoun]."
                "[subjPronoun_upper] looks at the ground silently."
                $ if dog.traits.training < 5: dog.traits.training += 0.5
            "Feed [possPronoun] a dog treat.":
                p "{i}Sigh...{/i}"
                "You pull out a dog treat and hold it near [possPronoun] nose. [subjPronoun_upper] immediately drops the sopping wet ball onto the ground and licks the treat out of your hand."
                p "Well, I guess that works too..."
                "You pick the ball back up."
                $ if dog.traits.gluttony < 5: dog.traits.gluttony += 0.5
            "Wait for [objPronoun] to finish.":
                "A gentle breeze blows by. [dog.name]'s beautiful coat is highlighted in the afternoon glow."
                d "{i}Panting heavily{/i}"
                "After about a minute, [subjPronoun] puts the ball back into your outstretched hand."
    elif dog.traits.social > 4:
        d "Arf! Arf! Arf!"
        "[subjPronoun_upper] seems pretty hyped already, just by seeing the ball. [subjPronoun_upper] might have done this before!"
        p "Ready, [dog.name]? You ready, [personPronoun]?!"
        d "Woof!"
    else:
        "[subjPronoun_upper] sniffs the ball inquisitively, then tilts [possPronoun] head to the side."
        p "You want the ball, [personPronoun]? You want it?"
        "[subjPronoun_upper] blinks."

    jump park_fetch_throw_1

label park_fetch_throw_1:
    "You get up and look down at [dog.name]."
    p "Let's give it a shot!"

    if dog.traits.passAggress >= 4:
        "You pull your arm back. [dog.name] stares intently at the ball, baring [possPronoun] teeth slightly."
        d "{b}Grrrrrrr...{/b}"
    elif dog.traits.energy >= 3:
        "You pull your arm back. [dog.name] lowers the front of [possPronoun] body, forming a slight grin with [possPronoun] lips."

    menu:
        "Lightly toss the ball in front of you.":
            "Probably best to start out light!"
            if dog.traits.energy <= 2  and dog.traits.passAggress >= 4:
                "Seems like [dog.name] is in a bad mood. Maybe we should try asking [possPronoun] nicely."
                p "[dog.name] do you want to play?"
                "[dog.name] lets out a nasty snarl."
                p "Okay, nevermind."
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
            "Let's get this exercise!"
            if dog.traits.passAggress >= 4:
                "[dog.name] senses your energy. You throw the ball as hard as you can and [subjPronoun] darts off, kicking up dirt as [subjPronoun] goes."
                d "Arf! Arf!"
                "[subjPronoun_upper] practically trips over [reflPronoun] trying to get to the ball. You see [dog.name] gnash [possPronoun] teeth through the ball in the distance."
                "[subjPronoun_upper] stays there and starts shaking [possPronoun] head viciously with the ball still in [possPronoun] jaws."
                p "Whoah there!! Let go, [dog.name], come on!"
                "You run over to [possPronoun], and after some time, you manage to get [possPronoun] to drop the ball again."
                p "Jeez..."
            elif dog.traits.energy >= 2:
                "[dog.name] darts out from under you in a blur. [subjPronoun_upper] grasps the ball and gracefully turns towards you."
                "[subjPronoun_upper] dashes back towards you proudly, a certain twinkle in [possPronoun] eye. [subjPronoun_upper] drops the ball at your feet."
                d "{i}Pants gently{/i}"
                p "Gooooood [personPronoun]!!! You did so well!!"
                "You give [possPronoun] a nice big rub all over the top of [possPronoun] fur coat. [possPronoun_upper] tail waggles happily."
            else:
                "You throw the ball a good distance away. It becomes a speck in the distance."
                "[dog.name] looks at the ball a little sadly. [subjPronoun_upper] turns back to look at you, and sits down."
                p "Okay, mood."
                "You stroll over and pick up the ball. [dog.name] follows you."

    $ park_fetched += 1
    # Boost for playing fetch
    if not (dog.traits.energy <= 2  and dog.traits.passAggress >= 4):
        $if dog.traits.training < 5: dog.traits.training += 0.5
    jump park_menu

    label park_fetch_throw_2:
    "We've still got time. Let's play more!"
    p "Hey, [dog.name], come here!"

    if dog.traits.energy <= 2  and dog.traits.passAggress >= 4:
        "[dog.name] gives you a sharp glare."
        p "Haha, I'm joking, I'm joking."
    elif dog.traits.energy >= 3:
        "[dog.name] bounces up and down, wagging [possPronoun] tail vigorously."

    menu:
        "Go for a light throw.":
            "[dog.name] might be tired. Let's give them an easy throw."
            if dog.traits.energy >= 4:
                p "Fet-"
                "Before you can even finish, you see that [dog.name] has already returned with the ball in [possPronoun] mouth."
                p "Oh, wow! Good [personPronoun]!"
            elif dog.traits.energy < 2:
                "[dog.name] makes another runs towards the ball, but at a noticeably slower pace. [subjPronoun_upper] slowly makes [possPronoun] way back towards you and plops the ball at your feet."
                p "Thanks, [dog.name]!"
                b "Woof!"
                "[dog.name] stretches out [possPronoun] front paws and lies down on the grass."
            else:
                "The ball rolls to a halt. With [possPronoun] tail still wagging, [dog.name] looks at the ball and then back at you."
                p "You can do it, [dog.name]!"
                b "Arf!"
                "[dog.name] lets out a yawn and curls up into a ball. [subjPronoun_upper] looks ready to take nap."
                p "Oh.. huh.."
                "You walk over to pick up the ball, feeling a bit tired yourself."
        "Wind up for a pitch.":
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
                d "Bark! Bark!"
                p "You're such... a GOOD [personPronoun]!!!"
                $if dog.traits.training < 5: dog.traits.training += 1.5
            else:
                "You start to wind up, but [dog.name] is just rollling around in the grass."
                d "Woof!"
                "You decide to put away the ball."


    $ park_fetched += 1
     # Boost for playing fetch
    if not (dog.traits.energy <= 2  and dog.traits.passAggress >= 4):
        $if dog.traits.training < 5: dog.traits.training += 0.5
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
    blogger "Hey there! This is my dog Cocoa! Isn't he simply adorable?"
    "A corgi with a darker brown coat looks up at you with shiny eyes, tail wagging contentedly behind him."
    cocoa "Yip!!"
    p "Nice to meet you. This is [dog.name]."
    "Cocoa rolls over onto his back, exposing his incredibly fluffy belly. It looks soft and luscious and beautiful."
    cocoa "Woof!!"
    "You feel your hand drawn towards his stomach."

    if dog.traits.passAggress >= 5:
        d "Grrrr!!"
        "[dog.name] jumps out and tries to bite Cocoa!"
        p "Whoah!!!! [dog.name]!!!!!!!!!!"
        "You manage to pull [objPronoun] back before [subjPronoun] gets there."
        blogger "Hey, watch it! You gotta train your dog before you go to the park!"
        "Cocoa whimpers and cowers behind the blogger, who scowls at you. He picks up Cocoa and walks away."
    else:
        menu:
            "Pet Cocoa":
                if dog.traits.jealousy >= 3:
                    d "Whiiiiine..."
                    "[dog.name] looks at you, ears flat against [possPronoun] head, and lowers [possPronoun] body to the ground."
                    blogger "Hey, your dog doesn't seem to like that. Some dogs are just naturally jealous of Cocoa's beauty! Sorry, babe!"
                    "The blogger gives you a poop-eating grin, picks up Cocoa, and walks away."
            "Smile charmingly at Cocoa":
                "You smile at Cocoa. Cocoa smiles back."
                # Don't pet Cocoa
                $if owner.traits.loyalty < 5: 
                $   if dog.traits.jealousy <= 3: owner.traits.loyalty += 0.5 
                $   else: owner.traits.loyalty += 1
                if dog.traits.social >= 3:
                    "[dog.name] sniffs curiously at Cocoa. Cocoa turns his head to the side, and stands up."
                    cocoa "Yip!"
                    d "Yip!"
                    "They walk in a circle around each other and begin sniffing each other's butts."
                    blogger "Wow, they really seem to like each other. Cocoa doesn't have many genuine friends, so that's nice!"
                    "They spend some time playing with each other. It's a very wholesome time!"

    $ park_met.append("cocoa")
    jump park_menu

label park_meet_roxy:
    "A dog trainer lightly tosses a frisbee into the air in front of you. In a flash, a golden retriever leaps straight up into the air."
    trainer "Good girl!"
    "The dog catches the frisbee in midair, flips its body around, and lands gracefully. It hands off the frisbee proudly and recieves a treat."
    p "Sorry to bother you, but what an amazing trick that was! How did you get her to do that?"
    trainer "Thank you. My name is Ashe Trainem, and this is Roxy. It takes a lot of practice, but with time, you can train any dog new tricks!"

    if dog.traits.passAggress >= 5:
        d "Grrrr!!"
        "[dog.name] jumps out and tries to bite Roxy!"
        p "Whoah!!!! [dog.name]!!!!!!!!!!"
        "Roxy leaps away nimbly, running a circle around [dog.name]."
        trainer "Hey, you should train your dog before taking [objPronoun] to the park, you know! I offer training services for only 500 an hour."
        p "Sorry, but that's a little out of my price range! I can't do $500 an hour!"
        trainer "$500? Ohohoho!! Oh no, I meant $500,000, of course. What a silly joke."
        "You walk away."
    else:
        "Roxy walks up to [dog.name] and carefully sniffs at [objPronoun]. [dog.name] looks back, tilting [possPronoun] head to the side."
        trainer "Roxy's really good at making friends. I trained her to do that as well!"
        "You watch as Roxy and [dog.name] slowly warm up to each other. They seem to be getting along just fine!"
        $ if dog.traits.social < 5: dog.traits.social += 0.5

    $ park_met.append("roxy")
    jump park_menu

label park_meet_pepper:
    "You approach a large brown and white bulldog with a spiked collar around its neck. There are practically no other dogs around."
    "As you draw closer, the dog drops its chew toy and grows."
    pepper "{b}GRRRRRR....{/b}"
    trucker "Whoa there, Pepper, old girl! Easy there!"
    "A large, tattooed gentleman tugs on her leash and turns towards you."
    trucker "Careful there! Pepper here's been trained as a guard dog, and isn't very good at calming down."
    p "I can tell. Best of luck to you!"
    $ park_met.append("pepper")
    jump park_menu

label park_end:
    "That's probably good enough for now. You got some good walking in, and you learned more about your new friend."
    p "Thanks for spending some time with me, [dog.name]. It was fun."
    d "Arf!"
    "[dog.name] tilts [possPronoun] head at you and sits down by your feet."

    # Don't meet other dogs
    if dog.traits.jealousy >= 3 and len(park_met) == 0:
        $if owner.traits.loyalty < 5: owner.traits.loyalty += 1.5

    jump new_day
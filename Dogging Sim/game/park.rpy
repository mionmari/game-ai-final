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
        trucker = Character("trucker")

    "What better way to bond with [dog.name] than taking #HER to the park? There’s one pretty close to your house!"
    if dog.traits.social <= 2:
        "Along the way, [dog.name] puts #HER nose in the air and silently whips #HER head left and right. #HER ears are pointed straight up."
        "You notice a lot of slack on the leash as she walks closely in front of you, checking #HER surroundings."
    elif dog.traits.energy <= 1:
        "[dog.name] walks a couple blocks with you, and then sits down on a street corner."
        d "{i}Whimpers{/i}"
        "It.... it kinda reminds you of yourself during finals week."
        p "Come on, [dog.name]. It'll be fun, I promise!"
        "After some gentle encouragement, [dog.name] cooperates with you. It walks in front of you, keeping its head pointed low."
    elif dog.traits.energy >= 4 and dog.traits.passAggress >= 3:
        "[dog.name] leaps forward, pulling you into a brisk jog."
        d "Woof! Woof!"
        p "Hey!! Slow down, #GIRL! I can't keep up like this!"
        "[dog.name] jumps around, trotting around trees and sniffing the ground. #HER ears point straight up and her tail flicks left and right."
        "#HER attention is quickly diverted to something new each time, and #SHE leads you up and down the streets."
        d "{i}Heavy panting{/i}"
        "You have a feeling you're gonna get some good exercise today!"
    else:
        "[dog.name] briskly walks ahead of you. #SHE occasionally sniffs at the base of a tree, and #HER eyes are caught by the occasional butterfly."
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
    "You hold it out to #HER."

    if dog.traits.gluttony >= 4:
        d "{i}Whiiine!{/i}"
        "[dog.name] snatches the ball from you, saliva getting all over your hand. #SHE begins gnawing on it ravenously."
        d "{i}Loud and adorable chewing noises{/i}"
        "You wanted to get some exercise in, but you also feel a sort of spiritual connection to #HER."
        menu:
            "Admonish [dog.name] and take it away from #HER.":
                p "[dog.name], NO! Tennis balls are for {i}fetch{/i}, not {i}food{/i}!!"
                "With a little bit of stern talking and some force, you manage to pry it away from #HER."
                "#SHE looks at the ground silently."
                $ if dog.traits.houseBroken < 5: dog.traits.houseBroken += 0.5
            "Feed #HER a dog treat.":
                p "{i}Sigh...{/i}"
                "You pull out a dog treat and hold it near #HER nose. #SHE immediately drops the sopping wet ball onto the ground and licks the treat out of your hand."
                p "Well, I guess that works too..."
                "You pick the ball back up."
                $ if dog.traits.gluttony < 5: dog.traits.gluttony += 0.5
            "Wait for her to finish.":
                "A gentle breeze blows by. [dog.name]'s beautiful coat is highlighted in the afternoon glow."
                d "{i}Panting heavily{/i}"
                "After about a minute, #SHE puts the ball back into your outstretched hand."
    elif dog.traits.social > 4:
        d "Arf! Arf! Arf!"
        "#SHE seems pretty hyped already, just by seeing the ball. #SHE might have done this before!"
        p "Ready, [dog.name]? You ready, #GIRL?!"
        d "Woof!"
    else:
        "#SHE sniffs the ball inquisitively, then tilts #HER head to the side."
        p "You want the ball, #GIRL? You want it?"
        "#SHE blinks."

    jump park_fetch_throw_1

label park_fetch_throw_1:
    "You get up and look down at [dog.name]."
    p "Let's give it a shot!"

    if dog.traits.passAggress >= 4:
        "You pull your arm back. [dog.name] stares intently at the ball, baring #HER teeth slightly."
        d "{b}Grrrrrrr...{/b}"
    elif dog.traits.energy >= 3:
        "You pull your arm back. [dog.name] lowers the front of #HER body, forming a slight grin with #HER lips."

    menu:
        "Lightly toss the ball in front of you.":
            "Probably best to start out light!"
            if dog.traits.energy <= 2  and dog.traits.passAggress >= 4:
                "Seems like [dog.name] is in a bad mood. Maybe we should try asking #HER nicely."
                p "[dog.name] do you want to play?"
                "[dog.name] lets out a nasty snarl."
                p "Okay, nevermind."
            elif dog.traits.energy >= 2:
                "[dog.name] bolts out immediately from beneath you. #SHE makes her way there in no time at all, leaping onto the ball."
                "#SHE dashes back with the ball in #HER mouth, and tilts #HER head to one side."
                p "Good #GIRL!"
                "#SHE drops the ball at your feet and quickly wags her tail from side to side, looking at you expectantly."
            else:
                "[dog.name] turns back and stares at you for a moment. #SHE calmly walks to the ball and places it in #HER jaw."
                p "Come on! Bring it back, #GIRL!"
                "#SHE stares at you again and puts #HER jaw loosely around the ball. #SHE trots over to you, drops the ball, and drops to the floor #HERSELF."
        "Chuck it a good distance forward.":
            "Let's get this exercise!"
            if dog.traits.passAggress >= 4:
                "[dog.name] senses your energy. You throw the ball as hard as you can and #SHE darts off, kicking up dirt as #SHE goes."
                d "Arf! Arf!"
                "#SHE practically trips over herself trying to get to the ball. You see [dog.name] gnash #HER teeth through the ball in the distance."
                "#SHE stays there and starts shaking #HER head viciously with the ball still in #HER jaws."
                p "Whoah there!! Let go, [dog.name], come on!"
                "You run over to #HER, and after some time, you manage to get #HER to drop the ball again."
                p "Jeez..."
            elif dog.traits.energy >= 2:
                "[dog.name] darts out from under you in a blur. #SHE grasps the ball and gracefully turns towards you."
                "#SHE dashes back towards you proudly, a certain twinkle in #HER eye. #SHE drops the ball at your feet."
                d "{i}Pants gently{/i}"
                p "Gooooood #GIRL!!! You did so well!!"
                "You give #HER a nice big rub all over the top of #HER fur coat. #HER tail waggles happily."
                $ if dog.traits.houseBroken < 5: dog.traits.houseBroken += 0.5
            else:
                "You throw the ball a good distance away. It becomes a speck in the distance."
                "[dog.name] looks at the ball a little sadly. #SHE turns back to look at you, and sits down."
                p "Okay, mood."
                "You stroll over and pick up the ball. [dog.name] follows you."

    $ park_fetched += 1
    jump park_menu

    label park_fetch_throw_2:
    "We've still got time. Let's play more!"
    p "Hey, [dog.name], come here!"

    if dog.traits.energy <= 2  and dog.traits.passAggress >= 4:
        "[dog.name] gives you a sharp glare."
        p "Haha, I'm joking, I'm joking."
    elif dog.traits.energy >= 3:
        "[dog.name] bounces up and down, wagging #HER tail vigorously."

    menu:
        "Go for a light throw.":
            "[dog.name] might be tired. Let's give them an easy throw."
            if dog.traits.energy >= 4:
                p "Fet-"
                "Before you can even finish, you see that [dog.name] has already returned with the ball in #HER mouth."
                p "Oh, wow! Good #GIRL!"
            elif dog.traits.energy < 2:
                "[dog.name] makes another runs towards the ball, but at a noticeably slower pace.  #SHE slowly makes #HER way back towards you and plops the ball at your feet."
                p "Thanks, [dog.name]!"
                b "Woof!"
                "[dog.name] stretches out #HER front paws and lies down on the grass."
            else:
                "The ball rolls to a halt. With #HER tail still wagging, [dog.name] looks at the ball and then back at you."
                p "You can do it, [dog.name]!"
                b "Arf!"
                "[dog.name] lets out a yawn and curls up into a ball. #SHE looks ready to take nap."
                p "Oh.. huh.."
                "You walk over to pick up the ball, feeling a bit tired yourself."
        "Wind up for a pitch.":
            "[dog.name] still seems to be full of energy. #SHE can handle a far throw."
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
                "You consider running after [dog.name] too, because #SHE is starting to get out of sight." 
                p "Hey, [dog.name] where are you?"
                "Eventually, [dog.name] comes back with the ball proudly in #HER jaw."
                d "Bark! Bark!"
                p "You're such... a GOOD #GIRL!!!"
            else:
                "You start to wind up, but [dog.name] is just rollling around in the grass."
                d "Woof!"
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
        "Call it a day." if park_fetched != 0 and len(park_met) != 0:
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
        "You manage to pull #HER back before #SHE gets there."
        blogger "Hey, watch it! You gotta train your dog before you go to the park!"
        "Cocoa whimpers and cowers behind the blogger, who scowls at you. He picks up Cocoa and walks away."
    else:
        menu:
            "Pet Cocoa":
                if dog.traits.jealousy >= 3:
                    d "Whiiiiine..."
                    "[dog.name] looks at you, ears flat against #HER head, and lowers #HER body to the ground."
                    blogger "Hey, your dog doesn't seem to like that. Some dogs are just naturally jealous of Cocoa's beauty! Sorry, babe!"
                    "The blogger gives you a poop-eating grin, picks up Cocoa, and walks away."
            "Smile charmingly at Cocoa":
                "You smile at Cocoa. Cocoa smiles back."
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
        trainer "Hey, you should train your dog before taking #HER to the park, you know! I offer training services for only 500 an hour."
        p "Sorry, but that's a little out of my price range! I can't do $500 an hour!"
        trainer "$500? Ohohoho!! Oh no, I meant $500,000, of course. What a silly joke."
        "You walk away."
    else:
        "Roxy walks up to [dog.name] and carefully sniffs at #HER. [dog.name] looks back, tilting #HER head to the side."
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
    "[dog.name] tilts #HER head at you and sits down by your feet."
    jump new_day
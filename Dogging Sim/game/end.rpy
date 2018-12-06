label end_true:
    scene dogShelter
    p "Well, it's been a good five days, but I guess it's time to go back to the shelter."
    show dogImage
    d "Arf?"
    hide dogImage
    "You make your way back to the Dogging Sim."
    p "I'm sorry, but I've run into a HUGE problem with [dog.name]."
    show dogImage
    d "{i}Yolemn yip.{/i}"
    hide dogImage
    ds "I'm terribly sorry to hear that. What appears to have been the issue?"
    p "I just... LOVE [dog.name] SOOOOO MUCHHHH I CAN'T CONTAIN MYSELF!!!!"
    "You reach down and rub [possPronoun] hair all over."
    if dog.traits.energy >= 3:
        "[dog.name] runs around you in circles excitedly, tail going crazy in happiness."
    else:
        "[dog.name] sits down smugly at your feet and leans [possPronoun] head against your leg."
    ds "{i}Phew...{/i} I'm relieved to see you two have become such good friends so quickly."
    p "I wouldn't trade [objPronoun] for the world!!"
    "You got the true ending!!! [dog.name] absolutely loves you."
    "We hope you continue to have a good time together from now on!"
return

label end_good:
    scene dogShelter
    "The next day, at the Dogging Sim."
    p "Hey, [dog.name], can we talk for a second?"
    "[dog.name] tilts [objPronoun] head at you and sticks [possPronoun] ears out upright."
    p "We haven't had a perfect time together. That's for sure."
    show dogImage
    d "{i}Sniffs{/i}"
    hide dogImage
    p "But I know that's as much my fault as it is yours! We'll learn to love each other, work around each other, and be there for each other!"
    ds "How heartwarming! I take it your week went well?"
    p "It went amazingly. It's been crazy, but also some of the most fun times I've ever had in my life."
    "You ruffle [dog.name]'s fur a little, and share a knowing gaze."
    "Congratulations! You got the good ending!"
    "We hope you two continue to enjoy your journey together, no matter how difficult, and no matter where it takes you!"
    return

label end_bad:
    scene dogShelter
    "The next day, you manage to drag [dog.name] back to the Dogging Sim."
    p "Excuse me!!"
    if dog.traits.passAggress >= 3:
        "[dog.name] bites at your ankles a little."
        p "Hey! HEY!! STOP THAT!!!"
        ds "Ahh... Please forgive [dog.name], [subjPronoun]'s a little..."
        p "YEP! I know that for sure!! Get off me!!"
        "The employee manages to separate you two."
    elif dog.traits.energy >= 3:
        "[dog.name] leaps up onto you with all of [objPronoun] strength, knocking you to the ground."
        p "Ah.... I'm sorry, but- {i}{b}OOF{/b}{/i}"
        "[dog.name] trots all over you, stepping all over your face and chest."
        p "Ouch...."
        ds "Please, this is no place to take a nap."
        "You manage to get up and dust yourself off."
    elif dog.traits.training <= 1:
        "[dog.name] lifts up [objPronoun] hind leg, looks you directly in the eye, and begins to urinate on your leg."
        p "Egh.... Hey...."
        "The employee just watches with a mixture of amusement and horror on their face."
        p "I don't think [dog.name] likes me very much."
        ds "No. Me neither."
        "You both let out a deep sigh."
    else:
        "As soon as [dog.name] gets inside the store, [subjPronoun] trots to the far corner of the room and just stares at you."
        "You turn to the employee."
        p "Hey... I'm sorry, but I feel like we don't get along very well, you know..."
        ds "That's understandable. The bonds between dogs and humans are often quite difficult to cultivate."
        "[dog.name] just stares."
    ds "I'm very sorry it didn't turn out well."
    p "It's alright... maybe a dog's not for me."
    ds "Or maybe there's a dog more suited to you out there."
    "Thank you for playing! [dog.name] might not have been your dream dog, but please feel free to play again."
    return
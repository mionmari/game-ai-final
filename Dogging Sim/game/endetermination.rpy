init python:
    def checkFlaws(dog):
        results = [True, True, True, True, True]

        # Dog is shy
        if dog.traits.social <= 2:
            if owner.traits.kindness <= 2 or owner.traits.patience <= 2:
                results[0] = False 
        # Dog is aggressive
        if dog.traits.passAggress >= 4:
            if owner.traits.patience <= 4 or owner.traits.kindness <= 2 or owner.traits.discipline <= 2:
                results[1] = False
        # Dog is susceptible to jealousy
        if dog.traits.jealousy >= 4:
            if owner.traits.loyalty <= 4 or owner.traits.kindness <= 2 or owner.traits.discipline <= 2:
                results[2] = False
        # Dog is gluttonous
        if dog.traits.gluttony >= 4:
            if owner.traits.discipline <= 2 or owner.traits.kindness <= 2:
                results[3] = False
        # Dog has low energy
        if dog.traits.energy <= 2:
            if owner.traits.discipline <= 2 or owner.traits.patience <= 2:
                results[4] = False

        return results


label end_determiner:
    
    $results = checkFlaws(dog)
    $trueCount = results.count(True)

    if trueCount >= 4 and dog.traits.training >= 4:
        jump end_true
    elif trueCount >= 2 and dog.traits.training >= 2:
        jump end_true
    else:
        jump end_bad
    
        # if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
        #     jump end_true
        # elif (owner.traits.kindness <= dog.traits.kindness and owner.traits.loyalty <= dog.traits.kindness and owner.traits.patience <= dog.traits.patience and owner.traits.discipline <= dog.traits.discipline): 
        #     jump end_bad
        # else: 
        #     jump end_good

    # elif dog.traits.training >= 2:
        # if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
        #     jump end_good
        # else: 
        #     jump end_bad 

    # else:
    #     jump end_bad

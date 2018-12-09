init python:
    def checkFlaws(dog):
        results = [1, 1, 1, 1, 1]

        # Dog is shy
        if dog.traits.social <= 2:
            if owner.traits.kindness <= 2 or owner.traits.patience <= 2:
                results[0] = 0
        # Doesn't exhibit this flaw
        else: results[0] = -1 
        
        # Dog is aggressive
        if dog.traits.passAggress >= 4:
            if owner.traits.patience <= 4 or owner.traits.kindness <= 2 or owner.traits.discipline <= 2:
                results[1] = 0
        # Doesn't exhibit this flaw
        else: results[1] = -1 
        
        # Dog is susceptible to jealousy
        if dog.traits.jealousy >= 4:
            if owner.traits.loyalty <= 4 or owner.traits.kindness <= 2 or owner.traits.discipline <= 2:
                results[2] = 0
        # Doesn't exhibit this flaw
        else: results[2] = -1 
        
        # Dog is gluttonous
        if dog.traits.gluttony >= 4:
            if owner.traits.discipline <= 2 or owner.traits.kindness <= 2:
                results[3] = 0
        # Doesn't exhibit this flaw
        else: results[3] = -1 
        
        # Dog has low energy
        if dog.traits.energy <= 2:
            if owner.traits.discipline <= 2 or owner.traits.patience <= 2:
                results[4] = 0
        # Doesn't exhibit this flaw
        else: results[4] = -1 

        return results
        


label end_determiner:
    
    $results = checkFlaws(dog)
    $success = results.count(1)
    $flaws = success + results.count(0)

    if flaws == 0:
        $successPercent = 1
    else:
        $successPercent = success / flaws

    if successPercent == 1 and training >= 4:
        jump end_true
    elif successPercent >= 0.5 and training >= 2:
        jump end_good
    else:
        jump end_bad
    
        # if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
        #     jump end_true
        # elif (owner.traits.kindness <= dog.traits.kindness and owner.traits.loyalty <= dog.traits.kindness and owner.traits.patience <= dog.traits.patience and owner.traits.discipline <= dog.traits.discipline): 
        #     jump end_bad
        # else: 
        #     jump end_good

    # elif training >= 2:
        # if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
        #     jump end_good
        # else: 
        #     jump end_bad 

    # else:
    #     jump end_bad

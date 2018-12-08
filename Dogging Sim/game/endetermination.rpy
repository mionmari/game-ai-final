label end_determiner:
    if dog.traits.training >= 4:
        if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
            jump end_true
        elif (owner.traits.kindness <= dog.traits.kindness and owner.traits.loyalty <= dog.traits.kindness and owner.traits.patience <= dog.traits.patience and owner.traits.discipline <= dog.traits.discipline): 
            jump end_bad
        else: 
            jump end_good

    elif dog.traits.training >= 1:
        if (owner.traits.kindness >= dog.traits.kindness and owner.traits.loyalty >= dog.traits.kindness and owner.traits.patience >= dog.traits.patience and owner.traits.discipline >= dog.traits.discipline): 
            jump end_good
        else: 
            jump end_bad 

    else:
        jump end_bad
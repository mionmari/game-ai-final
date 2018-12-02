init python:
    class OwnerTraits:
        def __init__ (self):
            self.kindness = 0
            self.loyalty = 0
            self.patience = 0
            self.discipline = 0

    class Owner:
        def __init__ (self):
            self.traits = OwnerTraits()

        # Renpy doesn't like self.__dict__ for some reason...
        # def __str__(self):
        #     return self.name + "\n" + self.breed + "\n" + str(self.traits.__dict__)
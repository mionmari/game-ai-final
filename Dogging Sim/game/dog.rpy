init python:  
    import json

    class DogTraits:
        def __init__ (self, dct):
            self.social = dct['social']
            self.passAggress = dct['passAggress']
            self.jealousy = dct['jealousy']
            self.gluttony = dct['gluttony']
            self.energy = dct['energy']
            self.training = dct['training']

    class Dog:
        def __init__ (self, name, sex, breed, traits):
            self.name = name
            self.sex = sex
            self.breed = breed
            self.traits = traits

        # Renpy doesn't like self.__dict__ for some reason...
        # def __str__(self):
        #     return self.name + "\n" + self.breed + "\n" + str(self.traits.__dict__)


    def as_dog(dct):
        if 'name' in dct:
            return Dog (dct['name'], dct['sex'], dct['breed'], DogTraits(dct['traits']))
        return dct

# if __name__ == '__main__':
#     with open('dogs.json') as json_data:
#         dogs = json.load(json_data, object_hook=as_dog)
        
#     for dog in dogs:
#         print ('\n{0}'.format(dog))
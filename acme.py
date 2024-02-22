import random


class Product:
    '''product class for the corporation acme'''

    def __init__(self, name, price=10, weight=20,
                 flammability=.5, identifier=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = (
            identifier if identifier is not None
            else random.randint(1000000, 10000000)
        )

    def stealability(self):
        '''
        determines whether a product is 'stealable' or not
        based on the products value vs its weight.
        Returns a message
        '''
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        if ratio >= 0.5 and ratio < 1.0:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        '''
        calculates the flammability times the weight,
        and then describes how the product will explode
        '''
        explosion_rating = self.flammability * self.weight
        if explosion_rating < 10:
            return '...fizzle.'
        if explosion_rating >= 10 and explosion_rating < 50:
            return '...boom!'
        return '...BABOOM!!'


class BoxingGlove(Product):
    '''It's a boxing glove product!'''

    def __init__(self, name, price=10, weight=10,
                 flammability=.5,
                 identifier=random.randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        '''update to the explode method in the Product parent class'''
        return "...it's a glove"

    def punch(self):
        '''
        punches a friend, a neighbor, or a stranger, and determines their
        reaction based on the weight of the glove
        '''
        if self.weight < 5:
            return "That tickles."
        if self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        return 'OUCH!'

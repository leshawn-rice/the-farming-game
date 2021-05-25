import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class Generator(object):

    @classmethod
    def generateId(cls, length, taken_ids):
        '''
        generates a string of length "length" comprised
        of random letters and numbers, and returns the value
        '''
        is_generated = False
        id = None
        while not is_generated:
            id = ''.join(random.choice(characters) for i in range(length))
            if id not in taken_ids:
                is_generated = True
        return id

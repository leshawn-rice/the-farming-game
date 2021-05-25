from classes.generator import Generator
from config import ID_LENGTH


class Player(object):
    def __init__(self, taken_ids):
        self.id = Generator.generateId(ID_LENGTH, taken_ids)
        self.wealth = 0
        self.debt = 0
        self.net_worth = 0
        # potentially turn these into sets
        self.grain_fields = []
        self.hay_fields = []
        self.cattle = []
        self.orchards = []
        self.options_to_buy = []
        self.tractors = []
        self.harvesters = []

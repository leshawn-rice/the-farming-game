from classes.generator import Generator
from src.config import ID_LENGTH


class Tractor(object):
    def __init__(self, taken_ids):
        self.id = Generator.generateId(ID_LENGTH, taken_ids)
        self.owners = []

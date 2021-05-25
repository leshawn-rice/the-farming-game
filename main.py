from typing import Set
from classes.tractor import Tractor
from classes.player import Player
from classes.tractor import Tractor

object_ids = set([])


p = Player(object_ids)
object_ids.add(p.id)
t = Tractor(object_ids)
object_ids.add(t.id)


print(f'The player\'s ID is: {p.id}')
print(f'The tractor\'s ID is: {t.id}')
print(f'The taken ID\'s are: {object_ids}')

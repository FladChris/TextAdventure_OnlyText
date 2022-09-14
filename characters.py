from multiprocessing.dummy import DummyProcess


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def injury(self, damage):
        self.health = self.health - damage
    
    def dead(self):
        if self.health <= 0:
            return True
        else:
            return False

class MainCharacter():
    def __init__(self, name, health, damage):
        self.player_name = name
        self.health = health
        self.damage = damage

    def player_name(self):
        return "Dummy"
    
    def health(self):
        return 100

    def damage(self):
        return 10

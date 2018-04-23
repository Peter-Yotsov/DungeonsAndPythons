class Hero:
    def __init__(self, **kwargs):
        for key, value in kwargs:
            setattr(self, key, value)
        self.max_health = self.health
        self.max_mana = self.mana

    def known_as(self):
        return '{} the {}'.format(self.name, self.title)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        pass

    def take_damage(self, damage):
        self.health -= self.damage
        if self.health < 0:
            self.health = 0

        return self.health

    def take_healing(self, healing):
        if self.is_alive():
            self.health += healing
            if self.health >= self.max_health:
                self.health = self.max_health
            return True
        else:
            return False

    def take_mana(self, mana_potion=0):
        if mana_potion == 0:
            self.mana += self.mana_regeneration_rate
        else:
            self.mana += mana_potion
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def equip(self, weapon):
        pass

    def learn(self, spell):
        pass

    def attack(self, *by):
        if by == 'weapon':
            pass
        elif by == 'magic':
            pass

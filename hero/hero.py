from attacksource import Weapon, Spell


class Hero:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.max_health = self.health
        self.max_mana = self.mana
        self.attack_weapon = 0
        self.attack_spell = 0

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
        if isinstance(weapon, Weapon):
            self.attack_weapon = weapon.damage

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.attack_spell = spell.damage

    def attack(self, *by):
        damage = 0
        if by == 'weapon':
            damage == self.attack_weapon
        elif by == 'magic':
            damage == self.attack_spell

        return damage

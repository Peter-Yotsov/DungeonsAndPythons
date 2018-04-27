from weapon import Weapon
from spell import Spell


class Hero:
    def __init__(self, *, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = self.health
        self.max_mana = self.mana
        self.current_weapon = 'No weapon'
        self.current_spell = 'No spell'

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
        if type(self.current_spell) is not str:
            if self.current_spell.mana_cost <= self.mana:
                return True

        return False

    def take_damage(self, damage):
        self.health -= damage
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
            self.current_weapon = weapon

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.current_spell = spell

    def attack(self, *, by):
        damage = 0
        if by == 'weapon' and type(self.current_weapon) is not str:
            damage = self.current_weapon.damage
        elif by == 'spell' and type(self.current_spell) is not str:
            if self.can_cast():
                damage = self.current_spell.damage
                self.mana -= self.current_spell.mana_cost
            else:
                print('Not enough mana to cast {}'.
                      format(self.current_spell.name))
        return damage

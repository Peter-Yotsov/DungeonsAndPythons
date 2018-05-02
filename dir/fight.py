class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        print('A fight is started between {}({}, {}) and Enemy({}, {}, {})'.
              format(self.hero.known_as(),
                     self.hero.get_health(),
                     self.hero.get_mana(),
                     self.enemy.get_health(),
                     self.enemy.get_mana(),
                     self.enemy.get_damage()))

    def hero_attack(self, by=None):
        if by == 'spell' or (by is None and self.hero.can_cast()):
            self.enemy.current_health -= self.hero.current_spell.damage
            self.hero.mana -= self.hero.current_spell.mana_cost

            return '{} casts a {}, hits Enemy for {} damage.\
 Enemy health is {}\n'.format(self.hero.known_as(),
                              self.hero.current_spell.name,
                              self.hero.current_spell.damage,
                              self.enemy.get_health())

        elif by == 'weapon' or by is None:
            self.enemy.current_health -= self.hero.current_weapon.damage

            return '{} hits Enemy with {} for {} damage.\
 Enemy health is {}\n'.format(self.hero.known_as(),
                              self.hero.current_weapon.name,
                              self.hero.current_weapon.damage,
                              self.enemy.get_health())

    def enemy_attack(self):
        self.hero.health -= self.enemy.damage

        return 'Enemy hits {} for {} damage.\
 {} health is {}\n'.format(self.hero.known_as(),
                           self.enemy.damage,
                           self.hero.known_as(),
                           self.hero.health)

    def ongoing_fight(self, hero_choice=None):
        while True:
            self.hero_attack(by=hero_choice)
            if self.enemy.current_health <= 0:
                return 'Enemy is dead!\n'

            self.enemy_attack()
            if self.hero.health <= 0:
                return '{} is dead!\n'.format(self.hero.known_as())

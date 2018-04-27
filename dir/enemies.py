class Enemy:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.current_health = self.health
        self.current_mana = self.mana

    def is_alive(self):
        return self.current_health > 0

    def can_cast(self):
        return self.current_mana > 0

    def get_health(self):
        return self.current_health

    def get_mana(self):
        return self.current_mana

    def take_healing(self, healig_points):
        if self.is_alive():
            self.current_health = max(self.current_health + healig_points,
                                      self.health)
            return True
        else:
            return False

    def take_mana(self, mana_points):
        if mana_points < 0:
            raise ValueError("Points must be greater than zero!")

        self.current_mana = max(self.current_mana + mana_points, self.mana)

    def attack(self, by):
        if by in self.__dict__.keys():
            return self.by
        else:
            return 0

    def take_damage(self, damage):
        if type(damage) is not int and type(damage) is not float:
            raise TypeError("The type of damage points\
                             must be integer or float!")

        self.current_health = self.current_health - damage

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell


if __name__ == '__main__':
    main()

class Weapon:
    def __init__(self, *, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return '{} deals {} damage.'.format(self.name, self.damage)

class Spell:
    def __init__(self, *, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __repr__(self):
        return str(self)

    def __str__(self):
    	return 'The {} spell deals {} damage,\
         costs {} mana and has a cast range of {}'\
         .format(self.name, self.damage, self.mana_cost, self.cast_range)

import unittest
from weapon import Weapon
from spell import Spell


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.w = Weapon(name="The Axe of Destiny", damage=20)

    def test_init(self):
        self.assertTrue(self.w, '{} deals {} damage'.format(
            self.w.name,
            self.w.damage
        ))


class TestSpell(unittest.TestCase):
    def setUp(self):
        self.s = Spell(name='Fireball', damage=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertTrue(self.s, 'The {} spell deals {} damage,\
         costs {} mana and has a cast range of {}'.format(
            self.s.name,
            self.s.damage,
            self.s.mana_cost,
            self.s.cast_range
        ))


if __name__ == '__main__':
    unittest.main()

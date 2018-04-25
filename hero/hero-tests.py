import unittest
from hero import Hero
from weapon import Weapon
from spell import Spell


class TestHero(unittest.TestCase):
    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100,
                      mana=100, mana_regeneration_rate=2)
        self.w = Weapon(name="The Axe of Destiny", damage=20)
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_known_as(self):
        self.assertTrue(self.h.known_as(),
                        '{} the {}'.format(self.h.name, self.h.title))

    def test_is_alive(self):
        self.assertTrue(self.h.is_alive())
        self.h.health = 0
        self.assertFalse(self.h.is_alive())

    def test_get_health(self):
        self.assertTrue(self.h.get_health(), self.h.health)

    def test_get_mana(self):
        self.assertTrue(self.h.get_mana(), self.h.mana)

    def test_can_cast(self):
        self.assertFalse(self.h.can_cast())
        self.h.learn(self.s)
        self.assertTrue(self.h.can_cast())
        self.h.mana = 40
        self.assertFalse(self.h.can_cast())

    def test_take_damage(self):
        self.assertEqual(self.h.take_damage(60), 40)
        self.assertEqual(self.h.take_damage(60), 0)

    def test_take_healing(self):
        self.assertTrue(self.h.take_healing(10))
        self.assertEqual(self.h.health, 100)
        self.h.health = 50
        self.assertTrue(self.h.take_healing(10))
        self.assertEqual(self.h.health, 60)
        self.h.health = 0
        self.assertFalse(self.h.take_healing(10))

    def test_take_mana(self):
        self.h.take_mana(10)
        self.assertEqual(self.h.mana, 100)
        self.h.mana = 50
        self.h.take_mana(10)
        self.assertEqual(self.h.mana, 60)
        self.h.take_mana()
        self.assertEqual(self.h.mana, 60 + self.h.mana_regeneration_rate)

    def test_weapon_equip_and_spell_learn(self):
        self.h.learn(self.w)
        self.h.equip(self.s)
        self.assertEqual(self.h.current_spell, 'No spell')
        self.assertEqual(self.h.current_weapon, 'No weapon')

        self.h.learn(self.s)
        self.h.equip(self.w)
        self.assertEqual(self.h.current_spell, self.s)
        self.assertEqual(self.h.current_weapon, self.w)

    def test_attack_function(self):
        self.assertEqual(self.h.attack(by='weapon'), 0)
        self.assertEqual(self.h.attack(by='spell'), 0)

        self.h.learn(self.s)
        self.h.equip(self.w)
        self.assertEqual(self.h.attack(by='weapon'), self.w.damage)
        self.assertEqual(self.h.attack(by='spell'), self.s.damage)

        self.h.mana = 20
        self.assertEqual(self.h.attack(by='spell'), 0)


if __name__ == '__main__':
    unittest.main()

import unittest
from fight import Fight
from hero import Hero
from enemies import Enemy
from weapon import Weapon
from spell import Spell


class Test(unittest.TestCase):
    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100,
                      mana=100, mana_regeneration_rate=2)
        self.w = Weapon(name="The Axe of Destiny", damage=20)
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.e = Enemy(health=100, mana=100, damage=20)
        self.h.equip(self.w)
        self.h.learn(self.s)
        self.f = Fight(self.h, self.e)

    def test_hero_attack(self):
        self.f.hero_attack(by='spell')
        self.assertTrue(self.e.current_health == 70)
        self.assertTrue(self.h.mana == 50)
        self.f.hero_attack()
        self.assertTrue(self.h.mana == 0)
        self.f.hero_attack()
        self.assertTrue(self.e.current_health == 20)
        self.f.hero_attack()
        self.assertFalse(self.e.is_alive())

    def test_enemy_attack(self):
        self.f.enemy_attack()
        self.assertTrue(self.h.health == 80)

    def test_ongoing_fight(self):
        self.f.ongoing_fight()
        self.assertTrue(self.h.is_alive())
        self.assertFalse(self.e.is_alive())

if __name__ == '__main__':
    unittest.main()

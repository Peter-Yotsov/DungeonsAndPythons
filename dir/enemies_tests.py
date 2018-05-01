import unittest
from enemies import Enemy


class EnemiesTests(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_is_alive(self):
        self.assertTrue(self.enemy.is_alive())
        self.enemy.take_damage(101)
        self.assertFalse(self.enemy. is_alive())

    def test_can_cast(self):
        self.assertTrue(self.enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)

    def test_take_healing(self):
        self.assertTrue(self.enemy.take_healing(1))
        self.enemy.take_healing(5)
        self.assertEqual(self.enemy.get_health, 100)
        self.enemy.take_damage(101)
        self.assertFalse(self.enemy.take_healing(1))

    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.enemy.take_mana(-10)

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.enemy.take_damage('smth')


if __name__ == '__main__':
    unittest.main()

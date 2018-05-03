import unittest
from dungeons import Dungeon
from hero import Hero
from coordinates import Coordinates

class TestDungeon(unittest.TestCase):
    def test_initial_spawn(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d_map = Dungeon('map.txt')

        self.assertTrue(d_map.initial_spawn(h))

    def test_is_inside_map(self):
        d_map = Dungeon('map.txt')

        self.assertTrue(d_map.is_inside_map(Coordinates(0, 0)))
        self.assertTrue(d_map.is_inside_map(Coordinates(4, 9)))
        self.assertFalse(d_map.is_inside_map(Coordinates(-1, 9)))
        self.assertFalse(d_map.is_inside_map(Coordinates(10, 9)))

    def test_new_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d_map = Dungeon('map.txt')
        d_map.spawn(h)

        self.assertEqual(d_map.new_coordinates('down'), Coordinates(1, 0))
        self.assertEqual(d_map.new_coordinates('left'), Coordinates(0, 1))

if __name__ == '__main__':
    unittest.main()

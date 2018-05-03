import unittest
from dungeons import Dungeon
from hero import Hero
from coordinates import Coordinates
from spell import Spell

class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.dungeon = Dungeon('map.txt')

    def test_initial_spawn(self):
        self.assertTrue(self.dungeon.initial_spawn(self.hero))
        self.assertEqual(self.dungeon.hero_coords.row, 0)
        self.assertEqual(self.dungeon.hero_coords.column, 0)

    def test_spawn(self):
        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.hero_coords, Coordinates(0, 0))

        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.hero_coords, Coordinates(0, 1))

        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.hero_coords, Coordinates(0, 4))

    def test_is_inside_map(self):
        self.assertTrue(self.dungeon.is_inside_map(Coordinates(0, 0)))
        self.assertTrue(self.dungeon.is_inside_map(Coordinates(4, 9)))
        self.assertFalse(self.dungeon.is_inside_map(Coordinates(-1, 9)))
        self.assertFalse(self.dungeon.is_inside_map(Coordinates(10, 9)))

    def test_new_coordinates(self):
        self.dungeon.spawn(self.hero)

        self.assertEqual(self.dungeon.new_coordinates('down'), Coordinates(1, 0))
        self.assertEqual(self.dungeon.new_coordinates('right'), Coordinates(0, 1))

        self.dungeon.move_hero('right')
        self.assertEqual(self.dungeon.new_coordinates('left'), Coordinates(0, 0))

        self.dungeon.move_hero('down')
        self.assertEqual(self.dungeon.new_coordinates('up'), Coordinates(0, 1))

    def test_change_coordinates_in_map(self):
        expected = '#*###E###E'
        self.dungeon.change_coordinates_in_map(2, 1, '*')
        self.assertEqual(self.dungeon.map[2], expected)

    def test_next_spawn(self):
        spawn_coords = self.dungeon.next_spawn()
        self.assertEqual(next(spawn_coords), Coordinates(0, 1))
        self.assertEqual(next(spawn_coords), Coordinates(0, 4))
        self.assertEqual(next(spawn_coords), Coordinates(0, 5))

    def test_can_attack_by_spell(self):
        spell = Spell(name='a', damage=20, mana_cost=5, cast_range=1)
        self.hero.learn(spell)
        self.dungeon.spawn(self.hero)

        self.dungeon.map = ['HE##', '#.##', '#.##', '#.E.']
        self.assertTrue(self.dungeon.can_attack_by_spell())

        self.dungeon.map = ['H.##', '#.##', '#.##', '#.E.']
        self.assertFalse(self.dungeon.can_attack_by_spell())

        spell = Spell(name='a', damage=20, mana_cost=5, cast_range=2)
        self.hero.learn(spell)

        self.dungeon.map = ['H.E#', '#.##', '#.##', '#.E.']
        self.assertTrue(self.dungeon.can_attack_by_spell())

        self.dungeon.map = ['H..#', '#.##', 'E.##', '#.E.']
        self.assertTrue(self.dungeon.can_attack_by_spell())

        self.dungeon.map = ['H..#', '#E##', '#.##', '#.E.']
        self.assertFalse(self.dungeon.can_attack_by_spell())

    def test_move_hero_from_to(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.map = ['HE##', '#.##', '#.##']

        from_coords = Coordinates(0, 0)
        to_coords = Coordinates(2, 1)
        self.dungeon.move_hero_from_to(from_coords, to_coords)

        expected_from = '.E##'
        expected_to = '#H##'
        self.assertEqual(self.dungeon.map[0], expected_from)
        self.assertEqual(self.dungeon.map[2], expected_to)

    def test_move_hero(self):
        self.dungeon.spawn(self.hero)

        self.dungeon.map = ['H#.#', 'TE##', '#.##', '#.E.']
        self.assertFalse(self.dungeon.move_hero('left'))
        self.assertFalse(self.dungeon.move_hero('right'))
        self.assertTrue(self.dungeon.move_hero('down'))
        self.assertTrue(self.dungeon.move_hero('up'))


if __name__ == '__main__':
    unittest.main()

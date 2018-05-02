from coordinates import Coordinates
from random import random


class Dungeon:
    treasures = []
    dict_ = {'start': 'S',
             'end': 'G',
             'obstacle': '#',
             'walkable': '.',
             'treasure': 'T',
             'enemy': 'E',
             'hero': 'H'
             }

    def __init__(self, filename):
        self.filename = filename
        self.map = []
        self.load_map()
        self.coordiantes = Coordinates(None, None)

    def load_map(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.map.append(line[:-1])

    def print_map(self):
        print("\n".join(self.map))

    def initial_spawn(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == self.dict_['start']:
                    self.map[i][j] = 'H'
                    return True

    def spawn(self, hero):
        if self.coordinates.row is None:
            self.initial_spawn()

        for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] == self.dict_['walkable']:
                        self.map[i][j] = 'H'
                        yield True

    def is_inside_map(self, coordinates):
        return coordinates.row >= 0 and coordinates.row < len(self.map[0])\
            and coordinates.column >= 0\
            and coordinates.column <= len(self.map)

    def new_coordinates(self, direction):
        if direction == 'up':
            new_coordinates = Coordinates(self.hero_coords.row + 1,
                                          self.hero_coords.column)
        elif direction == 'down':
            new_coordinates = Coordinates(self.hero_coords.row - 1,
                                          self.hero_coords.column)
        elif direction == 'left':
            new_coordinates = Coordinates(self.hero_coords.row,
                                          self.hero_coords.column - 1)
        elif direction == 'right':
            new_coordinates = Coordinates(self.hero_coords.row,
                                          self.hero_coords.column + 1)

        return new_coordinates

# mana, healthpotion, weapon, spell
    def pick_treasure(self):
        pass  # TODO

    def move_hero_from_to(self, coord_from, coord_to):
        self.map[coord_from.row][coord_from.column] = self.dict_['walkable']
        self.map[coord_to.row][coord_to.column] = 'H'
        self.hero_coords = Coordinates(coord_to.row, coord_to.column)

    def move_hero(self, direction):
        new_coord = self.new_coordinates(direction)

        if not self.is_inside_map(new_coord):
            return False
        elif self.map[new_coord.row][new_coord.column] ==\
                Dungeon.dict_['obstacle']:
            return False
        elif self.map[new_coord.row][new_coord.column] ==\
                Dungeon.dict_['enemy']:
            pass  # TODO
        elif self.map[new_coord.row][new_coord.column] ==\
                Dungeon.dict_['treasure']:
            self.pick_treasure()
            self.move_hero_from_to(self.hero_coords, new_coord)
            return True

from coordinates import Coordinates
from random import randint
from weapon import Weapon
from spell import Spell
from hero import Hero
import json

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
        self.hero_coords = Coordinates(None, None)

    def load_map(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.map.append(line[:-1])

    def print_map(self):
        print("\n".join(self.map))

    def change_coordinates_in_map(self, row, index, new_char):
        new_row = '{}{}{}'.format(self.map[row][:index], new_char, self.map[index + 1:])
        self.map[row] = new_row

    def initial_spawn(self, hero):
        self.hero = hero

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == self.dict_['start']:
                    self.change_coordinates_in_map(i, j, Dungeon.dict_['hero'])
                    self.hero_coords = Coordinates(i, j)
                    return True

    def spawn(self, hero):
        if self.hero_coords.row is None:
            self.initial_spawn(hero)

        for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] == self.dict_['walkable']:
                        self.change_coordinates_in_map(i, j, Dungeon.dict_['hero'])
                        self.hero_coords = Coordinates(i, j)
                        yield True

    def is_inside_map(self, coordinates):
        return coordinates.row >= 0 and coordinates.row < len(self.map)\
            and coordinates.column >= 0\
            and coordinates.column <= len(self.map[0])

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
        else:
            new_coordinates = Coordinates(self.hero_coords.row,
                                          self.hero_coords.column + 1)

        return new_coordinates

    def pick_treasure(self):
        treasures = {1: 'mana', 2: 'healthpotion', 3: 'weapon', 4: 'spell'}

        num = randint(1, 4)

        if treasures[num] == 'mana':
            self.hero.take_mana(mana_potion=randint(1, 100))
            return 'Found mana points. Hero mana is {}.'.format(self.hero.get_mana())
        elif treasures[num] == 'healthpotion':
            self.hero.take_healing(randint(1, 100))
            return 'Found health potion. Hero health is {}.'.format(self.hero.get_health())

        with open('treasures.json') as f:
            data = json.load(f)

        if treasures[num] == 'weapon':
            random_weapon = randint(0, len(data['Weapon']))
            w = Weapon(data['Weapon'][random_weapon])
            self.hero.equip(w)
            return 'Found weapon: {}'.format(str(w))
        else:
            random_spell = randint(0, len(data['Spell']))
            s = Spell(data['Spell'][random_spell])
            self.hero.learn(s)
            return 'Found spell: {}'.format(str(s))

    def can_attack_by_spell(self):
        if self.hero.current_spell.cast_range < 1:
            return False

        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(1, self.hero.current_spell.cast_range):
            for j in move: 
                coords = Coordinates(j[0] * i, j[1] * i)
                if self.is_inside_map(coords) and self.map[coords.row][coords.column] ==\
                        Dungeon.dict_['enemy']:
                    return True

        return False

    def hero_attack(self, *, by):
        if by == 'weapon' and type(self.current_weapon) is not str:
            #start fight with weapon
            pass
        elif by == 'spell' and type(self.current_spell) is not str:
            can_attack = self.can_attack_by_spell()
            if can_attack and self.hero.can_cast():
                #start fight with spell
                pass
            elif can_attack:
                return 'Enemies found in range, but cannot cast!'
            else:
                return 'Nothing in range {}'.format(self.hero.current_spell.cast_range)

    def move_hero_from_to(self, coord_from, coord_to):
        self.change_coordinates_in_map(coord_from.row, coord_from.column, self.dict_['walkable'])
        self.change_coordinates_in_map(coord_to.row, coord_to.column, self.dict_['hero'])
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
            print(self.pick_treasure())
            self.move_hero_from_to(self.hero_coords, new_coord)
            return True

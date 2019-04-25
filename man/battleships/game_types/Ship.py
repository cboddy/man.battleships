import operator
from enum import Enum
from typing import List, FrozenSet

from man.battleships.exceptions import InvalidOrientationError
from man.battleships.game_types.Point import Point


class Orientation(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"


class Ship:
    def __init__(self):
        self.horizontal_offsets = []
        self.vertical_offsets = []

    def __len__(self):
        return len(self.horizontal_offsets)

    def get_points(self, point: Point, orientation: Orientation) -> FrozenSet[Point]:
        """ Returns a set of points corresponding to the positions the ship will occupy on the game board """
        if orientation == Orientation.Horizontal:
            return frozenset(
                [Point(*map(operator.add, point, p)) for p in self.horizontal_offsets]
            )
        elif orientation == Orientation.Vertical:
            return frozenset(
                [Point(*map(operator.add, point, p)) for p in self.vertical_offsets]
            )
        else:
            raise InvalidOrientationError


class Carrier(Ship):
    """
    Looks like:
                   -
    - - - - -  or  -
                   -
                   -
                   _
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(4, 0)]
        self.vertical_offsets = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(0, 4)]


class Battleship(Ship):
    """
    Looks like:
                 -
    - - - -  or  -
                 -
                 -
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]
        self.vertical_offsets = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]


class Cruiser(Ship):
    """
    Looks like:
                -
    - - -  or   -
                -
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [Point(0, 0), Point(1, 0), Point(2, 0)]
        self.vertical_offsets = [Point(0, 0), Point(0, 1), Point(0, 2)]


class Submarine(Ship):
    """
    Looks like:
                -
    - - -  or   -
                -
    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [Point(0, 0), Point(1, 0), Point(2, 0)]
        self.vertical_offsets = [Point(0, 0), Point(0, 1), Point(0, 2)]


class Destroyer(Ship):
    """
    Looks like:
    
    - -  or  -
             -


    """

    def __init__(self):
        super().__init__()
        self.horizontal_offsets = [Point(0, 0), Point(0, 1)]
        self.vertical_offsets = [Point(0, 0), Point(1, 0)]

# Defines the array of ships that must be placed by a player before the game can begin
def ships_to_place() -> List[Ship]:
    return [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]

import collections
from random import choice
import math

# Chapter 1: Python Data Model
# Summary
# By implementing special methods, your objects can behave like the built-in types,
# enabling the expressive coding style the community considers Pythonic.

# A basic requirement for a Python object is to provide usable string representations of
# itself, one used for debugging and logging, another for presentation to end users.
# That is why the special methods __repr__ and __str__ exist in the data model.

# Emulating sequences, as shown with the FrenchDeck example, is one of the most
# common uses of the special methods. For example, database libraries often return
# query results wrapped in sequence-like collections

# Thanks to operator overloading, Python offers a rich selection of numeric types, from
# the built-ins to decimal.Decimal and fractions.Fraction, all supporting infix
# arithmetic operators. The NumPy data science libraries support infix operators
# with matrices and tensors.

# card deck example ----------------
Card = collections.namedtuple('Card', ['rank', 'suit'])


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(c: Card):
    rank_value = FrenchDeck.ranks.index(c.rank)
    return rank_value * len(suit_values) + suit_values[c.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# vector example ----------------
class Vector:
    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other: 'Vector'):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int | float):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    # card deck example ----------------
    d1 = FrenchDeck()
    print(len(d1))
    print(d1[0])
    print(d1[-1])
    print(choice(d1))
    print(Card("Q", 'hearts') in d1)

    for c in sorted(d1, key=spades_high):
        print(c)

    # vector example ----------------
    v1 = Vector(3, 7)
    v2 = Vector(2, 5)
    print(v1 + v2)
    print(abs(v1))
    print(v1 * 1.5)
    print(bool(v1))
    print(v1)

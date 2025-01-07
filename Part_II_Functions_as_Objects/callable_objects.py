# the call operator '()' can be applied to other objects than just functions.
# To check if an object is callable, use the built-in function callable()
# There are nine callable object types in Python:
# - user-defined functions
# - built-in functions
# - built-in methods - like dict.get
# - methods - functions thar are defined in a class body
# - classes - calling a class creates a new instance of it by first calling its __new__ method, then __init__, and than returning the instance to the caller
# - class instances - if a class defines a __call__ method, it's instances may be invoked as functions
# - generator functions - functions or methods using yield keyword in their body; when called, return a generator objects; iterators
# - native corutine functions - functions or methods defined with async def syntax; when called, return a corutine object
# - async generator functions - functions or methods defined with async def syntax and containing yield keyword;
#       when called, return an async generator object that can be used with async for loops

# ---- User-Defined Callable Types ----
# You can make arbitrary Python object behave like functions by implementing a __call__ instance method

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

if __name__ == '__main__':
    bingo = BingoCage([1, 2, 3, 4, 5])
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))  # prints True - bingo is callable
    print(callable(bingo.pick))  # prints True - bingo.pick is callable
    print(callable(BingoCage))  # prints True - BingoCage is callable

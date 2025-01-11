# functools.partial produces a new callable
# with some of the arguments of the original callable bound to predetermined values.
# Useful for adapting functions to fit into APIs that require a different number of arguments.

from operator import mul
from functools import partial
import unicodedata


if __name__ == '__main__':
    # trivial example
    triple = partial(mul, 3)
    print(triple(7))  # 21
    print(list(map(triple, range(1, 10))))  # [3, 6, 9, 12, 15, 18, 21, 24, 27]

    # more useful example - unicode normalization
    nfc = partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)  # False
    print(nfc(s1) == nfc(s2))  # True
    # partial takes a calalble as first argument and any number of positional or keyword arguments
    from positional_and_keyword_only_parameters import tag
    picture = partial(tag, 'img', class_='pic-frame')
    print(picture(src='wumpus.jpeg'))  # <img class="pic-frame
    # the functools.partialmethod function does the same thing as functools.partial, but is designed to work with methods
    # the functools also has higher order functions designed to be used as function decorators
    # example: lru_cache - caches the results of a function call to speed up subsequent calls
    # singledispatch - allows a single function to handle different types of arguments in different ways


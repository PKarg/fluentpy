# Abstract Base Classes
from collections.abc import Mapping


# usage of abc.Mapping allows the caller to provide an instance of dict,
# defaultdict, ChainMap, UserDict subclass - any sublass of Mapping
def name2hex(name: str, color_map: Mapping[str, str]) -> str: ...


# usage of dict forces caller to provide an instance of dict or subclass of dict
# subclass of UserDict will not be accepted
def name2hex2(name: str, color_map: dict[str, int]) -> str: ...


# because of that in general it's better to use Mapping or MutableMapping in parameter annotations
# it's consistent with Postel's Law - be liberal in what you accept and conservative in what you send


# The return value of a function is always a concrete object, so the return type hint should be a concrete type,
# as in this example that uses list[str]:
def tokenize(text: str) -> list[str]:
    return text.upper().split()


# just like with mappings similar principle applies to sequences
# List annotation should be used in return type hint, and Sequence or Iterable in parameter type hint
# difference between them is that Sequence has length and indexing operations defined on it in addition to iteration
# List should be specified in parameter when it's really necessary
# the same goes for Dict and Set

# the numbers ABC's are rejected by PEP 484, which dictates usage of built-in types for numerical annotations
# int, float, bool, complex etc
# if you want to avoid hardcoding concrete types use numeric protocols like SupportsFloat

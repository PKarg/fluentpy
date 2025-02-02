## Abstract Base Classes
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

## Iterable
# it's recommended to use Sequence or Iterable in function parameter annotations
from collections.abc import Iterable

FromTo = tuple[str, str]  # type alias for a tuple of two strings


def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


# changes is equal to Iterable[tuple[str, str]]
# I'd personally say that it's debatable that FromTo is more readable than tuple[str, str],
# but that's what the author states lol

# since python 3.10 there is explicit TypeAlias type
from typing import TypeAlias, Sequence

ToFrom: TypeAlias = tuple[str, str]

# most important difference between Sequence and Iterable is that Sequence has length and indexing operations defined on it
# Iterable has only iteration defined on it
# both are best used as parameter types, return types should be more specific

## Parametrized Generics and TypeVar
# parametrized generic is a generic type written as list[T], where T is a type variable that will be bound to a concrete type
# with each usage

from random import shuffle
from typing import TypeVar

T = TypeVar("T")  # type variable T


def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError("size must be >= 1")
    result = list(population)
    shuffle(result)
    return result[:size]


# function annotated like that supports any type of sequence - sequence of elements of any type

# TypeVar can also be restricted
# example - numeric TypeVar

NumberT = TypeVar("NumberT", int, float, complex)

from collections import Counter


def mode(data: Iterable[NumberT]) -> NumberT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


# problem with this annotation is, that str can also be used in mode function, but it would make no sense
# in our typevar

# Bounded TypeVar
from collections.abc import Hashable

HashableT = TypeVar("HashableT", bound=Hashable)


def better_mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


## static Protocols
# in python, a protocol definition is written as a typing.Protocol subclass
# however, classes that implement a protocol are don't need to inherit, register
# or declare any relatonship with the protocol class

from typing import Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LT = TypeVar("LT", bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


# Callable
# Callable[[ParamType1, ParamType2], ReturnType]
# covariance and contravariance


# NoReturn -- annotate functions without return value

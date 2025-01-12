from typing import Any

# the Any type - also known as dynamic type


def duble(x):
    return x * 2


def dubleany(x: Any) -> Any:  # this will be accepted by type checkers no problem
    return x * 2


def dubleobject(
    x: object,
) -> object:  # will be rejected by type checkers - object does not support __mul__
    return x * 2


# more general types have less operations defined on them
# object class implements fewer operations than abc.Sequence
# which implements fewer operations than abc.MutableSequence
# which implements fewer operations than list

# the Any type is the most general type, and will be accepted by type checkers;
# it's the most general type and the most specialized type - it supports all operations
# (that's how it's understood by type checkers)


# subtype-of vs consistent-with
# is subtype of is the relationship underpinning Liskov substitution principle
# example
class Dog: ...


class Dachshund(Dog): ...


def pet(dog: Dog) -> None: ...


def pet_dachshund(dachshund: Dachshund) -> None: ...


d1 = Dog()
d2 = Dachshund()

pet(d1)  # works
pet(d2)  # works, even though function expects a Dog
pet_dachshund(d1)  # does not work
pet_dachshund(d2)  # works

# in gradual type system there's also relationship of consistent-with
# consistent-with is a weaker relationship than is subtype of
# every type is consistent-with Any
# Any is consistent-with every type


def pet_any(dog: Any) -> None: ...


d0 = object()
pet_any(d0)  # works
pet_any(d1)  # works
pet_any(d2)  # works

# simple Types and Classes
# simple types like int, float, str, bool, and bytes may be used directly in type hints.
# concrete classes from stdlib may also be used directly in type hints
# just like classes from external packages and user defined classes
# the same goes for Absctract Base Classes

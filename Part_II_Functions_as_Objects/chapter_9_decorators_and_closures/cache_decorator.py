import functools
from .implementing_simple_decorator import better_clock


@better_clock
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


def test_fibo():
    print(fibonacci(6))


@functools.cache  # cached is applied on the function returned by better_clock
@better_clock
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


def test_fibo_cached():
    print(fibonacci(6))


# great use case for cache is in single use scripts making api calls
# cache is great, but it can literally consume all available memory
# if you want to limit the cache size, you can use lru_cache which takes additional arguments


@functools.lru_cache(maxsize=16, typed=False)
@better_clock
def fibo_lru(n: int) -> int:
    return n if n < 2 else fibo_lru(n - 2) + fibo_lru(n - 1)


def test_fibo_lru():
    print(fibo_lru(18))


# single dispatch - allows you to define overloaded functions using a single dispatch generic function
import html
from functools import singledispatch
from collections import abc
import fractions
import decimal
import numbers


@singledispatch  # mark the base function with @singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"


@htmlize.register  # register specialized functions to handle specific types
def _(text: str) -> str:  # the name of the function doesn't matter
    content = html.escape(text).replace("\n", "<br/>\n")
    return f"<p>{content}</p>"


# with singledispatch the type of the first argument is used to dispatch to the right function
# it's good idea to register specialized functions with ABCs instead of concrete implementations like int and list
# in realistic use case you would not have all the implementations in the same module

@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f"<pre>{n} (0x{n:x})</pre>"


@htmlize.register
def _(n: bool) -> str:
    return f"<pre>{n}</pre>"


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f"<pre>{frac.numerator}/{frac.denominator}</pre>"


@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f"<pre>{x} ({frac.numerator}/{frac.denominator})</pre>"

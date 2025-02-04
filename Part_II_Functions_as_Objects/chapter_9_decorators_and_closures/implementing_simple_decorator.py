import time
from typing import Callable, Any


def clock(func: Callable[..., Any]) -> Callable[..., Any]:
    def clocked(*args) -> Any:
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print(f"[{elapsed:.8f}s] {name}({arg_str}) -> {result}")
        return result

    return clocked


@clock
def snooze(seconds: float) -> None:
    time.sleep(seconds)


@clock
def factorial(n: int) -> int:
    return 1 if n < 2 else n * factorial(n - 1)


# this decorator does the same thing as: factorial = clock(factorial)


def test_clock():
    snooze(0.123)
    factorial(6)
    assert snooze.__name__ == "clocked"
    assert (
        factorial.__name__ == "clocked"
    )  # the name of the decorated function is changed


# this is the typical behavior of decorators - replacing decorated function
# with a new function that accepts the same arguments

# better way to implement decorators is to use functools.wraps decorator
import functools


def better_clock(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def clocked(*args, **kwargs) -> Any:
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f"{k}={v!r}" for k, v in kwargs.items())
        arg_str = ", ".join(arg_lst)
        print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
        return result

    return clocked


@better_clock
def factorial(n: int) -> int:
    return 1 if n < 2 else n * factorial(n - 1)


def test_better_clock():
    factorial(6)
    assert (
        factorial.__name__ == "factorial"
    )  # the name of the decorated function is changed

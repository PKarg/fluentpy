# implementation of parametrized clock decorator as a class
import functools
import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"


class Clock:

    def __init__(self, fmt: str = DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        @functools.wraps(func)
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ", ".join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked


@Clock()
def snooze(seconds: float):
    time.sleep(seconds)


@Clock("{name}({args}) dt={elapsed:0.3f}s")
def snooze2(seconds):
    time.sleep(seconds)


def test_class_based_deco():
    for i in range(3):
        snooze(0.123)

    for i in range(3):
        snooze2(0.123)

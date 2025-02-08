import time

# for simplicity, the clock decorator will be simpler than the one in 'implementing_simple_decorator.py'

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ", ".join(repr(arg) for arg in _args)
            result = repr(_result)
            print(
                fmt.format(**locals())
            )  # fmt uses the local variables of clocked (linters will complain about this)
            return _result

        return clocked

    return decorate


if __name__ == "__main__":

    @clock()
    def snooze(seconds: float):
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)


@clock("{name}({args}) dt={elapsed:0.3f}s")
def snooze2(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze2(0.123)

# there are strong arguments for decorators to be implemented as classes implementing __call__ method
# instead of functions returning functions

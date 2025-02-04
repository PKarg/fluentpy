import pytest


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == "__main__":
    try:
        f1(3)  # will fail because b is not defined
    except NameError:
        print("error - b is not defined")
    b = 6
    f1(3)  # will work because b is defined as global variable
    try:
        f2(3)  # will fail because b IS defined in the function's scope,
        # but it's defined after it's referenced
    except UnboundLocalError as e:
        print(e)
    # when Python compiles the body of the function, it decides that b is a local variable
    # because it is assigned within the function.
    # Python does not require you to declare variables, but assumes that a variable
    # assigned in the body of a function is local.
    f3(3)  # will work because b is defined as global variable
    print(
        b
    )  # 9 - value of b was changed in f3, and b was explicitly declared as global variable

# --- closures ---
# example of averager class and functional implementations


class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value: float) -> float:
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def test_class_avg():
    avg = Averager()
    assert avg(10) == 10
    assert avg(11) == 10.5
    assert avg(12) == 11.0


def make_averager():
    series = []  # a free variable - variable not bound in the local scope

    def averager(new_value: float) -> float:
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def test_func_avg():
    avg = make_averager()
    assert avg(10) == 10
    assert avg(11) == 10.5
    assert avg(12) == 11.0


def test_func_obj_freevars():
    avg = make_averager()
    assert "series" in avg.__code__.co_freevars
    assert (
        "new_value" in avg.__code__.co_varnames and "total" in avg.__code__.co_varnames
    )
    avg(10)
    assert 10 in avg.__closure__[0].cell_contents
    # looking at the last test it can be seen that a closure is a function
    # that retains the bindings of the free variables when that exist when the function is defined
    # so that they can be used later when the function is invoked and the defining scope is no longer available


# previous implementation of make_averager was not efficient
# in order to make it more efficient we will need 'nonlocal' keyword
# but first - to show why, an example of broken higher-order function


def broken_make_averager():
    count = 0
    total = 0

    def averager(new_value: float) -> float:
        count += 1  # interpreter freaks out because it thinks count and total are local variables
        total += new_value
        return total / count

    # the problem is that using count += is equivalent to count = count + 1
    # and assignment to count leads to it being treated as a local variable
    # it is not a problem with mutable types, because they are not assigned, but mutated
    # with immutable types, this implementation won't work

    return averager


def test_broken_make_averager():
    avg = broken_make_averager()
    with pytest.raises(UnboundLocalError):
        avg(10)  # function call raises UnboundLocalError


def nonlocal_make_averager():
    count = 0
    total = 0

    def averager(new_value: float) -> float:
        nonlocal count, total  # nonlocal keyword allows to change the value of variables in the enclosing scope
        count += 1
        total += new_value
        return total / count

    return averager


def test_nonlocal_make_averager():
    avg = nonlocal_make_averager()
    assert avg(10) == 10
    assert avg(11) == 10.5
    assert avg(12) == 11.0


# what all of this examples show is a behaviour of changing variable lookup logic in python
# when a function is defined, the Python bytecode compiler uses these rules to determine how to fetch a variable x

# 1.If there is a global x declaration, x comes from and is assigned to the x global variable module.
# 2.If x is declared nonlocal, x comes from and is assigned to a variable in the nearest enclosing function.
# 3.If x is a parameter or is assigned a value in the function body, then x is the local variable
# 4.If x is referenced but is not assigned and is not a parameter:
#       x will be looked up in the local scopes of the surrounding function bodies (nonlocal scopes)
#       If not found in surrounding scopes, it will be read from the module global
#       If not found in the global scope, it will be read from __builtins__.__dict__.

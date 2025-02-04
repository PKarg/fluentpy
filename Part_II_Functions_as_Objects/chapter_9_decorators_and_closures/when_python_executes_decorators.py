from typing import Callable, Any

registry = []


def register(func: Callable[..., Any]) -> Callable[..., Any]:
    print(f"registering {func}")
    registry.append(func)
    return func


@register
def f1():
    print("f1")


@register
def f2():
    print("f2")


def f3():
    print("f3")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
    # function decorators are executed when the module is imported
    # decorated functions run only when they are explicitly called
    # this means, that decorators run at import time, but decorated functions run at runtime
    # decorators like register above are rare
    # they can be called registration decorators, and their main purpose is to register calling of other functions
    # in practice most decorators declare an inner function and return it
    # decorators like that are used for example in registry mapping of URL patterns

# adding parameters to decorators needs to another layer changing our decorator to decorator factory

registry = set()


def register(active=True):
    def decorate(func):
        print("running register(active=%s)->decorate(%s)" % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print("running f1()")


@register()
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()

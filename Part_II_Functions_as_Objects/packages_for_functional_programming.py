# there are functions in python that can be used in higher order functions instead of writing very simple lambdas

# example: factorial
from functools import reduce
from operator import mul, itemgetter, attrgetter

def factorial_ano(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

def factorial_ope(n):
    return reduce(mul, range(1, n+1))


if __name__ == "__main__":
    print(factorial_ano(5)) # 120
    print(factorial_ope(5)) # 120

    # another case of operators to replace lambdas are the itemgetter and attrgetter functions

    data = [('a', 1), ('b', 2), ('c', 3)]
    print(sorted(data, key=lambda x: x[1])) # [('a', 1), ('b', 2), ('c', 3)]
    print(sorted(data, key=itemgetter(1))) # [('a', 1), ('b', 2), ('c', 3)]

    data_dicts = [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}, {'name': 'c', 'value': 3}]
    print(sorted(data_dicts, key=lambda x: x['value'])) # [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}, {'name': 'c', 'value': 3}]
    print(sorted(data_dicts, key=itemgetter('value'))) # [{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}, {'name': 'c', 'value': 3}]



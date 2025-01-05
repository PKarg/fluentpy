
if __name__ == '__main__':
    # functions as first class objects -------------------------------------------------------------------------------------------------------------
    # functions are first class objects in Python - it means they can be:
    # created at runtime,
    # assigned to a variable,
    # passed as an argument to a function,
    # returned as the result of a function
    def factorial(n):
        '''returns n!'''
        return 1 if n < 2 else n * factorial(n - 1)

    print(factorial(42))
    print(factorial.__doc__)  # prints the docstring
    print(type(factorial))    # prints the type of the function - <class 'function'>; factorial is an instance of a function class

    fact = factorial
    print(fact(5))  # prints 120 - function can be assigned to a variable and called through that variable
    print(list(map(factorial, range(11))))
    print(list(map(fact, range(11))))  # same as above, but using the variable 'fact'

    # first class functions allow for programming in a functional style - i.e it's possible to pass functions as arguments to other functions

    # higher order functions ---------------------------------------------------------------------------------------------------------------------
    # functions that take other functions as arguments or return functions as results are called higher order functions
    # example: map, sorted, filter, reduce
    # sorted:
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))  # sorts the list by ascending length of the elements; key argument is a function that will be applied to each element for sorting

    def reverse(word):
        return word[::-1]
    print(reverse('testing'))  # prints 'gnitset'
    print(sorted(fruits, key=reverse))  # sorts the list by reversed spelling of the elements
    # in python higher order functions are mostly replaced by list comprehensions and generator expressions
    # example:
    print(list(map(factorial, range(6))))
    print([factorial(n) for n in range(6)])  # same result, but list comprehension has generally better readability

    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # example of higher order function composition, factorial of odd numbers
    print([factorial(n) for n in range(6) if n % 2])  # same result, but again, better readability thanks to using listcomp

    from functools import reduce  # reduce is not a built-in function in Python 3, it's in functools module
    from operator import add

    print(reduce(add, range(100)))  # reduce applies add function to the elements of the iterable, in this case it sums all the numbers from 0 to 99
    print(sum(range(100)))  # same result, but sum is more readable and efficient, also a built-in function
    # other reducing functions: all, any, max, min
    print(all([1, 2, 3]))  # returns True if all elements are true
    print(any([1, None, False]))  # returns True if any element is true


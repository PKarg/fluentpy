# Anonymous functions - lambdas in python
# lambda keyword creates an anonymous function within a single line
# lambdas can be used as arguments to higher order functions
# lambdas are limited to be pure expressions - they can't contain statements (assignments, loops, etc.)

if __name__ == "__main__":
    # sorting a list of words by their reversed spelling with lambdas
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda fruit: fruit[::-1]))
    # outside of the context of argumetns to higher order functions, lambdas are rarely useful
    # very often it's better to just define a named function instead



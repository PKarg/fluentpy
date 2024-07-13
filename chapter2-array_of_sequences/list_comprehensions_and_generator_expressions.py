import array

# ex 1 listomp vs map and filter
symbols = '$¢£¥€¤'

# list comprehension
ords = [ord(symbol) for symbol in symbols]

# map and filter
ords_map = list(map(ord, symbols))

# ex 2 cartesian product
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
tshirts2 = [(size, color) for size in sizes for color in colors]


# ex 3 generator expressions

tup = tuple(ord(sym) for sym in symbols)
ar = array.array('I', (ord(sym) for sym in symbols))

if __name__ == "__main__":
    print(ords)
    print(ords_map)
    print(tshirts)
    print(tshirts2)
    print(tup)
    print(ar)
    print(ar[3])

    # cartesian product in genexp
    for tshirt in (f'{s} {c}' for c in colors for s in sizes):
        print(tshirt)
    # what's important to understand, generators don't produce a list in memory, they produce values on the fly.
    # good for large datasets, or when you don't need to store the entire list in memory.

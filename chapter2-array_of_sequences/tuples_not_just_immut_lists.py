# 1. tuples as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# when tuples are used as records, it's important to remember that sorting may destroy important information


# 2. tuples as immutable lists
# tuple length will never change
# tuples use less memory than lists of the same length
# tuple immutability only applies to stored references, not the referenced objects. dict in a tuple can be changed.

if __name__ == "__main__":
    # tuples as records
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)

    # tuple object mutability example
    a = (1, 2, [30, 40])
    a[2].append(50)
    assert a == (1, 2, [30, 40, 50])  # new element was added to the list stored in the tuple

    # tuple with elements that are mutable is unhashable and can't be used as a dict key
    s = (1, 2, 3)
    old_id = id(s)
    s2 = (4, 5)
    s += s2
    assert old_id != id(s)  # new tuple was created
    print(s)  # it's possible to concatenate tuples but it creates a new tuple

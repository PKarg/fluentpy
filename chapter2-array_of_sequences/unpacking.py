
# standard unpacking
coords = (257, 124)
x, y = coords

# unpacking to function as arguments
v = divmod(*coords)

# grabbing excess items
a, b, *rest = range(5)
a, *body, c, d = range(5)
*head, b, c, d = range(5)


# nested unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def unpack(data):
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in data:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == "__main__":
    print(x, y)
    print(v)
    print(rest)
    print(body)
    unpack(metro_areas)

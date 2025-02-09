from array import array
import math


class Vector2d:
    typecode = "d"  # used for converting to and from bytes
    __match_args__ = ("x", "y")

    @classmethod
    def frombytes(cls, octets: bytes) -> "Vector2d":
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x: float | str, y: float | str):
        self.__x = float(x)  # use float() to check for valid input
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (
            i for i in (self.x, self.y)
        )  # it makes Vector2d iterable, which allows for unpacking

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.x!r}, {self.y!r})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other: "Vector2d"):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec: str = ""):
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash((self.x, self.y))


def test_vector2d_format():
    v1 = Vector2d(3, 4)
    assert format(v1) == "(3.0, 4.0)"
    assert format(v1, ".2f") == "(3.00, 4.00)"
    assert format(v1, ".3e") == "(3.000e+00, 4.000e+00)"
    assert format(v1, "p") == "<5.0, 0.9272952180016122>"
    assert format(v1, "0.3p") == "<5.0, 0.927>"


def test_vector2d_hash():
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    v3 = Vector2d(3, 4)
    assert hash(v1) == hash(v3)
    assert hash(v1) != hash(v2)


def test_vector2d_pattern_match():
    vectors = [Vector2d(0, 0), Vector2d(1, 1), Vector2d(2, 3)]
    for v in vectors:
        match v:
            case Vector2d(0, 0):
                assert v.x == 0
                assert v.y == 0
                assert abs(v) == 0
            case Vector2d(x, y) if x == y:
                assert x == y
            case Vector2d(_, 0):
                assert v.y == 0
            case Vector2d(x, y) if x < y:
                assert x < y
            case _:
                assert False, "unexpected match"

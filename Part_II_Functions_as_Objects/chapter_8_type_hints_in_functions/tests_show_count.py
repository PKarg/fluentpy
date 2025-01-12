import pytest

from gradual_typing_in_practice import show_count


@pytest.mark.parametrize('qty, expected', [
    (1, '1 apple'),
    (2, '2 apples'),
    (0, 'no apples')
])
def test_show_count(qty, expected):
    got = show_count(qty, 'apple')
    assert got == expected


def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'

# the simplest way to define a type is by the operations that can be performed on it

from collections import abc


def double_seq(x: abc.Sequence):
    return (
        x * 2
    )  # type errror - type Sequence does not support multiplication (__mul__)


# duck typing vs static type checking
class Birb:
    pass


class Duckling(Birb):

    def quack(self):
        return print("Quack!")


def alert(birb):
    birb.quack()


def duck_alert(duckling) -> None:
    duckling.quack()


def birb_alert(birb: Birb) -> None:
    birb.quack()


if __name__ == "__main__":
    print(
        double_seq([1, 2, 3])
    )  # [1, 2, 3, 1, 2, 3]; works correctly despite type warning, cause List type itself supports multiplication

    # check birb alerts
    daffy = Duckling()
    alert(daffy)  # Quack!
    duck_alert(daffy)  # Quack!
    birb_alert(daffy)  # Quack!
    # all 3 calls work correctly, despite the type hint in birb_alert() being incorrect

    woody = Birb()  # AttributeError - Birb does not have a quack() method
    alert(woody)
    duck_alert(woody)
    birb_alert(woody)

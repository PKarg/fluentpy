from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __str__(self) -> str:
        return f"Order total: {self.total():.2f} due: {self.due():.2f}"


class Promotion(ABC):  # the Strategy: an abstract base class
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return discount as a positive value to subtract from total."""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points."""

    def discount(self, order: Order) -> Decimal:
        return (
            order.total() * Decimal("0.05")
            if order.customer.fidelity >= 1000
            else Decimal(0)
        )


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units."""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal("0.1")
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items."""

    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        return (
            order.total() * Decimal("0.07") if len(distinct_items) >= 10 else Decimal(0)
        )

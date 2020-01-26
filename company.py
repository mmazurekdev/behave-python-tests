from dataclasses import dataclass, field
from functools import partial
from product import Product

without_init = partial(field, init=False, default=0)


@dataclass
class Company:
    name: str
    income_tax_rate: int
    vat_to_pay: float = without_init()
    income_tax_to_pay: float = without_init()
    income: float = without_init()
    real_income: float = without_init()

    def sell(self, value, vat_rate) -> 'Company':
        self.income += value
        self.vat_to_pay += round((value * vat_rate) / (100 + vat_rate), 2)
        self.income_tax_to_pay += (self.income_tax_rate * (value - self.vat_to_pay)) / 100
        return self

    def buy(self, product: Product) -> 'Company':
        vat_of_product = product.vat_value
        self.vat_to_pay -= vat_of_product
        self.income_tax_to_pay -= (self.income_tax_rate * (product.price - vat_of_product)) / 100
        return self

    def get_taxes(self):
        return self.vat_to_pay, self.income_tax_to_pay

    def get_real_income(self):
        return self.income - self.income_tax_to_pay - self.vat_to_pay
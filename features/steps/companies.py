from behave import *
from company import Company, Product


@given("I created company called '{name}' with income tax rate {income_tax_rate}")
def step_impl(context, name, income_tax_rate):
    context.company = Company(name, int(income_tax_rate))


@when("I sell {name} for {value} with vat at {vat_rate} rate")
def step_impl(context, name, value, vat_rate):
    context.company.sell(Product(name, float(value), int(vat_rate)))


@then("my real income will be {income}")
def step_impl(context, income):
    print(context.company.get_taxes())
    print(context.company.get_real_income())
    assert context.company.get_real_income() == float(income)


@then("my taxes will be vat: {vat_value} and income tax: {income_tax_value}")
def step_impl(context, vat_value, income_tax_value):
    print(context.company.get_taxes())
    assert context.company.get_taxes() == (float(vat_value), float(income_tax_value))


@when("I buy {name} for {price} with vat at {vat_rate} rate")
def step_impl(context, name, price, vat_rate):
    product = Product(name, float(price), int(vat_rate))
    context.company.buy(product)
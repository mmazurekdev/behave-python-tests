from product import Product
from company import Company


company = Company("Flomedia.pl", 19)

services = Product("Usługi", 11500, 23)
computer = Product("Komputer", 5000, 23)
mobile = Product("IPhone", 9000, 23)
some_other_services = Product("Inne usługi", 4500, 23)

taxes = company.\
    sell(services).\
    buy(computer).\
    buy(mobile).\
    sell(some_other_services).get_taxes()

print(taxes)
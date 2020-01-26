from product import Product
from company import Company


c = Company("Flomedia.pl", 19)

p = Product("Kawa", 12.3, 23)


print(c.sell(12300, 23).buy(p).get_taxes())

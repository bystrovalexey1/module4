from src.product import Product
from src.category import Category


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


first_product = Product(
    "Iphone 11 Pro",
    "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч",
    24000.0,
    43,
)
second_product = Product(
    "XIAOMI Ultra Pro",
    "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч",
    24000.0,
    31,
)
first_category = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [first_product, second_product],
)

iterator = ProductIterator(first_category)

for product in iterator:
    print(product)

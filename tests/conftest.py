import os

import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass
from src.product_iterator import ProductIterator


@pytest.fixture
def first_product():
    return Product(
        "Iphone 11 Pro",
        "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч",
        24000.0,
        43,
    )


@pytest.fixture
def second_product():
    return Product(
        "XIAOMI Ultra Pro",
        "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч",
        24000.0,
        31,
    )


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Iphone 11 Pro", "Samsung Galaxy S10"],
    )


@pytest.fixture
def second_category():
    return Category("Верхняя одежда", "Одежда, для выхода на улицу", ["Куртка", "Шапка", "Кроссовки"])


@pytest.fixture
def third_category(first_product, second_product):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [first_product, second_product],
    )


@pytest.fixture
def sum_counter(third_category):
    return f"{third_category.name}, {third_category.products[0].quantity + third_category.products[1].quantity} шт."


@pytest.fixture
def product_1_str(first_product):
    return f"{first_product.name}, {first_product.price} руб. Остаток: {first_product.quantity} шт."


@pytest.fixture
def product_2_str(second_product):
    return f"{second_product.name}, {second_product.price} руб. Остаток: {second_product.quantity} шт."


@pytest.fixture
def counter(first_product, second_product):
    return first_product.price * first_product.quantity + second_product.price * second_product.quantity


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Iphone 13 Pro", "128Gb, 2Gb OZU, 13Mp Camera", 39500, 13, 99.1, "13 Pro", "128 Gb", "Space Gray"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Samsung Galaxy S3", "1TB, 8Gb OZU, 20Mp Camera", 55000, 5, 105.1, "S3", "1 Tb", "black")


@pytest.fixture
def smartphone_3():
    return Smartphone("Nokia 3900", "128Mb, 256Mb OZU, 0.5Mp Camera", 1000, 3, 35.0, "3900", "128 Mb", "Blue")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газон", "Трава для посадки газона", 750, 67, "Russia", "14 дней", "Зеленыый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газон синий", "Трава для посадки газона", 1200, 15, "Germany", "8 дней", "Синий")


@pytest.fixture
def category_smartphones():
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone_1, smartphone_2])
    return category_smartphones


@pytest.fixture
def filename():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")


@pytest.fixture
def empty_list():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "empty_products.json")


@pytest.fixture
def product_iterator(third_category):
    return ProductIterator(third_category)


@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Категория без продуктов", [])

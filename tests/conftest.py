import pytest

from src.category import Category
from src.product import Product


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
        43,
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

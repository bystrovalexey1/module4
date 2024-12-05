import pytest

from src.product import Product, Smartphone, LawnGrass, BaseProduct, MixinLog


def test_product_init(first_product):
    assert first_product.name == "Iphone 11 Pro"
    assert (
        first_product.description
        == "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч"
    )
    assert first_product.price == 24000.0
    assert first_product.quantity == 43


def test_price_setter(capsys):
    product = Product("Nokia 3300", "Cool telephone", 0, 1)
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = 2388.0
    assert product.price == 2388.0


new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


def test_new_str(product_1_str, product_2_str):
    assert product_1_str == "Iphone 11 Pro, 24000.0 руб. Остаток: 43 шт."
    assert product_2_str == "XIAOMI Ultra Pro, 24000.0 руб. Остаток: 31 шт."


def test_counter(counter, first_product, second_product):
    assert first_product + second_product == counter


def test_subclass_product():
    assert issubclass(Smartphone, Product) == True
    assert issubclass(LawnGrass, Product) == True


def test_isinstance_product(smartphone_1, smartphone_2, smartphone_3, lawn_grass_1, lawn_grass_2):
    assert isinstance(smartphone_1, Smartphone) == True
    assert isinstance(smartphone_2, Smartphone) == True
    assert isinstance(smartphone_3, Smartphone) == True
    assert isinstance(lawn_grass_1, LawnGrass) == True
    assert isinstance(lawn_grass_2, LawnGrass) == True


def test_error_type(category_smartphones, smartphone_3, lawn_grass_1):
    with pytest.raises(TypeError):
        assert category_smartphones.add_product("Not a product") == TypeError
    assert category_smartphones.add_product(smartphone_3) is None
    assert category_smartphones.add_product(lawn_grass_1) is None


def test_sum(smartphone_3, smartphone_2, lawn_grass_2):
    assert smartphone_3 + smartphone_2 == 278000
    with pytest.raises(TypeError):
        assert smartphone_3 + lawn_grass_2 == TypeError


def test_abs_classes():
    assert Smartphone.__mro__[1:] == LawnGrass.__mro__[1:]
    assert issubclass(Product, MixinLog) is True
    assert issubclass(MixinLog, object) is True
    assert issubclass(BaseProduct, object) is True


def test_product_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == 'Iphone 11 Pro'
    assert next(product_iterator).name == 'XIAOMI Ultra Pro'


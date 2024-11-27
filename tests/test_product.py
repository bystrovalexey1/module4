from src.product import Product


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

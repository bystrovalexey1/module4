def test_product_init(first_product):
    assert first_product.name == "Iphone 11 Pro"
    assert (
        first_product.description
        == "ядер - 6x(2.65 ГГц), 4 ГБ, 1 SIM, Super Retina XDR, 2436x1125, камера 12+12+12 Мп, NFC, 4G, GPS, 3190 мА*ч"
    )
    assert first_product.price == 24000.0
    assert first_product.quantity == 43

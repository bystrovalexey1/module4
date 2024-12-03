def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.products == ["Iphone 11 Pro", "Samsung Galaxy S10"]
    assert len(first_category.products) == 2

    assert second_category.name == "Верхняя одежда"
    assert second_category.description == "Одежда, для выхода на улицу"
    assert second_category.products == ["Куртка", "Шапка", "Кроссовки"]
    assert len(second_category.products) == 3

    assert first_category.category_count == 3
    assert second_category.category_count == 3
    assert first_category.product_count == 7
    assert second_category.product_count == 7


def test_products(first_category):
    assert first_category.products == ["Iphone 11 Pro", "Samsung Galaxy S10"]


def test_add_product(first_category, second_product):
    assert first_category.product_count == 11
    first_category.add_product(second_product)
    assert first_category.product_count == 12


def test_product_list_property(third_category):
    print(third_category.product_list)
    assert (
        third_category.product_list == "Iphone 11 Pro, 24000.0 руб. Остаток: 43 шт.\n"
        "XIAOMI Ultra Pro, 24000.0 руб. Остаток: 31 шт.\n"
    )


def test_add_counter(sum_counter):
    assert sum_counter == "Смартфоны, 74 шт."

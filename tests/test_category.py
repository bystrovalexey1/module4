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

    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 5
    assert second_category.product_count == 5

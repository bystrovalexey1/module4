from src.product import Product, Smartphone


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        """Функция возврата продуктов"""
        return self.__products

    def add_product(self, new_product: Product):
        """Функция добавления продуктов в список"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def product_list(self):
        """Функция вывода строки продуктов в нужном формате"""
        products_str: str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def __str__(self):
        counter = 0
        for product in self.__products:
            counter += product.quantity
        return f"{self.name}, количество продуктов {counter} шт.\n"

    def middle_price(self):
        """Функция, которая подсчитывает среднюю цену всех товаров"""
        try:
            sum = 0
            quan = 0
            for product in self.__products:
                sum += product.price * product.quantity
                quan += product.quantity
            mid_price = sum / quan
        except ZeroDivisionError:
            return 0
        else:
            return round(mid_price, 2)

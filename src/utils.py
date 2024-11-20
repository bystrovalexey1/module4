import json
import os
from src.product import Product
from src.category import Category


def read_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def data_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    data = read_json("../data/products.json")
    users_data = data_from_json(data)

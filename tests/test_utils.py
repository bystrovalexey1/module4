import pytest
from src.utils import read_json, data_from_json


def test_read_json(filename):
    assert read_json(filename)[1] == {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }


def test_read_json_empty(empty_list):
    assert read_json(empty_list) == 'Нет данных для чтения'

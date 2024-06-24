import requests
import allure
import pytest
import unittest

BASE_URL = "https://web-gate.chitai-gorod.ru/api/v1"
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTg1NTUxNzgsImlhdCI6MTcxODM4NzE3OCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImMxYWQzYWFlN2NlZGE0NWVkNTE2NWNjYzM5NThiYTdlNDA0NjEwZjRmMDk1OGIyNTAyOGU2M2YxNDYwZjMyYWUiLCJ0eXBlIjoxMH0.bGnqNUZ0Btx-9_Vq2cdwVDVhUWuhNnPOD6fkdJt4zuQ"
book_id = "master-i-margarita-3018590"

@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"



@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_book_by_id():
    book_id = "master-i-margarita-3018590"    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/products/slug/{book_id}", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Булгаков" in response.text
    
@allure.feature("API")
@allure.story("Поиск книг на кириллице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_rus():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=мастер и маргарита", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Поиск книг на латинице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_eng():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=phyton", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Символы юникода")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_unicode_symbols():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=✉ § © ☯ ☭ ? $ £ ¢", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_space():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=   ", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Получение списка книг по категории")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_category_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?forceFilters[categories]=110282", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг по фильтрам")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_filtres_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?filters[onlyNew]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"      


@allure.feature("API")
@allure.story("Получение списка книг по автору")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_books_by_author():      
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products/facet?filters[authors]=593251", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 

@allure.feature("API")
@allure.story("Получение списка книг по наличию")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_available_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products/facet?filters[onlyAvailable]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 

@allure.feature("API")
@allure.story("Добавление книги в корзину")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_add_book_to_cart():
    data = {
        "id": '3018590',
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.post(f"{BASE_URL}/cart/product", json=data, headers=headers)
    assert response.status_code == 400, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка товаров в корзине")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/cart", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Удаление книги из корзины")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_del_book_from_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.delete(f"{BASE_URL}/cart", headers=headers)
    assert response.status_code == 204, f"Ожидался статус-код 200, но получен {response.status_code}"
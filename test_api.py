import requests
import allure
import pytest

# BASE_URL = "https://www.chitai-gorod.ru/"
# BASE_URL = 
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2/"
Bearer = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTgzODA1NTAsImlhdCI6MTcxODIxMjU1MCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg1NmEyNjQ0NjZiYjA2Y2RlOGNiMzc4ZWNiNjc4MTM1ZmY2Yzk0MmE1NDI0Yjg0MzM1YmQxY2U4YjY1Y2I1ZTIiLCJ0eXBlIjoxMH0.UP79_uyJ3yb7nOPKIeIz3CWf58KBez1knlrqleWekM0"

@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_books():
    response = requests.get("{BASE_URL_2}products" headers = headers)
    headers = {
          'content-type' : 'application/json',
          'authorization' : 'Bearer'
            }
    assert response.status_code == 200


@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_book_by_id():
    book_id = 3018590
    response = requests.get(f"{BASE_URL}/products/{book_id}")
    assert response.status_code == 404

@allure.feature("API")
@allure.story("Поиск книг")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_rus():
    search_query = "Мастер и Маргарита"
    response = requests.get(f"{BASE_URL}/products", params={"search": search_query})
    assert response.status_code == 200

@allure.feature("API")
@allure.story("Поиск книг")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_eng():
    search_query = "Python"
    response = requests.get(f"{BASE_URL}/products", params={"search": search_query})
    assert response.status_code == 200

@allure.feature("API")
@allure.story("Пустое поле")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_empty():
    search_query = ""
    response = requests.get(f"{BASE_URL}/products", params={"search": search_query})
    assert response.status_code == 200


@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_space():
    search_query = "   "
    response = requests.get(f"{BASE_URL}/products", params={"search": search_query})
    assert response.status_code == 200

@allure.feature("API")
@allure.story("Получение списка книг по категории")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_category_books():
        my_params = {
        "genre": "nauka-tekhnika-it-110282",
        "page": 1,
        "limit": 10
    }
        response = requests.get(f"{BASE_URL}/catalog/books", params=my_params)
        assert response.status_code == 200

@allure.feature("API")
@allure.story("Получение списка книг по фильтрам")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_filtres_books():
        filter_params = {
        "filters": "onlyNew",
        "page": 1,
        "limit": 10
    }
        response = requests.get(f"{BASE_URL}/products", params=filter_params)
        assert response.status_code == 200        


@allure.feature("API")
@allure.story("Получение списка книг по автору")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_books_by_author():      
        author_params = {
        "filters": "filters[authors]=593251",
        "page": 1,
        "limit": 10
    }
        response = requests.get(f"{BASE_URL}/products", params=author_params)
        assert response.status_code == 200

@allure.feature("API")
@allure.story("Получение списка книг по наличию")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_available_books():
        available_filter_params = {
        "filters": "onlyAvailable",
        "page": 1,
        "limit": 10
    }
        response = requests.get(f"{BASE_URL}/products", params=available_filter_params)
        assert response.status_code == 200  
   



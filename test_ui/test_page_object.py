import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Проверка загрузки главной страницы")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitai_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()

@allure.title("Поиск книги на кириллице")
@allure.description("Проверка получения книг на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_rus_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на кириллице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_rus_ui('Мастер и Маргарита')
        assert text [0:53] == "Показываем результаты по запросу «мастер и маргарита»"

@allure.title("Поиск книги на латинице")
@allure.description("Проверка получения книг на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_eng_ui():
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на латинице"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_book_eng_ui('Master i Margarita')
        assert text [0:53] == "Показываем результаты по запросу «master i margarita»"

@allure.title("Поиск по символам юникода")
@allure.description("Проверка поиска по символам юникода")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_search_invalid_ui():
    with allure.step("Открытие веб-страницы в Chrome, ввод символов юникода"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.search_invalid_ui('✉ § © ☯ ☭ ? $ £ ¢')
        assert text [0:28] == "Похоже, у нас такого нет"

@allure.title("Пустая корзина")
@allure.description("Проверка пустой корзины")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_get_empty_cart():
    with allure.step("Открытие веб-страницы в Chrome, заходим в корзину"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.get_empty_cart()
        assert text [0:20] == "В корзине ничего нет"       



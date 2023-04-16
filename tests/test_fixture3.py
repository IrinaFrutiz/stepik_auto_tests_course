import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# Фикстурами в PyTest'е называют функции, которые выполняются с различным scope-ом и возвращают какое-то значение либо выполняют какие-то действия.

# @pytest.fixture(scope='class', autouse=True)
# def suite_data():
#     print("\n> Suite setup")
#     yield
#     print("> Suite teardown")

# В данном примере “@pytest.fixture” — декоратор, указывающий, что функция ниже является фикстурой, “scope=’…’” указывает на “очерёдность” выполнения, а “autouse=True” говорит о том, что фикстура будет применена для каждого сьюта в тестовом фреймворке
#
# Очерёдность выполнения - их четыре: “session”, “module”, “class” и “function”. Выполняются они в такой же последовательности.
#
# Из фикстуры можно передать значение в сьют с помощью оператора yield. При этом после yield можно добавить ещё код, который будет выполнен после кейса. Таким образом можно сказать, что всё, что идёт до оператора yield является “setup”, а всё, что после — “teardown” (yield, к слову, может ничего и не возвращать, а просто будет разделителем, отделяющим сетап от тирдауна).
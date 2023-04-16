from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

#setup и teardown - ключевые слова см https://docs.pytest.org/en/latest/how-to/xunit_setup.html
class TestMainPage1():

    @classmethod #декоратор + для читаемости кода
    def setup_class(self): #важно что в названии есть _class поэтому выполняется в начале/конце всех тестов
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print(f"start test_guest_should_see_login_link")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print(f"start test_guest_should_see_basket_link_on_the_main_page")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self): #важно что в названии есть _method поэтому испольняется в начале/конце каждого теста
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print(f"start test_guest_should_see_login_link")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print(f"start test_guest_should_see_basket_link_on_the_main_page")
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
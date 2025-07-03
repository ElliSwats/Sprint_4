import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до конца страницы')
    def scroll_to_end_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Кликнуть на элемент')
    def click_by_element_by_id(self, locator):
        self.driver.find_element(By.ID, locator).click()

    @allure.step('Кликнуть на элемент')
    def click_by_element_by_xpath(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    @allure.step('принимаем куки')
    def accept_cookie(self, locator):
        self.click_by_element_by_id(locator)

    @allure.step('Получить текст элемента')
    def get_text_by_element_by_id(self, locator):
        element = self.driver.find_element(By.ID, locator)
        return element.text

    @allure.step('Получить текст элемента')
    def get_text_by_element_by_xpath(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element.text

    @allure.step('Ввести текст в поле ввода')
    def send_keys(self, locator, keys):
        element = self.driver.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(keys)

    @allure.step('Ожидание видимости элемента')
    def download_wait_by_visible_xpath(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.XPATH, locator)))

    @allure.step('Ожидание видимости элемента')
    def download_wait_by_visible_id(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.ID, locator)))

    @allure.step('Ожидание кликабельности элемента')
    def download_wait_by_clickable_xpath(self, locator):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, locator)))

    @allure.step('Ожидание url')
    def download_wait_new_url(self, expected_url):
        WebDriverWait(self.driver, 15).until(ec.url_to_be(expected_url))

    @allure.step('Переход на другое окно')
    def switch_to_window_ind(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step('Получение URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Заполняем поле данными')
    def set_placeholder(self, locator, information):
        self.driver.find_element(By.XPATH, locator).send_keys(information)

    @allure.step('Скролл до кнопки "Заказать"')
    def scroll_to_element(self, locator):
        self.download_wait_by_visible_xpath(locator)
        button_order_in_body = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", button_order_in_body)

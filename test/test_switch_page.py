import allure

from locators.order_page_locator import OrderPageLoc
from locators.main_page_locators import MainPageLoc
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import (dzen_url, main_page_url)


main_page_loc = MainPageLoc
order_page_loc = OrderPageLoc


class TestSwitchBetweenPage:

    @allure.title('Переход на "Дзен" через кнопку "Яндекс"')
    @allure.description('Проверям переход на "Дзен" при клике на конопку "Яндекс"')
    def test_switch_to_dzen_click(self, driver):
        main_page = MainPage(driver=driver)
        actual_url = main_page.switch_to_dzen(dzen_url)
        assert actual_url == dzen_url

    @allure.title('Переход на главную страницу со стораницы заказа')
    @allure.description('Проверям переход на главную страницу при клике на конопку "Самокат" в шапке страницы')
    def test_clic_to_scooter_in_header(self, driver):
        order_page = OrderPage(driver=driver)
        order_page.order_button(locator=order_page_loc.for_whom_order)
        assert order_page.get_url() == main_page_url

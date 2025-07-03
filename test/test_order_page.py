import pytest
import allure

from locators.order_page_locator import OrderPageLoc
from locators.main_page_locators import MainPageLoc
from pages.order_page import OrderPage
from data import (user_1, user_2)


order_page_loc = OrderPageLoc


class TestOrderPage:

    @allure.title('Проверка форм заказа')
    @allure.description('Проверяем запролнение форм заказа тестовыми данными')
    @pytest.mark.parametrize('loc_btn_order, user_data', [
        (MainPageLoc.order_in_head, user_1),
        (MainPageLoc.order_in_body, user_2)])
    def test_filling_out_order_form(self, driver, loc_btn_order, user_data):
        order_page = OrderPage(driver=driver)
        expected_text = 'Заказ оформлен'
        order_page.scroll_to_element(loc_btn_order)
        order_page.filling_order_form_about_user(
            loc=loc_btn_order, name=user_data['name'],
            surname=user_data['surname'], address=user_data['address'],
            subway=user_data['station'], phone=user_data['phone'])
        order_page.filling_order_form_about_rent(
            data=user_data['data'], comments=user_data['comments'])
        actual_text = order_page.completed_order()
        assert expected_text in actual_text

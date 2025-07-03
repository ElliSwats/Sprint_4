import allure
from selenium.webdriver.common.by import By

from locators.order_page_locator import OrderPageLoc
from locators.main_page_locators import MainPageLoc
from pages.base_page import BasePage


order_page_loc = OrderPageLoc
main_page_loc = MainPageLoc


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.set_placeholder(order_page_loc.loc_name, name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self, surname):
        self.set_placeholder(order_page_loc.loc_surname, surname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        self.set_placeholder(order_page_loc.loc_address, address)

    @allure.step('Заполняем поле Станция метро')
    def set_subway(self, subway):
        self.download_wait_by_clickable_xpath(order_page_loc.loc_subway)
        self.click_by_element_by_xpath(order_page_loc.loc_subway)
        self.set_placeholder(order_page_loc.loc_subway, subway)
        self.download_wait_by_visible_xpath(order_page_loc.loc_subway_value).click()

    @allure.step('Заполняем поле Телефон')
    def set_phone(self, phone):
        self.click_by_element_by_xpath(order_page_loc.loc_phone)
        self.set_placeholder(order_page_loc.loc_phone, phone)

    @allure.step('Нажимаем кнопку далее')
    def click_to_button_then(self):
        self.click_by_element_by_xpath(order_page_loc.loc_then)

    @allure.step('ожидание загрузки страницы про аренду')
    def waiting_detail_page_order(self):
        self.download_wait_by_visible_xpath(order_page_loc.loc_about_rent)

    @allure.step('заполняем поле когда привезти самокат')
    def when_delivery_order(self, data):
        self.click_by_element_by_xpath(order_page_loc.loc_when_delivery)
        self.driver.find_element(By.XPATH, order_page_loc.loc_when_delivery).send_keys(data)
        self.click_by_element_by_xpath(order_page_loc.loc_calendar)

    @allure.step('заполняем поле срок аренды')
    def choice_period_rent(self):
        self.click_by_element_by_xpath(order_page_loc.loc_period_rent)
        self.download_wait_by_visible_xpath(order_page_loc.calendar).click()

    @allure.step('выбираем цвет самоката серый')
    def choice_colour_scooter_grey(self):
        self.click_by_element_by_xpath(order_page_loc.loc_color_choice)

    @allure.step('заполняем поле комментарий')
    def placeholder_comments(self, comments):
        self.set_placeholder(order_page_loc.loc_comments, comments)

    @allure.step('нажимаем кнопку "заказать"')
    def push_button_order(self):
        self.click_by_element_by_xpath(order_page_loc.button_order)

    @allure.step('ожидаем появления окна подтверждения заказа')
    def wait_window_order_accept(self):
        self.download_wait_by_visible_xpath(order_page_loc.would_you_like_order)

    @allure.step('Нажимаем кнопку "Да" в окне подтверждения заказа')
    def push_button_yes_order(self):
        self.click_by_element_by_xpath(order_page_loc.yes_button_order_window)

    @allure.step('Заполнение формы заказа в разделе "Для кого самокат"')
    def filling_order_form_about_user(self, loc, name, surname, address, subway, phone):
        self.accept_cookie(main_page_loc.cookie_id)
        self.click_by_element_by_xpath(loc)
        self.download_wait_by_visible_xpath(order_page_loc.for_whom_order)
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone(phone)
        self.click_to_button_then()

    @allure.step('Заполнение формы заказа в разделе "Про ареду"')
    def filling_order_form_about_rent(self, data, comments):
        self.waiting_detail_page_order()
        self.when_delivery_order(data)
        self.choice_period_rent()
        self.choice_colour_scooter_grey()
        self.placeholder_comments(comments)
        self.push_button_order()
        self.wait_window_order_accept()
        self.push_button_yes_order()

    @allure.step('ожидаем появления окна "Заказ оформлен"')
    def completed_order(self):
        self.download_wait_by_visible_xpath(order_page_loc.order_has_been_placed)
        actual_text = self.get_text_by_element_by_xpath(order_page_loc.order_has_been_placed)
        return actual_text

    @allure.step('нажимаем кнопку "Самокат" в шапке страницы')
    def push_button_scooter(self):
        self.click_by_element_by_xpath(order_page_loc.loc_scooter)

    @allure.step('Переход в форму заказа по кнопке "Заказть" в шапке страницы')
    def order_button(self, locator):
        self.click_by_element_by_id(main_page_loc.cookie_id)
        self.click_by_element_by_xpath(main_page_loc.order_in_head)
        self.download_wait_by_visible_xpath(locator)
        self.click_by_element_by_xpath(order_page_loc.loc_scooter)

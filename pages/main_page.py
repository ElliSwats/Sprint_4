import allure
from locators.main_page_locators import MainPageLoc
from pages.base_page import BasePage


main_page_loc = MainPageLoc


class MainPage(BasePage):

    @allure.step('Поочередно открываем вопросы и получаем текст их ответов')
    def click_to_question(self, loc_question, loc_answer):
        self.accept_cookie(main_page_loc.cookie_id)
        self.scroll_to_end_page()
        self.download_wait_by_visible_id(loc_question)
        self.click_by_element_by_id(loc_question)
        self.download_wait_by_visible_id(loc_answer)
        actual_text = self.get_text_by_element_by_id(loc_answer)
        return actual_text

    @allure.step('Переход на Дзен по кнопке "Яндекс" в шапке страницы')
    def switch_to_dzen(self, expected_url):
        self.click_by_element_by_xpath(main_page_loc.yandex_by_xpath)
        self.switch_to_window_ind(1)
        self.download_wait_new_url(expected_url)
        return self.get_url()

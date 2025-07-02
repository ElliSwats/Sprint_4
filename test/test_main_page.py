import pytest
import allure

from locators.main_page_locators import MainPageLoc
from locators.order_page_locator import OrderPageLoc
from data import (TextAnswers, list_param_ans_quest)
from pages.main_page import MainPage


main_page_loc = MainPageLoc
order_page_loc = OrderPageLoc
text_answer = TextAnswers


class TestMainPage:

    @allure.description('При клике на вопрос сравниваем фактический ответ на вопрос с ожидаемым')
    @pytest.mark.parametrize('loc_question, loc_answer, fact_answer_text', list_param_ans_quest)
    def test_get_answer_on_question(self, driver, loc_question, loc_answer, fact_answer_text):
        main_page = MainPage(driver=driver)
        actual_text = main_page.click_to_question(loc_question, loc_answer)
        assert actual_text == fact_answer_text

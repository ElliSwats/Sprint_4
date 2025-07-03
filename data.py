from dataclasses import dataclass
from locators.main_page_locators import MainPageLoc


main_page_loc = MainPageLoc


@dataclass
class TextAnswers:
    how_much_pay: str = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    several_scooters: str = (
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
        'можете просто сделать несколько заказов — один за другим.')
    time_rent_calculated: str = ('Допустим, вы оформляете заказ на 8 мая. '
                                 'Мы привозим самокат 8 мая в течение дня. '
                                 'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                                 'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    order_today: str = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    extend_return: str = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')
    charger_with_scooter: str = ('Самокат приезжает к вам с полной зарядкой. '
                                 'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                                 'Зарядка не понадобится.')
    possible_cancel_order: str = ('Да, пока самокат не привезли. Штрафа не будет, '
                                  'объяснительной записки тоже не попросим. Все же свои.')
    outside_moscow_ring_road: str = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


text_answer = TextAnswers

list_param_ans_quest = [
        (main_page_loc.how_much_and_how_pay_id,
         main_page_loc.per_day_payment_id,
         text_answer.how_much_pay),
        (main_page_loc.want_several_is_it_possible_id,
         main_page_loc.one_order_one_scooter_id,
         text_answer.several_scooters),
        (main_page_loc.how_time_calculated_id,
         main_page_loc.time_current_id,
         text_answer.time_rent_calculated),
        (main_page_loc.possible_order_today_id,
         main_page_loc.start_tomorrow_id,
         text_answer.order_today),
        (main_page_loc.extend_or_return_scooter_id,
         main_page_loc.not_yet_call_support_id,
         text_answer.extend_return),
        (main_page_loc.charger_with_scooter_id,
         main_page_loc.full_charge_id,
         text_answer.charger_with_scooter),
        (main_page_loc.possible_cancel_order_id,
         main_page_loc.cancel_until_scooter_arrives_id,
         text_answer.possible_cancel_order),
        (main_page_loc.bring_outside_moscow_ring_road_id,
         main_page_loc.moscow_and_regions_id,
         text_answer.outside_moscow_ring_road)
    ]

user_1 = {
    'name': 'Василий',
    'surname': 'Васечкин',
    'address': 'Москва, ул. Вавилова. д. 3',
    'station': 'Комсомольская',
    'phone': '89993334455',
    'data': '10.07.2025',
    'comments': 'покатаемся'
}
user_2 = {
    'name': 'Тузий',
    'surname': 'Тузевич',
    'address': 'Москва, ул. Неглинная. д. 4',
    'station': 'Сокольники',
    'phone': '89995556633',
    'data': '10.07.2025',
    'comments': 'а может и нет'
}

dzen_url = 'https://dzen.ru/?yredirect=true'
order_url = 'https://qa-scooter.praktikum-services.ru/order'
main_page_url = 'https://qa-scooter.praktikum-services.ru/'

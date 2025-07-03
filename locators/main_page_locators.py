from dataclasses import dataclass


@dataclass
class MainPageLoc:
    # куки
    cookie_id: str = 'rcc-confirm-button'
    # Вопросы
    # Сколько это стоит? И как оплатить?
    how_much_and_how_pay_id: str = 'accordion__heading-0'
    # Хочу сразу несколько самокатов! Так можно?
    want_several_is_it_possible_id: str = 'accordion__heading-1'
    # Как рассчитывается время аренды?
    how_time_calculated_id: str = 'accordion__heading-2'
    # Можно ли заказать самокат прямо на сегодня?
    possible_order_today_id: str = 'accordion__heading-3'
    # Можно ли продлить заказ или вернуть самокат раньше?
    extend_or_return_scooter_id: str = 'accordion__heading-4'
    # Вы привозите зарядку вместе с самокатом?
    charger_with_scooter_id: str = 'accordion__heading-5'
    # Можно ли отменить заказ?
    possible_cancel_order_id: str = 'accordion__heading-6'
    # Я жизу за МКАДом, привезёте?
    bring_outside_moscow_ring_road_id: str = 'accordion__heading-7'
    # Сутки — 400 рублей. Оплата курьеру — наличными или картой.

    # ответы
    per_day_payment_id: str = 'accordion__panel-0'
    # Пока что у нас так: один заказ — один самокат.
    one_order_one_scooter_id: str = 'accordion__panel-1'
    # Допустим, вы оформляете заказ на 8 мая.
    time_current_id: str = 'accordion__panel-2'
    # Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    start_tomorrow_id: str = 'accordion__panel-3'
    # Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    not_yet_call_support_id: str = 'accordion__panel-4'
    # Самокат приезжает к вам с полной зарядкой.
    full_charge_id: str = 'accordion__panel-5'
    # Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
    cancel_until_scooter_arrives_id: str = 'accordion__panel-6'
    # Да, обязательно. Всем самокатов! И Москве, и Московской области.
    moscow_and_regions_id: str = 'accordion__panel-7'

    # Дзен
    yandex_by_xpath: str = '//img[@alt="Yandex"]'
    # вернхняя кнопка заказать
    order_in_head: str = "//button[@class='Button_Button__ra12g']"
    # Нижняя кнопка заказать
    order_in_body: str = "//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']"

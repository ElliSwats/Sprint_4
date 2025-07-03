from dataclasses import dataclass


@dataclass
class OrderPageLoc:
    # Для кого самокат
    for_whom_order: str = "//div[@class='Order_Header__BZXOb']"
    # локатор ввода имени
    loc_name: str = "//input[@placeholder='* Имя']"
    # локатор ввода фамилии
    loc_surname: str = "//input[@placeholder='* Фамилия']"
    # Локатор ввода адреса
    loc_address: str = "//input[@placeholder='* Адрес: куда привезти заказ']"
    # Локатор станции метро
    loc_subway: str = "//input[@placeholder='* Станция метро']"
    # Локатор станции метро
    loc_subway_value: str = "//*[@class ='select-search__select']"
    # Локатор телефона
    loc_phone: str = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Локатор кнопки далее
    loc_then: str = '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    # локатор надписи "про аренду"
    loc_about_rent: str = "//div[@class='Order_Header__BZXOb']"
    # локатор ввода когда привезти заказ
    loc_when_delivery: str = "//input[@placeholder='* Когда привезти самокат']"
    # локатор календаря
    loc_calendar: str = "//div[@class='react-datepicker__day react-datepicker__day--010 react-datepicker__day--selected' and text()='10']"
    # локатор выпадающего календаря
    calendar: str = "//*[text()='сутки']"
    # локатор ввода поля период
    loc_period_rent: str = "//div[@class='Dropdown-root']"
    # Локатор выбора цвета
    loc_color_choice: str = "//input[@id='grey' and @type='checkbox']"
    # Локатор поля комментарий для курьера
    loc_comments: str = "//input[@placeholder='Комментарий для курьера']"
    # Локатор кнопки заказать
    button_order: str = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    # Локатор окна подветрждения заказа
    would_you_like_order: str = "//div[@class='Order_Modal__YZ-d3']"
    # локатор кнопки "Да" на окна подтверждения заказа
    yes_button_order_window: str = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    # локатор сообщения "заказ оформлен"
    order_has_been_placed: str = "//div[@class='Order_ModalHeader__3FDaJ']"
    # Локатор кнопки "Самокат" в шапке
    loc_scooter = "//img[@alt='Scooter']"

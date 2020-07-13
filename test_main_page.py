from time import sleep
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_basket_button(browser):
    browser.get(link)
    sleep(5) #sleep для проверки инициализации браузера
    add_to_basket = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(add_to_basket) > 0
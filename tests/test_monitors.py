import time

from pages.homepage import HomePage


def test_monitors(browser):
    mon1 = HomePage(browser)
    mon1.open()
    mon1.click_monitor()
    time.sleep(3)
    mon1.check_products_count(2)


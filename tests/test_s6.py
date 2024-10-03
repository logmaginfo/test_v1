from pages.homepage import HomePage
from pages.product import ProductPage

def test_s6(browser):
    s6 = HomePage(browser)
    s6.open()
    s6.click_galaxy_s6()

    s62 = ProductPage(browser)
    s62.check_title_is("Samsung galaxy s6")

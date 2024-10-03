from selenium import webdriver # импорт браузера
import pytest
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()  # открываем браузер
    # browser.maximize_window() # открываем окно на максимум
    browser.implicitly_wait(3) # если проблемы подожди
    yield browser
    ## browser.close()
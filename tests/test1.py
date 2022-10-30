import time

def test_1(selenium):
    selenium.get('https://pikabu.ru/')
    time.sleep(5)

    #assert selenium.find_element('xpath', '/html/body/div[1]/header/div[2]/div').is_displayed(), "WARRNING nbl"




'''
import adress
import time
from selenium.webdriver.support.ui import WebDriverWait



def test_1(selenium):
    #selenium.implicitly_wait(10)
    selenium.get(adress)


    login = selenium.find_element('xpath', '//*[@id="name"]')
    login.send_keys('loginName')

    element = WebDriverWait(selenium, 10).until(selenium.find_element('xpath', '//*[@id="email"]'))


    Ma = selenium.find_element('xpath', '//*[@id="email"]')
    Ma.send_keys('pass12332@ff')

    Ps = selenium.find_element('xpath', '//*[@id="pass"]')
    Ps.send_keys('pass12332')

    btn = selenium.find_element('xpath', '/html/body/div/div/form/div[4]/button')
    btn.click()


    time.sleep(3)

    assert selenium.find_element('xpath', '//h1').is_displayed(), "WARRNING visbl"


'''

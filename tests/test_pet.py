import pytest
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.core import driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\\project\\chromedriver.exe')
    # Переходим на страницу регистрации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    pytest.driver.implicitly_wait(10)
    # Вводим мыло
    pytest.driver.find_element('id', 'email').send_keys('lbtumatym1@gmail.com')
    # Вводим пароль
    pytest.driver.find_element('id', 'pass').send_keys('1227341d')
    # Нажимаем кнопку входа в аккаунт
    pytest.driver.find_element('css selector', 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователяx
    assert pytest.driver.find_element('tag name', 'h1').text == "PetFriends"

    images = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    names = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements('css selector', '.card-deck .card-img-top')

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located(("css selector", ".card-deck .card-img-top"))
    )

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''  # на странице нет питомцев без фото
        assert names[i].text != ''  # на странице нет питомцев без Имени
        assert descriptions[i].text != ''  # на странице нет питомцев с пустым полем для указания Породы и возраста
        assert ', ' in descriptions[i]  # проверяем, что между породой и лет есть запятая (значит есть оба значения)
        parts = descriptions[i].text.split(", ")  # Создаём список, где разделитель значений - запятая
        assert len(parts[0]) > 0  # Проверяем, что длина текста в первой части списка и
        assert len(parts[1]) > 0  # ...и во второй > 0, значит там что-то да указано! Если нет -> FAILED!

    assert driver.find_element('tag name', 'h1').text == "PetFriends"  # Проверяем, что мы были на главной
    # есть утверждение для проверки заголовка страницы, что <title> Label содержит текст «PetFriends»:
    assert 'PetFriends' in driver.title  # да, работает

import time
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# first test

link = "http://selenium1py.pythonanywhere.com/ru/"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

browser.find_element_by_css_selector('#language_selector div select')
assert browser.find_element_by_css_selector('#language_selector .btn.btn-default').text == 'Выполнить'
browser.find_element_by_css_selector('#login_link')
assert browser.find_element_by_css_selector('.page_inner .col-sm-7.h1 a').text == 'Oscar'
assert browser.find_element_by_css_selector('.page_inner .col-sm-7.h1 small').text == 'Sandbox'
assert browser.find_element_by_css_selector('.page_inner .basket-mini strong').text == 'Всего в корзине:'
funt = browser.find_element_by_css_selector('.page_inner .basket-mini').text
assert funt[-20] == '£'
assert browser.find_element_by_css_selector('.page_inner .basket-mini a').text == 'Посмотреть корзину'
browser.find_element_by_css_selector('.page_inner .basket-mini button')
assert browser.find_element_by_css_selector('#browse a').text == 'Просмотр магазина'
browser.find_element_by_css_selector('#id_q')
browser.find_element_by_css_selector('.navbar-collapse .btn.btn-default')

browser.quit()


# second test

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

browser.find_element_by_css_selector('#login_link').click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#register_form button')))
browser.find_element_by_css_selector('#id_login-username')
browser.find_element_by_css_selector('#id_login-password')
assert browser.find_element_by_css_selector('#login_form a').text == 'Я забыл пароль'
browser.find_element_by_css_selector('#login_form > button')

browser.find_element_by_css_selector('#id_registration-email')
browser.find_element_by_css_selector('#id_registration-password1')
browser.find_element_by_css_selector('#id_registration-password2')
assert browser.find_element_by_css_selector('#register_form button').text == 'Зарегистрироваться'
browser.quit()


# third test

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

browser.find_element_by_css_selector('#login_link').click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#register_form button')))
browser.find_element_by_css_selector('#id_login-username').send_keys('qwer@qwer.ri')
browser.find_element_by_css_selector('#id_login-password').send_keys('2020varakin2020')
browser.find_element_by_css_selector('#login_form > button').click()
assert browser.find_element_by_css_selector('#messages div div').text == 'Рады видеть вас снова'
browser.quit()


# fourth test

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

browser.find_element_by_css_selector('#login_link').click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#register_form button')))
name = time.strftime("%Y%m%d%H%M", time.localtime())
browser.find_element_by_css_selector('#id_registration-email').send_keys(name + '@qwer.ru')
browser.find_element_by_css_selector('#id_registration-password1').send_keys('2020varakin2020')
browser.find_element_by_css_selector('#id_registration-password2').send_keys('2020varakin2020')
browser.find_element_by_css_selector('#register_form button').click()
assert browser.find_element_by_css_selector('#messages div div').text == 'Спасибо за регистрацию!'
browser.quit()


# fifth test

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

browser.find_element_by_css_selector('#browse li a').click()
# проверка пунктов в общем меню
assert browser.find_element_by_css_selector('#browse li ul li:nth-child(1) a').text == 'Все товары'
assert browser.find_element_by_css_selector('#browse li ul li:nth-child(3) a').text == 'Одежда'
assert browser.find_element_by_css_selector('#browse li ul li.dropdown-submenu a').text == 'Книги'
assert browser.find_element_by_css_selector('#browse li ul li:nth-child(6) a').text == 'Предложения'
# клик по пункту "Все товары"
browser.find_element_by_css_selector('#browse li ul li:nth-child(1) a').click()
# ожидание появления надписи "Начало"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.container-fluid.page div ul li:nth-child(1) a'), 'Начало'))
assert browser.find_element_by_css_selector('.container-fluid.page .page-header.action h1').text == 'Все товары'
# создание массива товаров
all_item = browser.find_elements_by_css_selector('.container-fluid.page div div div section div .row li')
assert len(all_item) != 0
# проверка, что у всех товаров есть кнопка с надписью "добавить в корзину"
for i in all_item:
    assert browser.find_element_by_css_selector('.product_price button').text == 'Добавить в корзину'
# переход на главную страницу
browser.find_element_by_css_selector('.container-fluid.page div ul li:nth-child(1) a').click()
assert "Oscar - Sandbox" == browser.title
# клик по кнопке "просмотр магазина"
browser.find_element_by_css_selector('#browse li a').click()
# клик по пункту "Одежда"
browser.find_element_by_css_selector('#browse li ul li:nth-child(3) a').click()
# ожидание загрузки надписи "Одежда"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#default .container-fluid.page .page-header.action h1'), 'Одежда'))
# создание массива с элементами одежды
all_clothes = browser.find_elements_by_css_selector('.container-fluid.page div div div section div .row li')
assert len(all_clothes) != 0
for i in all_clothes:
    assert browser.find_element_by_css_selector('.product_price button').text == 'Добавить в корзину'
# переход на главную страницу
browser.find_element_by_css_selector('.container-fluid.page div ul li:nth-child(1) a').click()
assert "Oscar - Sandbox" == browser.title
# клик по кнопке "просмотр магазина"
browser.find_element_by_css_selector('#browse li a').click()
# клик по пункту "Книги"
browser.find_element_by_css_selector('#browse li ul .dropdown-submenu').click()
# ожидание отображения надписи "Начало"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.container-fluid.page div ul li:nth-child(1) a'), 'Начало'))
assert browser.find_element_by_css_selector('#default .container-fluid.page .page-header.action h1').text == 'Книги'
# создание массива книг
all_books = browser.find_elements_by_css_selector('.container-fluid.page div div div section div .row li')
assert len(all_books) != 0
# проверка, что у всех товаров есть кнопка с надписью "добавить в корзину"
for i in all_books:
    assert browser.find_element_by_css_selector('.product_price button').text == 'Добавить в корзину'
# переход на главную страницу
browser.find_element_by_css_selector('.container-fluid.page div ul li:nth-child(1) a').click()
assert "Oscar - Sandbox" == browser.title
# клик по кнопке "просмотр магазина"
browser.find_element_by_css_selector('#browse li a').click()
# клик по пункту "Предложения"
browser.find_element_by_css_selector('#browse li ul li:nth-child(6) a').click()
# ожидание отображения надписи "Начало"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.container-fluid.page div ul li:nth-child(1) a'), 'Начало'))
assert browser.find_element_by_css_selector('.container-fluid.page .page-header.action h1').text == 'Предложения'
# создание массива предолжений
all_offer = browser.find_elements_by_css_selector('#content_inner ul:nth-child(3) li')
assert len(all_offer) != 0
# проверка, что у всех товаров есть кнопка с надписью "добавить в корзину"
for i in all_offer:
    assert browser.find_element_by_css_selector('.product_price button').text == 'Добавить в корзину'
browser.close()


# sixth test

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(20)
browser.maximize_window()
wait = WebDriverWait(browser, 20)

# ввод в поле поиска символа "handbook"
browser.find_element_by_css_selector('#id_q').send_keys('handbook')
# нажатие на кнопку "поиск"
browser.find_element_by_css_selector('.navbar.primary.navbar-static-top.navbar-inverse .navbar-collapse.primary-collapse.collapse .btn.btn-default').click()
# ожидание подгрузки списка - пункт "Найти" после "Начало"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#default .container-fluid.page div ul li:nth-child(2)'), 'Найти'))
# создание массива из найденных элементов
list_find = browser.find_elements_by_css_selector('#default .container-fluid.page div div div section div ol li')
assert len(list_find) != 0
browser.close()



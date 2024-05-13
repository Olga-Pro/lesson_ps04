# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
#
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
#     - листать параграфы текущей статьи;
#     - перейти на одну из связанных страниц — и снова выбор из двух пунктов:
#           - листать параграфы статьи;
#           - перейти на одну из внутренних статей.
#     - выйти из программы.
from selenium import webdriver
from selenium.webdriver import Keys  # Для имитации клавиатуры
from selenium.webdriver.common.by import By  # Для поиска элементов на сайте

import time
import random

def read_paragraph():
    # Листать параграфы статьи
    browser.get(url)
    paragraphs = browser.find_elements(By.TAG_NAME, "p")  # ищем все тэги "p"
    for paragraph in paragraphs:  # Выводим статьи подряд, по нажатию enter
        print(paragraph.text)
        input()

def read_random_hatnote():
    # Перейти на одну из связанных страниц
    browser.get(url)  # Страница по запросу пользователя

    hatnotes = []  # Список всех статей по тэгу "div"

    for element in browser.find_elements(By.TAG_NAME, "div"):
        my_class = element.get_attribute("class")
        if my_class == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    hatnote = random.choice(hatnotes)  # Случайная статья
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")  # Ссылка
    browser.get(link)



user_text = input("Введите запрос для поиска в Википедии: ")

browser = webdriver.Chrome()  # Объект браузера
# Заглавная страница Википедии:
url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
browser.get(url)
search_box = browser.find_element(By.ID, "searchInput")  # Найти окно поиска на сайте
search_box.send_keys(user_text)  # Ввод текста в окно поиска на сойте
search_box.send_keys(Keys.RETURN)  # Нажать Enter для поиска
time.sleep(5)
a = browser.find_element(By.LINK_TEXT, user_text)  # Найти первый попавшийся элемент по запросу пользователя
a.click()  # Клик на элемент
time.sleep(5)

#url = browser.current_url
#print(url)

user_choice1 = input("1/2/3 ").strip()

match user_choice1:
    case "1":
        read_paragraph()
    case "2":
        read_random_hatnote()
        user_choice2 = input("1/2")
        match user_choice2:
            case 1:
                read_paragraph()
            case 2:
                read_random_hatnote()
    case 3:
        pass

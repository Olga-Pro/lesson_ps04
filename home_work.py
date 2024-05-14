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
from selenium.common.exceptions import NoSuchElementException  # Исключение в случае "Элемент не найден"

import time
import random

def read_paragraph():
    # Листать параграфы статьи
    browser.get(url)
    paragraphs = browser.find_elements(By.TAG_NAME, "p")  # ищем все тэги "p"
    for paragraph in paragraphs:  # Выводим статьи подряд, по нажатию enter
        print(paragraph.text)
        user_choice = input("\nНажмите Enter для продолжения или 0 для выхода: ")
        if user_choice.strip() == "0":
            print("Просмотр статьи завершен.")
            break

def read_random_hatnote():
    # Перейти на одну из связанных страниц
    browser.get(url)  # Страница по запросу пользователя

    hatnotes = []  # Список всех статей по тэгу "div"

    for element in browser.find_elements(By.TAG_NAME, "div"):
        my_class = element.get_attribute("class")
        if my_class == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    if hatnotes != []:
        hatnote = random.choice(hatnotes)  # Случайная статья
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")  # Ссылка
        browser.get(link)
        time.sleep(5)
        title_page = browser.find_element(By.ID,"firstHeading").text
        print(f"\nНайдена статья: {title_page}")
        return True
    else:
        print("Связанные статьи не найдены")
        return False



user_text = input("Введите запрос для поиска в Википедии: ")

browser = webdriver.Chrome()  # Объект браузера
try:
    # Заглавная страница Википедии:
    url = "https://ru.wikipedia.org"
    browser.get(url)
    search_box = browser.find_element(By.ID, "searchInput")  # Найти окно поиска на сайте
    search_box.send_keys(user_text)  # Ввод текста в окно поиска на сойте
    search_box.send_keys(Keys.RETURN)  # Нажать Enter для поиска
    time.sleep(5)
    link_element = browser.find_element(By.LINK_TEXT, user_text)  # Найти первый попавшийся элемент по запросу пользователя
    link_element.click()  # Клик на элемент
    time.sleep(5)

    url = browser.current_url  # url текущей страницы
    browser.get(url)  # Перезазрузить данные из текущей страницы
    time.sleep(5)
    assert "Википедия" in browser.title

    print("\nВыберите действие:")
    print("1: Показать параграфы статьи")
    print("2: Показать одну из связанных статей")
    print("3: Выйти из программы")
    user_choice1 = input("Ваш выбор: ").strip()


    match user_choice1:
        case "1":
            read_paragraph()
        case "2":
            if read_random_hatnote():
                print("\nВыберите следующее действие:")
                print("1: Показать параграфы статьи")
                print("2: Показать одну из связанных статей")

                user_choice2 = input("Ваш выбор: ").strip()

                # print(browser.current_url)
                url = browser.current_url
                browser.get(url)
                time.sleep(5)

                match user_choice2:
                    case "1":
                        read_paragraph()
                    case "2":
                        read_random_hatnote()
        case "3":
            browser.quit()
except AssertionError:
    # Иногда почему-то происходит переход по ссылкам из источников информации
    # на другие сайты
    print("Ошибка перехода. Не Википедия.")
    print(browser.current_url)

except NoSuchElementException:
    print(f"По запросу '{user_text}' статьи не найдены.")
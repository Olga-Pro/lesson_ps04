from selenium import webdriver
import time

from selenium.webdriver import Keys  # Для имитации клавиатуры
from selenium.webdriver.common.by import By  # Для поиска элементов на сайте

# Объект браузера
browser = webdriver.Chrome()

# Настройка возможности зайти на сайт
# url = "https://en.wikipedia.org/wiki/Document_Object_Model"
# browser.get(url)
# browser.save_screenshot("dom.png")
# time.sleep(10)  # Задержка 10 секунд
# browser.quit()  # Закрыть сайт

url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
browser.get(url)
assert "Википедия" in browser.title  # Проверить наличие слова Википедия в заголовке
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")  # Найти окно поиска на сайте
search_box.send_keys("Солнечная система")  # Ввод текста в окно поиска на сойте
search_box.send_keys(Keys.RETURN)  # Нажать Enter для поиска
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, "Солнечная система")  # Найти первый попавшийся элемент Солнечная система
a.click()  # Клик на элемент
time.sleep(5)
browser.quit()  # Закрыть сайт

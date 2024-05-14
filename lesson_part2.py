# Материал урока
from selenium import webdriver
import time

from selenium.webdriver import Keys  # Для имитации клавиатуры
from selenium.webdriver.common.by import By  # Для поиска элементов на сайте

# Объект браузера
browser = webdriver.Chrome()

url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0"
browser.get(url)  # Страница с Солнечной системой

paragraphs = browser.find_elements(By.TAG_NAME, "p")  # ищем все тэги "p"
for paragraph in paragraphs:  # Выводим статьи подряд, по нажатию enter
    print(paragraph.text)
    input()


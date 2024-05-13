from selenium import webdriver
import time
import random

from selenium.webdriver import Keys  # Для имитации клавиатуры
from selenium.webdriver.common.by import By  # Для поиска элементов на сайте

# Объект браузера
browser = webdriver.Chrome()

url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0"
browser.get(url)  # Страница с Солнечной системой

hatnotes = []  # Список всех статей по тэгу "div"

for element in browser.find_elements(By.TAG_NAME, "div"):
    my_class = element.get_attribute("class")
    if my_class == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)

hatnote = random.choice(hatnotes)  # Случайная статья
print(hatnote)
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")  # Ссылка
print(link)
browser.get(link)
time.sleep(5)




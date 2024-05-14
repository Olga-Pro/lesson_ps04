# Использование `WebDriverWait` и ожиданий условий (Expected Conditions)
# позволяет более точно и надежно ожидать выполнения определенных условий
# на веб-странице. Это особенно полезно при работе с динамически загружаемыми элементами.
#
# Вот пример использования `WebDriverWait` для ожидания загрузки элементов на странице в вашем сценарии:
# # 1. Импортирование необходимых модулей.
# 2. Использование `WebDriverWait` для ожидания появления элементов.
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создание экземпляра браузера
browser = webdriver.Chrome()

# Открытие страницы Википедии
url = "https://ru.wikipedia.org"
browser.get(url)

# Нахождение и использование поля поиска
search_box = browser.find_element(By.ID, "searchInput")
user_text = "Пример текста для поиска"  # Пример текста для поиска
search_box.send_keys(user_text)
search_box.send_keys(Keys.RETURN)

# Ожидание загрузки результатов поиска
try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, user_text))
    )
    # Нажатие на ссылку, соответствующую тексту поиска
    a = browser.find_element(By.LINK_TEXT, user_text)
    a.click()

    # Ожидание загрузки новой страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "some_element_id"))  # Укажите ID элемента, который должен загрузиться на новой странице
    )

    # Получение URL текущей страницы
    current_url = browser.current_url
    print(current_url)

finally:
    # Закрыть браузер
    browser.quit()
# В этом примере:
#
# 1. `WebDriverWait` создается с таймаутом в 10 секунд.
# 2. `until` метод используется для ожидания, пока элемент с указанным текстом ссылки не станет доступным.
# 3. После клика на ссылку, снова используется `WebDriverWait` для ожидания,
# пока загрузится новый элемент на новой странице.
#
# Если вы точно не знаете, какой элемент должен загрузиться на новой странице,
# вы можете использовать более общие условия, такие как `EC.title_contains`
# для проверки наличия текста в заголовке страницы.
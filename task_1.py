import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

try:
    def calc(x):
    	return str(math.log(abs(12*math.sin(int(x)))))

    # Открытие веб-страницы
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Ожидание, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    

    # Вводим ответ
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(y)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()


    # Добавьте задержку, если необходимо, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрытие драйвера
    browser.quit()

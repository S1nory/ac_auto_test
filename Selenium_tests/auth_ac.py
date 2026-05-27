import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Загружаем конфигурацию из файла
with open('internal.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 2. Извлекаем логин и пароль
val_login = config['login_stepik']
val_password = config['password_stepik']

# 3. Основной код теста
try:
    link = "https://demo01.avroraos.ru/emm/admin/ui"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # 4. Вводим данные из конфига
    input_login = browser.find_element(By.ID, "login")
    input_login.send_keys(val_login)

    input_password = browser.find_element(By.ID, "password")
    input_password.send_keys(val_password)
    
    login_btn = browser.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
    login_btn.click()

finally:
    time.sleep(10)  # визуальная проверка результата
    browser.quit()

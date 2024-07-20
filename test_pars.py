from seleniumbase import SB
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip 
import time
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium import webdriver
from time import sleep 


def parsing_vfs(click_city):
    click_city = "mat-option-6"
    email = "sanya.khokhrin.88@list.ru"
    """Парсинг сайта и заполнения данных пользователя"""
    password = "Test2024!!!"

    with SB(uc=True, user_data_dir=r'C:\Users\максим\AppData\Local\Google\Chrome\User Data') as sb: 
        sb.driver.uc_open_with_reconnect("https://visa.vfsglobal.com/rus/ru/fra/login", reconnect_time=20)
        sb.click('h1[class="fs-21 fs-sm-24 mb-10"]')
        sb.click("input[id='mat-input-0']")
        sleep(5)

        sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
        time.sleep(16)

        sb.click("button[class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']")
        time.sleep(5)

        click_city_selector = f"mat-option[id='{click_city}']"
        print(click_city_selector)
        sb.click('mat-form-field[appearance="outline"]')
        sb.click(click_city_selector)

        time.sleep(5)        



        sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-8 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
        sb.click('mat-option[id="mat-option-20"]')
        time.sleep(5)


        sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-6 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"')
        sb.click('mat-option[id="mat-option-24"]')
        time.sleep(10)



        alert_info = sb.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-info.border-0.rounded-0.ng-star-inserted")
        last_date = alert_info.text
        return last_date
click_city = "mat-option-6"
parsing_vfs(click_city)
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
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db import ActiveOrders,Account

# Base = declarative_base()
# engine = create_engine('sqlite:///DATABASE.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)

def parsing_vfs():
    click_city = "mat-option-6"
    email = "sanya.khokhrin.88@list.ru"
    """Парсинг сайта и заполнения данных пользователя"""
    password = "Test2024!!!"

    with SB(uc=True, user_data_dir=r'C:\Users\максим\AppData\Local\Google\Chrome\User Data') as sb: 
        sb.driver.uc_open_with_reconnect("https://visa.vfsglobal.com/rus/ru/fra/login", reconnect_time=20)
        sb.click("input[id='mat-input-0']")
        time.sleep(2)
        
        sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
        time.sleep(5)

        sb.click("button[class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']")
        time.sleep(5)
 
        click_city_selector = f"mat-option[id='{click_city}']"
        print(click_city_selector)
        sb.click('mat-form-field[appearance="outline"]')
        sb.click(click_city_selector)
        
        time.sleep(5)        
        
        
        
        sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-8 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
        sb.click('mat-option[id="mat-option-20"]')
        time.sleep(10)
        
        
        sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-6 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"')
        sb.click('mat-option[id="mat-option-24"]')
        time.sleep(15)

                
                
        alert_info = sb.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-info.border-0.rounded-0.ng-star-inserted")
        last_date = alert_info.text
        return last_date
parsing_vfs()

# def parsing_vfs():
    # click_city = "mat-option-6"
#     email = "sanya.khokhrin.88@list.ru"
#     """Парсинг сайта и заполнения данных пользователя"""
#     password = "Test2024!!!"

#     with SB(uc=True, user_data_dir=r'C:\Users\максим\AppData\Local\Google\Chrome\User Data') as sb: 
#         sb.driver.uc_open_with_reconnect("https://visa.vfsglobal.com/rus/ru/fra/login", reconnect_time=20)
#         sb.click("input[id='mat-input-0']")
#         sleep(2)

        
#         sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
#         time.sleep(5)

#         sb.click("button[class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']")
#         time.sleep(5)
 
#         click_city_selector = f"mat-option[id='{click_city}']"
#         print(click_city_selector)
#         sb.click('mat-form-field[appearance="outline"]')
#         sb.click(click_city_selector)
        
#         time.sleep(5)        
        
        
        
#         sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-8 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
#         sb.click('mat-option[id="mat-option-20"]')
#         time.sleep(5)
        
        
#         sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-6 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"')
#         sb.click('mat-option[id="mat-option-24"]')
#         time.sleep(10)

                
                
#         alert_info = sb.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-info.border-0.rounded-0.ng-star-inserted")
#         last_date = alert_info.text
#         return last_date
# click_city = "mat-option-6"
# parsing_vfs()


# def parsing_vfs_filling_data():
#     session = Session()
#     # Исправление вызова метода для получения данных
#     data = session.query(ActiveOrders).all()
    
#     for entry in data:  # Перебор списка результатов
#         name = entry.name
#         surname = entry.surname
#         gender = entry.gender
#         date_of_birth = entry.date_of_birth
#         passport = entry.passport_ID
#         passport_validity_period = entry.passport_validity_period
#         number_phone = entry.number_phone
#         email = entry.email
#         click_city = entry.click_city
        
#         with SB(uc=True, user_data_dir=r'C:\Users\максим\AppData\Local\Google\Chrome\User Data') as sb: 
#             sb.driver.uc_open_with_reconnect("https://visa.vfsglobal.com/rus/ru/fra/login", reconnect_time=20)
#             sb.click("input[id='mat-input-0']")
#             sleep(5)
            
#             sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
#             sleep(5)
            
#             sb.click("button[class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']")
#             sleep(5)
            
#             click_city_selector = f"mat-option[id='{click_city}']"
#             print(click_city_selector)
#             sb.click('mat-form-field[appearance="outline"]')
#             sb.click(click_city_selector)
            
#             sleep(5)
            
#             sb.click('mat-form-field[class="mat-form-field мат-form-field-outline-brand ng-tns-c64-8 mat-primary mat-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
#             sb.click('mat-option[id="mat-option-20"]')
#             sleep(5)
            
#             sb.click('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-6 мат-primary mat-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"')
#             sb.click('mat-option[id="mat-option-24"]')
#             sleep(10)
            
#             sb.type('input[id="mat-input-2"]', name)
#             sb.type('input[id="mat-input-3"]', surname)
            
#             if gender == "male":
#                 sb.click('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-12 мат-primary мат-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
#                 sb.click('mat-option[id="mat-option-29"]')
#             elif gender == "female":
#                 sb.click('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-12 мат-primary мат-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
#                 sb.click('mat-option[id="mat-option-28"]')
            
#             sb.type('input[id="dateOfBirth"]', date_of_birth)
            
#             sb.click('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-14 мат-primary мат-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
#             sb.click('mat-option[id="mat-option-205"]')
            
#             sb.type('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-16 мат-primary мат-form-field-type-mat-input мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"],', passport)
            
#             sb.type('input[id="passportExpirtyDate"]', passport_validity_period)
            
#             sb.type('input[id="mat-input-5"]', '8')
#             sb.type('input[id="mat-input-6"]', number_phone)
            
#             sb.type('input[id="mat-input-7"]', email)



# def main():
#     success = False
#     while not success:
#         try:
#             print("Бот запущен")
#             parsing_vfs_filling_data()
#             success = True
#             print("Бот сработал верно")
#         except Exception as e:
#             print("Возникла ошибка {e}" )
#             print("Пробуем снова")
            
            
# main()
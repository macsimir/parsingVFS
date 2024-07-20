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

Base = declarative_base()
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)



def parsing_vfs_filling_data():
    session = Session()
    # Исправление вызова метода для получения данных
    data = session.query(ActiveOrders).all()
    
    for entry in data:  # Перебор списка результатов
        name = entry.name
        surname = entry.surname
        gender = entry.gender
        date_of_birth = entry.date_of_birth
        passport = entry.passport_ID
        passport_validity_period = entry.passport_validity_period
        number_phone = entry.number_phone
        email = entry.email
        click_city = entry.click_city
        type_visa_click = entry.type_visa
        click_visa_sub = entry.subtype_visa
        if gender == "male":
            gender = "mat-option-29"
        elif gender == "female":
            gender = "mat-option-28"
        
        
        with SB(uc=True, user_data_dir=r'C:\Users\максим\AppData\Local\Google\Chrome\User Data') as sb: 
            sb.driver.uc_open_with_reconnect("https://visa.vfsglobal.com/rus/ru/fra/login", reconnect_time=20)
            sb.click('h1[class="fs-21 fs-sm-24 mb-10"]')
            sb.click("input[id='mat-input-0']")
            
            sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted"]')
            sleep(5)
            
            sb.click("button[class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']")
            sleep(5)
            
            click_city_selector = f"mat-option[id='{click_city}']"
            print(click_city_selector)
            sb.click('mat-form-field[appearance="outline"]')
            sb.click(click_city_selector)
            
            sleep(5)
            
            sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-8 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')

            sb.click(f'mat-option[id="{type_visa_click}"]')
            sleep(5)
            
            sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-6 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
            # sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-6 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
            sb.click(f'mat-option[id="{click_visa_sub}"]')
            sleep(10)
            
            sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-raised-button mat-button-base ng-star-inserted"]')
            sleep(5)
            
            
            sb.type('input[id="mat-input-2"]', name)
            sleep(5)
            sb.type('input[id="mat-input-3"]', surname)
            sleep(5)
            
           
            sb.click('mat-form-field[class="mat-form-field mat-form-field-outline-brand ng-tns-c64-14 mat-primary mat-form-field-type-mat-select mat-form-field-appearance-outline mat-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
            print("Пол выбран ")
            sb.click(f'mat-option[id="{gender}"]')
            sleep(5)

            sb.type('input[id="dateOfBirth"]', date_of_birth)
            
            sleep(5)
            sb.click('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-14 мат-primary мат-form-field-type-mat-select мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"]')
            sb.click('mat-option[id="mat-option-205"]')
            
            sleep(5)
            sb.type('mat-form-field[class="мат-form-field мат-form-field-outline-brand ng-tns-c64-16 мат-primary мат-form-field-type-mat-input мат-form-field-appearance-outline мат-form-field-can-float ng-untouched ng-pristine ng-invalid ng-star-inserted"],', passport)
            
            sleep(5)
            sb.type('input[id="passportExpirtyDate"]', passport_validity_period)
            
            sleep(5)
            sb.type('input[id="mat-input-5"]', '8')
            sb.type('input[id="mat-input-6"]', number_phone)
            
            sleep(5)
            sb.type('input[id="mat-input-7"]', email)
            
            sleep(5)
            sb.click('button[class="mat-focus-indicator mat-stroked-button mat-button-base btn btn-block btn-brand-orange mat-btn-lg"]')
            sleep(8)
            
            
            sb.click('button[class="mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base"]')
            sleep(15)
            
            sb.click('td[class="fc-daygrid-day fc-day fc-day-mon fc-day-past"]')
            sleep(20)

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

parsing_vfs_filling_data()
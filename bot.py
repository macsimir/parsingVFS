from seleniumbase import SB
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from aiogram.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from datetime import datetime
from db import ActiveOrders,Account
from button_bot import *
from state_bot import *
import asyncio
import pyperclip 
import random
import json
import re 
import time

bot = Bot(token="6975877359:AAHiKPfQSY82HE_WtfE_ZD4mEBeUF_z2DeM")
dp = Dispatcher()
Base = declarative_base()


@dp.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("Привет. Выбери действия:", reply_markup=start_btn())

@dp.message(Form_statements.name)
async def process_name(message: types.Message, state: FSMContext):
    global name
    name = message.text
    await state.set_state(Form_statements.surname)
    await message.reply("Введите вашу фамилию:")
    
@dp.message(Form_statements.surname)
async def process_name(message: types.Message, state: FSMContext):
    global surname
    surname = message.text
    await state.set_state(Form_statements.date_of_birth)
    await message.reply("Введите дату рождения которая указана в паспорте. В формате 01.01.2001")
    
@dp.message(Form_statements.date_of_birth )
async def process_name(message: types.Message, state: FSMContext):
    global date_of_birth
    date_of_birth = message.text
    await state.set_state(Form_statements.passport_ID )
    await message.reply("Введите номер паспорта")
    
@dp.message(Form_statements.passport_ID )
async def process_name(message: types.Message, state: FSMContext):
    global passport_ID
    passport_ID = message.text
    await state.set_state(Form_statements.passport_validity_period )
    await message.reply("Введите срок действия паспорта в формате 01.01.2001")

@dp.message(Form_statements.passport_validity_period)
async def passport_validity_period_command(message: types.Message, state:FSMContext):
    global passport_validity_period
    passport_validity_period = message.text
    await state.set_state(Form_statements.number_phone )
    await message.reply("Введите номер телефона")

@dp.message(Form_statements.number_phone)
async def process_name(message: types.Message, state: FSMContext):
    global number_phone 
    phone_number = message.text
    number_phone = re.sub(r'^\+7|^8', '', phone_number)
    cleaned_number = re.sub(r'\D', '', number_phone)  # Используем number_phone вместо phone_number
    if len(cleaned_number) == 10:
        await state.set_state(Form_statements.email)
        await message.reply("Введите почту")
    else:
        await message.answer("Номер не действителен")


@dp.message(Form_statements.email)
async def email_command(message: types.Message, state: FSMContext):
    global email
    email = message.text
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        await message.answer("Выберите пол", reply_markup=gender_user_btn())
    else:
        await message.answer("Некорректный адрес электронной почты, попробуйте снова")



@dp.callback_query(lambda c: c.data.startswith("g_"))
async def gender_command_vs(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]
    gender = "male" if action == "male" else "female"
    last_date = None
    success = False

    while not success:
        try:
            await callback.message.answer("Подождите...")
            last_date = parsing_vfs(click_city=click_city)
            success = True  # Если выполнение прошло успешно, выходим из цикла
        except Exception as e:
            # Обработка ошибки
            print(f"Произошла ошибка: {e}")
            await callback.message.answer("Произошла ошибка, пробуем снова...")

    await callback.message.answer(f'Последняя доступная дата {last_date}')
    await callback.message.answer("Заявка создана!")
 

    

@dp.callback_query(F.data == "new appointment")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Выберите нужный вам центр", reply_markup=sity_btn_1())
    
@dp.callback_query(F.data == "send_sity_1")
async def send_sity_btn1(callback: types.CallbackQuery):
    await callback.message.answer("Выберите нужный центр", reply_markup=sity_btn_2())

@dp.callback_query(F.data == "send_sity_2")
async def send_sity_btn2(callback: types.CallbackQuery):
    await callback.message.answer("Выберите нужный центр", reply_markup=sity_btn_3())

@dp.callback_query(F.data == "send_sity_3")
async def send_sity_btn3(callback: types.CallbackQuery):
    await callback.message.answer("Выберите нужный центр", reply_markup=sity_btn_4())

@dp.callback_query(F.data.startswith("sity_"))
async def city_selection(callback: types.CallbackQuery, state: FSMContext):
    global city, click_city
    city = None
    click_city = None
    action = callback.data.split("_")[1]
    if action == "ekb":
        click_city= "mat-option-2"
        city = "Екатеринбург"
    elif action == "irk":
        click_city= "mat-option-3"
        city = "Иркутск"
    elif action == "kzn":
        click_city= "mat-option-4"
        city = "Казань"
    elif action == "kali":
        click_city= "mat-option-5"
        city = "Калининград"
    elif action == "krasndar":
        click_city= "mat-option-6"
        city = "Краснодар"
    elif action == "krasn":
        click_city= "mat-option-7"
        city = "Красноярск"
    elif action == "msk":
        click_city= "mat-option-8"
        city = "Москва"
        
        click_city= "mat-option-9"
        city = "Нижний Новгород"
    elif action == "nvsb":
        click_city= "mat-option-10"
        city = "Новосибирск"
    elif action == "perm":
        click_city= "mat-option-11"
        city = "Пермь"
    elif action == "spb":
        click_city= "mat-option-12"
        city = "Санкт-Петербург"
    elif action == "srtv":
        click_city= "mat-option-13"
        city = "Саратов"
    elif action == "ufa":
        click_city= "mat-option-14"
        city = "Уфа"
    elif action == "hbrvsk":
        click_city= "mat-option-15"
        city = "Хабаровск"
    elif action == "vldvstk":
        click_city= "mat-option-16"
        city = "Владивосток"
    elif action == "omsk":
        click_city= "mat-option-17"
        city = "Омск"
    elif action == "samara":
        click_city= "mat-option-18"
        city = "Самара"
    elif action == "rostov":
        click_city= "mat-option-19"
        city = "Ростов-на-Дону"
    await state.set_state(Form_statements.name)
    await callback.message.answer("Введите ваше имя:")

@dp.callback_query(F.data == "new_acc")
async def new_acc_command(callback: types.CallbackQuery, state: FSMContext ):
    await callback.message.answer("Введите почту")
    await state.set_state(New_account.email)  # Исправлено

@dp.message(New_account.email)  # Исправлено
async def new_acc_email_command(message: types.Message, state: FSMContext):
    global email_new_acc
    email_new_acc = message.text  # Исправлено
    await state.set_state(New_account.password)  # Исправлено
    await message.answer("Введите пароль")
    
@dp.message(New_account.password)  # Исправлено
async def new_acc_password_command(message: types.Message, state: FSMContext):  # Исправлено
    password_new_acc = message.text  # Исправлено
    data_new_acc = Account(email=email_new_acc, password=password_new_acc)
    await message.answer("Аккаунт добавлен и теперь он будет использоваться, когда один из аккаунтов забанят")
    session = Session()
    session.add(data_new_acc)
    session.commit() 
    session.close()
    await state.clear()  # Сброс состояния после завершения процессаунт добавлен и теперь он будет использоваться когда один из аккаунтов забанят")


        
def parsing_vfs(click_city):
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
        time.sleep(10)

                
                
        alert_info = sb.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-info.border-0.rounded-0.ng-star-inserted")
        last_date = alert_info.text
        return last_date



engine = create_engine('sqlite:///DATABASE.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

async def main():
    session = Session()
    print("Бот @vfs_parsing_bot запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
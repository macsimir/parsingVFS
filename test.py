from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import memory
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import logging

# Define states
class Form(StatesGroup):
    name = State()
    surname = State()
    date_of_birth = State()
    passport_ID = State()
    passport_validity_period = State()
    number_phone = State()
    email = State()

# Set up the database connection
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Callback query handler
@dp.callback_query_handler(lambda c: c.data.startswith("g_"))
async def gender_command_vs(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]
    gender = "male" if action == "male" else "female"
    await state.update_data(gender=gender)  # Store the gender in the state

    last_date = None
    success = False

    while not success:
        try:
            await callback.message.answer("Подождите...")
            last_date = parsing_vfs(click_city=click_city)
            success = True  # Если выполнение прошло успешно, выходим из цикла
        except Exception as e:
            # Обработка ошибки
            logging.error(f"Произошла ошибка: {e}")
            await callback.message.answer("Произошла ошибка, пробуем снова...")

    await state.update_data(last_date=last_date)  # Store the last_date in the state

    # Proceed to collect additional information
    await callback.message.answer("Пожалуйста, введите ваше имя:")
    await Form.name.set()

# State handlers for collecting additional information
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Пожалуйста, введите вашу фамилию:")
    await Form.surname.set()

@dp.message_handler(state=Form.surname)
async def process_surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Пожалуйста, введите вашу дату рождения (дд-мм-гггг):")
    await Form.date_of_birth.set()

@dp.message_handler(state=Form.date_of_birth)
async def process_date_of_birth(message: types.Message, state: FSMContext):
    await state.update_data(date_of_birth=message.text)
    await message.answer("Пожалуйста, введите номер вашего паспорта:")
    await Form.passport_ID.set()

@dp.message_handler(state=Form.passport_ID)
async def process_passport_ID(message: types.Message, state: FSMContext):
    await state.update_data(passport_ID=message.text)
    await message.answer("Пожалуйста, введите срок действия вашего паспорта:")
    await Form.passport_validity_period.set()

@dp.message_handler(state=Form.passport_validity_period)
async def process_passport_validity_period(message: types.Message, state: FSMContext):
    await state.update_data(passport_validity_period=message.text)
    await message.answer("Пожалуйста, введите ваш номер телефона:")
    await Form.number_phone.set()

@dp.message_handler(state=Form.number_phone)
async def process_number_phone(message: types.Message, state: FSMContext):
    await state.update_data(number_phone=message.text)
    await message.answer("Пожалуйста, введите ваш email:")
    await Form.email.set()

@dp.message_handler(state=Form.email)
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)

    # Retrieve all data from state
    user_data = await state.get_data()

    # Create new ActiveOrders entry
    new_order = ActiveOrders(
        last_date=user_data['last_date'],
        right_center_city=user_data['right_center_city'],
        click_city=user_data['click_city'],
        name=user_data['name'],
        surname=user_data['surname'],
        gender=user_data['gender'],
        date_of_birth=user_data['date_of_birth'],
        passport_ID=user_data['passport_ID'],
        passport_validity_period=user_data['passport_validity_period'],
        number_phone=user_data['number_phone'],
        email=user_data['email']
    )

    # Add to the session and commit
    session.add(new_order)
    session.commit()

    await message.answer(f'Последняя доступная дата {user_data["last_date"]}')
    await message.answer("Заявка создана!")

    # Finish conversation
    await state.finish()

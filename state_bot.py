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

class New_account(StatesGroup):
    email = State() #Почта
    password = State() #Пароль


class Form_statements(StatesGroup):
    """Форма чтобы их задавал бот"""
    name = State() #Имя 
    surname = State() #Фамилия 
    date_of_birth = State() #Дата рождения 
    passport_ID = State() #Номер паспорта 
    passport_validity_period = State() #Срок действия 
    number_phone = State() #Номера телефона
    email = State() #Email
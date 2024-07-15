from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_btn():
    buttons = [
        [types.InlineKeyboardButton(text="Новая запись", callback_data="new appointment"), types.InlineKeyboardButton(text="Поменять аккаунт", callback_data="new_acc")]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def sity_btn_1():
    buttons = [
        [types.InlineKeyboardButton(text="Екатеринбург", callback_data="sity_ekb"),
         types.InlineKeyboardButton(text="Иркутск", callback_data="sity_irk")],
        [types.InlineKeyboardButton(text="Казань", callback_data="sity_kzn"),
         types.InlineKeyboardButton(text="Калининград", callback_data="sity_kali")],
        [types.InlineKeyboardButton(text="Краснодар", callback_data="sity_krasndar"),
            types.InlineKeyboardButton(text="→", callback_data="send_sity_1")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def sity_btn_2():
    buttons = [
        [types.InlineKeyboardButton(text="Красноярск", callback_data="sity_krasn"),
         types.InlineKeyboardButton(text="Москва", callback_data="sity_msk")],
        [types.InlineKeyboardButton(text="Нижний Новгород", callback_data="sity_nvsb"),
         types.InlineKeyboardButton(text="Новосибирск", callback_data="sity_nvsb")],
        [types.InlineKeyboardButton(text="→", callback_data="send_sity_2")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def sity_btn_3():
    buttons = [
        [types.InlineKeyboardButton(text="Пермь", callback_data="sity_perm"),
         types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="sity_spb")],
        [types.InlineKeyboardButton(text="Саратов", callback_data="sity_srtv"),
         types.InlineKeyboardButton(text="Уфа", callback_data="sity_ufa")],
        [types.InlineKeyboardButton(text="→", callback_data="send_sity_3")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def sity_btn_4():
    buttons = [
        [types.InlineKeyboardButton(text="Хабаровск", callback_data="sity_hbrvsk"),
         types.InlineKeyboardButton(text="Владивосток", callback_data="sity_vldvstk")],
        [types.InlineKeyboardButton(text="Омск", callback_data="sity_omsk"),
         types.InlineKeyboardButton(text="Самара", callback_data="sity_samara")],
        [types.InlineKeyboardButton(text="Ростов-на-Дону", callback_data="sity_rostov")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard



def gender_user_btn():
    buttons = [
        [
            types.InlineKeyboardButton(text="Мужской пол", callback_data="g_male"),
            types.InlineKeyboardButton(text="Женский пол", callback_data="g_female")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
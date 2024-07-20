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
        [types.InlineKeyboardButton(text="Новая запись", callback_data="new appointment"), types.InlineKeyboardButton(text="Поменять аккаунт", callback_data="new_acc")],
        [types.InlineKeyboardButton(text="Активные заявки", callback_data="all_active_orders")]
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

def type_visa_btn():
    buttons = [
        [
            types.InlineKeyboardButton(text="Краткосрочная виза", callback_data="v_short"),
            types.InlineKeyboardButton(text="Национальная виза", callback_data="v_national")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def subtype_visa_btn_short():
    buttons = [
        [
            types.InlineKeyboardButton(text="Держатели дипломатических или служебных паспортов", callback_data="s_1"),
            types.InlineKeyboardButton(text="Другие краткосрочные визы", callback_data="s_2")
        ],
        [
            types.InlineKeyboardButton(text="Красткосрочная виза с деловой или профессиональной целью", callback_data="s_3"),
            types.InlineKeyboardButton(text="Краткосрочная виза для водителей, задействованных в международных перевозках!", callback_data="s_4")
        ],
        [            
            types.InlineKeyboardButton(text="Краткосрочная виза для моряков", callback_data="s_5"),
            types.InlineKeyboardButton(text="Краткосрочная виза для членов летного экипажа", callback_data="s_6")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def subtype_visa_btn_national():
    buttons = [
        [
            types.InlineKeyboardButton(text="Carte PRO MAE", callback_data="n_1"),
            types.InlineKeyboardButton(text="Lecteur et assistant de langue", callback_data="n_2")
        ],
        [
            types.InlineKeyboardButton(text="Salarié OFII проект 'СОЮЗ'", callback_data="n_3"),
            types.InlineKeyboardButton(text="Долгосрочная виза 'Бенифициары положительного решения OFII о воссоединении семь'", callback_data="n_4")
        ],
        [
            types.InlineKeyboardButton(text="Долгосрочная виза Passeport Talent + сопровождающие члены семьи", callback_data="n_5"),
            types.InlineKeyboardButton(text="Долгосрочная виза для обучения в высшем усебном заведении", callback_data="n_6")
        ],
        [
            types.InlineKeyboardButton(text="Другие долгосрочные визы", callback_data="n_7"),
            types.InlineKeyboardButton(text="Ученые, приглашенные французскими научно исследовательскими институтами", callback_data="n_8")
        ],
    ]
    
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
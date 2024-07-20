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
engine = create_engine('sqlite:///DATABASE.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)




def gender():
    session = Session()
    # Исправление вызова метода для получения данных
    data = session.query(ActiveOrders).all()
    for entry in data:
        gender = entry.gender
    if gender == "male":
        print('муж')
    elif gender == "female":
        print('жен')
gender()
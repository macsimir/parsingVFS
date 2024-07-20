from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean,Date
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

class ActiveOrders(Base):
    __tablename__ = "active_orders"
    id = Column(Integer, primary_key=True)
    last_date = Column(String)
    right_center_city = Column(String)
    click_city = Column(String)
    type_visa = Column(String)
    subtype_visa = Column(String)
    name = Column(String)
    surname = Column(String)
    gender = Column(String)
    date_of_birth = Column(String)
    passport_ID = Column(String)
    passport_validity_period = Column(String)
    number_phone = Column(String)
    email = Column(String)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    
    
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
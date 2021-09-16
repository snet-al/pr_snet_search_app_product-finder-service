from sqlalchemy import create_engine
from database.base import Base
from database.model import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://admin:admin321@localhost', echo=True)
session = sessionmaker(bind=engine)()
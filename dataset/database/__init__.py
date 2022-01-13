from sqlalchemy import create_engine
from dataset.database.model import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://admin:admin321@localhost:3306/spar', echo=True)
session = sessionmaker(bind=engine)()
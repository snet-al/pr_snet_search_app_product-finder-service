from sqlalchemy import *
from dataset.database.model import Model
from sqlalchemy.orm import relationship


class ShopModel(Model):

    __tablename__ = 'business_sectors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    web_name = Column(String)

    def __repr__(self):
        return "<Shop(name='%s')>" % self.name

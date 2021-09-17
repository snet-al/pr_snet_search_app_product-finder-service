from sqlalchemy import *
from dataset.database.model import Model
from sqlalchemy.orm import relationship


class ProductModel(Model):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    sale_price = Column(String)
    sector_ids = Column(String)

    def __repr__(self):
        return "<Product(name='%s')>" % self.name

from dataset.models.shop_model import ShopModel
from dataset.database import *

class Shop:

    @staticmethod
    def get_from_db():
        return session.query(ShopModel).all()

def test():
    print(__name__ + "/shop/test")
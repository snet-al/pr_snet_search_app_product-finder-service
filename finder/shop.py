from dataset.models.shop_model import ShopModel

class Shop:

    @staticmethod
    def get_from_db():
        return ShopModel.all()

def test():
    print(__name__ + "/shop/test")
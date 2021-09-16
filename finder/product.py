from dataset.database import *
from dataset.models.product_model import ProductModel
from finder.compare import is_similar

class Product:
    @staticmethod
    def similar(product1: ProductModel, product2: ProductModel):
        return is_similar(product1.name.lower(), product2.name.lower())


    @staticmethod
    def get_from_db():
        return session.query(ProductModel).filter(ProductModel.parent_id != 0).all()

    @staticmethod
    def get_from_db_per_sector(sector_id):
        return session(ProductModel).filter(ProductModel.parent_id != 0).filter(ProductModel.sector_ids == "_" + sector_id + "_").all()


class ParentProduct:
    @staticmethod
    def get_from_db():
        return session.query(ProductModel).filter(ProductModel.parent_id != 0).all()

    @staticmethod
    def find(id):
        return session.query(ProductModel).filter(ProductModel.parent_id != 0).filter(ProductModel.id == id).all()

    @staticmethod
    def add(product):
        new_product = ProductModel(**product.asdict())
        session.add(new_product)
        session.commit()
        return new_product

def test():
    print(__name__ + "/product/test")
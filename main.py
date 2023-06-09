from dataset.database import *
from finder.shop import Shop
from finder.product import Product, ParentProduct

def main():
    shops = Shop.get_from_db()
    products_per_shop = {}
    for shop in shops:
        products_of_shop = Product.get_from_db_per_shop(shop.id)
        products_per_shop[shop.id] = products_of_shop

    for shop in shops:
        shop_id = shop.id
        for base_product in products_per_shop[shop_id]:
            base_parent_product = ParentProduct.find(base_product.id)
            if base_parent_product is None:
                base_parent_product = ParentProduct.add(base_parent_product)

            for shop_to_compare in shops:
                if shop_id == shop_to_compare.id: continue

                shop_to_compare_id = shop_to_compare.id
                most_similar_inside_a_shop = 0
                most_similar_inside_a_shop_ratio = 0

                for product_to_compare in products_per_shop[shop_to_compare_id]:
                    similarity = Product.similar(base_parent_product, product_to_compare)
                    if similarity > most_similar_inside_a_shop_ratio:
                        most_similar_inside_a_shop_ratio = similarity
                        most_similar_inside_a_shop = product_to_compare

                base_parent_product.sector_ids += ',' + most_similar_inside_a_shop.sector_ids
                most_similar_inside_a_shop.parent_id = base_parent_product.id
                session.add(base_parent_product)
                session.add(most_similar_inside_a_shop)
                session.commit()


if __name__ == '__main__':
    main()
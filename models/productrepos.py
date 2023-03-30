from requests import Session
from sqlalchemy import delete
from models.product import Product
from models.session import session


class ProductRepository:

    def __init__(self, session):
        self.__session: Session = session

    def get_all(self):
        '''

        :return: all products
        '''
        for product in self.__session.query(Product).all():
            print(product)

    def add_item(self):
        '''

        :return: add new product in to table
        '''
        new_product = Product(name="Maslo", price="11")
        self.__session.add(new_product)
        self.__session.commit()
        return new_product.id

    def update_by_id(self, id, name):
        '''

        :param id: product id
        :param name: name of product
        :return: updated product
        '''
        self.__session.query(Product).filter_by(id=f"{id}").update({"name": name})
        self.__session.commit()

    def delete_by_id(self, id):
        '''

        :param id: id of product
        :return: delete product by id
        '''
        self.__session.query(Product).filter_by(id=f"{id}").delete()
        self.__session.commit()


if __name__ == "__main__":
    product = ProductRepository(session)
    product.get_all()
    id_added_item = product.add_item()
    product.get_all()
    product.update_by_id(id_added_item, "Slivochnoe maslo")
    product.get_all()
    product.delete_by_id(id_added_item)
    product.get_all()

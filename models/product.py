from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, VARCHAR, DECIMAL


Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id: int = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20))
    price = Column(DECIMAL)

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nprice: {self.price}"

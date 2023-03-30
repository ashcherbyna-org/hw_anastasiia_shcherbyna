from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Qwerty12!@localhost:32768/store")
__session = sessionmaker(engine)
session: Session = __session()
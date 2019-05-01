from tiktok.handlers import DBHandler
from tiktok.structures.base import Base


if __name__ == '__main__':
    db_handler = DBHandler()
    Base.metadata.drop_all(bind=db_handler.get_engine())
    Base.metadata.create_all(bind=db_handler.get_engine())

from tiktok.handlers import Handler
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class DBHandler(Handler):

    def __init__(self, conn_uri=None):
        """
        init save folder
        :param folder:
        """
        super().__init__()
        if not conn_uri:
            # conn_uri = "postgres://admin:password@localhost:5432/tiktok"
            conn_uri = "sqlite:///../app.sqlite"
        self.db = create_engine(conn_uri)

    def get_engine(self):
        return self.db

    async def process(self, obj, **kwargs):
        """
        download to file
        :param url: resource url
        :param name: save name
        :param kwargs:
        :return:
        """
        db_session = sessionmaker(bind=self.db)
        session = db_session()

        # save to db
        print('Saving', obj, 'to db...')
        session.merge(obj)
        session.commit()
        print('Saved', obj, 'to db successfully')

from tiktok.structures import Base
from sqlalchemy import Column, String, DateTime


class TikTokUser(Base):
    __tablename__ = 'tiktok_user'

    id = Column(String(20), primary_key=True)
    gender = Column(String(200))
    name = Column(String(200))
    create_time = Column(DateTime(), nullable=True)
    birthday = Column(String(50), nullable=True)
    sign = Column(String(500))
    alias = Column(String(50))
    avatar = Column(String(200))
    verify = Column(String(200))
    verify_info = Column(String(2000))
    
    def __init__(self, **kwargs):
        """
        init user object
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.gender = kwargs.get('gender')
        self.name = kwargs.get('name')
        self.create_time = kwargs.get('create_time')
        self.birthday = kwargs.get('birthday')
        self.sign = kwargs.get('sign')
        self.alias = kwargs.get('alias')
        self.avatar = kwargs.get('avatar')
        self.verify = kwargs.get('verify')
        self.verify_info = kwargs.get('verify_info')
    
    def __repr__(self):
        """
        user to str
        :return:
        """
        return '<User: <%s, %s>>' % (self.alias, self.name)

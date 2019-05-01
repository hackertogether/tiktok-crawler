from tiktok.structures import Base
from sqlalchemy import Column, String, Float


class TikTokAddress(Base):

    __tablename__ = 'tiktok_address'

    id = Column(String(20), primary_key=True)
    province = Column(String(50))
    city = Column(String(50))
    district = Column(String(50))
    full = Column(String(500))
    address = Column(String(250))
    place = Column(String(250))
    postal_code = Column(String(50))
    longitude = Column(Float())
    latitude = Column(Float())
    
    def __init__(self, **kwargs):
        """
        init address object
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.province = kwargs.get('province')
        self.city = kwargs.get('city')
        self.district = kwargs.get('district')
        self.full = kwargs.get('full')
        self.address = kwargs.get('address')
        self.place = kwargs.get('place')
        self.postal_code = kwargs.get('postal_code')
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
    
    def __repr__(self):
        """
        address to str
        :return:
        """
        return '<Address: <%s, %s>>' % (self.id, self.place)

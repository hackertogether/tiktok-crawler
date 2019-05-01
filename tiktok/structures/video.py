from sqlalchemy.orm import relationship, backref

from tiktok.structures import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey


class TikTokVideo(Base):
    __tablename__ = 'tiktok_video'

    id = Column(String(20), primary_key=True)
    desc = Column(String(2000))
    like_count = Column(Integer())
    comment_count = Column(Integer())
    share_count = Column(Integer())
    hot_count = Column(Integer())
    play_url = Column(String(100))
    is_ads = Column(Boolean())
    duration = Column(Integer())
    create_time = Column(DateTime(), nullable=True)
    share_url = Column(String(100))
    ratio = Column(Integer())
    cover_url = Column(String(100))
    address = Column(String(100))

    author_id = Column(String, ForeignKey('tiktok_user.id'))
    author = relationship('TikTokUser', backref=backref("tiktok_user", uselist=False))
    music_id = Column(String, ForeignKey('tiktok_music.id'))
    music = relationship('TikTokMusic', backref=backref("tiktok_music", uselist=False))

    def __init__(self, **kwargs):
        """
        init video object
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.desc = kwargs.get('desc')
        self.author = kwargs.get('author')
        self.music = kwargs.get('music')
        self.like_count = kwargs.get('like_count')
        self.comment_count = kwargs.get('comment_count')
        self.share_count = kwargs.get('share_count')
        self.hot_count = kwargs.get('hot_count')
        self.play_url = kwargs.get('play_url')
        self.is_ads = kwargs.get('is_ads') or False
        self.duration = kwargs.get('duration')
        self.create_time = kwargs.get('create_time')
        self.share_url = kwargs.get('share_url')
        self.ratio = kwargs.get('ratio')
        self.cover_url = kwargs.get('cover_url')
        self.address = kwargs.get('address')

    def __repr__(self):
        """
        video to str
        :return: str
        """
        return '<Video: <%s, %s>>' % (self.id, self.desc[:10].strip() if self.desc else None)

from tiktok.structures import Base
from tiktok.utils.fetch import fetch
from tiktok.config import music2video_url, common_headers
from sqlalchemy import Column, String, Integer


class TikTokMusic(Base):
    __tablename__ = 'tiktok_music'

    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    cover_url = Column(String(250))
    play_url = Column(String(250))
    owner_id = Column(String(50))
    owner_name = Column(String(50))
    hot_count = Column(Integer())

    def __init__(self, **kwargs):
        """
        music init args
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.cover_url = kwargs.get('cover_url')
        self.play_url = kwargs.get('play_url')
        self.owner_id = kwargs.get('owner_id')
        self.owner_name = kwargs.get('owner_name')
        self.hot_count = kwargs.get('hot_count')

    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Music: <%s, %s>>' % (self.id, self.name)

    def videos(self, max=None):
        """
        get videos of topic
        :return:
        """
        if max and not isinstance(max, int):
            raise RuntimeError('`max` param must be int')
        from tiktok.utils.tranform import data_to_video
        query = {
            'device_id': '33333333',
            'music_id': self.id,
            'count': '18',
        }
        offset, count = 0, 0
        while True:
            # define cursor
            query['cursor'] = str(offset)
            result = fetch(music2video_url, params=query, headers=common_headers, verify=False)
            aweme_list = result.get('aweme_list', [])
            for item in aweme_list:
                video = data_to_video(item)
                count += 1
                yield video
                if max and count >= max:
                    return
            # next page
            if result.get('has_more'):
                offset += 18
            else:
                break

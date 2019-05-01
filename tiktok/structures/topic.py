from tiktok.structures import Base
from tiktok.utils.fetch import fetch
from tiktok.config import topic2video_url, common_headers, common_parameter
from tiktok.utils.signature import generate_signature
from sqlalchemy import Column, String, Integer


class TikTokTopic(Base):
    __tablename__ = 'tiktok_topic'

    id = Column(String(20), primary_key=True)
    view_count = Column(Integer())
    user_count = Column(Integer())
    name = Column(String(50))
    desc = Column(String(50))

    def __init__(self, **kwargs):
        """
        init topic object
        :param kwargs:
        """
        self.id = kwargs.get('id')
        self.view_count = kwargs.get('view_count')
        self.user_count = kwargs.get('user_count')
        self.name = kwargs.get('name')
        self.desc = kwargs.get('desc')

    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Topic: <%s, %s>>' % (self.id, self.name)

    def videos(self, max=None):
        """
        get videos of topic
        :return:
        """
        from tiktok.utils.tranform import data_to_video
        if max and not isinstance(max, int):
            raise RuntimeError('`max` param must be int')
        query = {
            'count': '9',
            'cursor': '0',
            'aid': '1128',
            'screen_limit': '3',
            'download_click_limit': '0',
            'ch_id': self.id,
            '_signature': generate_signature(str(self.id))
        }
        cursor, video_count = None, 0
        while True:
            # define cursor
            if cursor:
                query['cursor'] = str(cursor)
                query['_signature'] = generate_signature(str(self.id) + '9' + str(cursor))
            result = fetch(topic2video_url, params=query, headers=common_headers)
            aweme_list = result.get('aweme_list', [])
            if not aweme_list:
                break
            for aweme in aweme_list:
                video = data_to_video(aweme)
                video_count += 1
                yield video
            if result.get('has_more'):
                cursor = result.get('cursor')
            else:
                break

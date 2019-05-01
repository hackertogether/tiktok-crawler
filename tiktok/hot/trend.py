from tiktok.utils import fetch
from tiktok.config import common_parameter
from tiktok.utils.tranform import data_to_music, data_to_topic
from tiktok.structures.hot import HotTrend
from tiktok.utils.common import parse_datetime


def trend(hot_trend_url, count, **kwargs):
    """
    get trend result
    :return:
    """
    offset = 0
    while True:
        common_parameter['cursor'] = str(offset)
        result = fetch(hot_trend_url, params=common_parameter, **kwargs)
        category_list = result.get('category_list')
        datetime = parse_datetime(result.get('extra', {}).get('now'))
        final = []
        for item in category_list:
            # process per category
            if item.get('desc') == '热门话题':
                final.append(data_to_topic(item.get('challenge_info', {})))
            if item.get('desc') == '热门音乐':
                final.append(data_to_music(item.get('music_info', {})))
        yield HotTrend(datetime=datetime, data=final, offset=offset, count=count)
        offset += 10

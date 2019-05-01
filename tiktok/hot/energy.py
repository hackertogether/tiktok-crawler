from tiktok.structures import HotEnergy
from tiktok.utils import fetch
from tiktok.utils.common import parse_datetime
from tiktok.utils.tranform import data_to_video


def energy(hot_energy_url, **kwargs):
    """
    get hot energy result
    :return: HotEnergy object
    """
    result = fetch(hot_energy_url, **kwargs)
    # process json data
    datetime = parse_datetime(result.get('active_time'))
    video_list = result.get('aweme_list', [])
    videos = []
    for item in video_list:
        video = data_to_video(item.get('aweme_info'))
        video.hot_count = item.get('hot_value')
        videos.append(video)
    # construct HotEnergy object and return
    return HotEnergy(datetime=datetime, data=videos)
